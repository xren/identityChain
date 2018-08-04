from flask import Blueprint, request, abort, make_response, jsonify, url_for
from flask.views import MethodView
import json
import requests
from facepp import API
facial_recognition = Blueprint('facial_recognition', __name__)

api = API('J2WKF74Tb9d2ilM0PZDG6TQCiYulVbdW', 'ewUvvuO8yanG9fTb2HI9PzKPNNi92Amu')
FACESET_TOKEN = 'd73b8dff7aceb173137627124d8eba21'
REDIRECT_URL = '/nber/post_auth/{}'

class CapturedImage(MethodView):
  def post(self):
    print 'capturing image'
    post_data = json.loads(request.get_data())
    image_base_64 = post_data['imageBase64']
    res = api.detect(image_base64=image_base_64)
    matched_result = None
    name = 'alien'
    redirect_url = None
    print 'detect', res
    if len(res['faces']) != 0:
      face_token = res['faces'][0]['face_token']
      search_results = api.search(face_token=face_token, faceset_token=FACESET_TOKEN)
      print search_results['results']
      for res in search_results['results']:
        if res['confidence'] > 80:
          matched_result = True
          matched_token = res['face_token']
          break

      if matched_result:
        r = requests.get('http://localhost:3100/api/user/'+matched_token)
        
        if r.status_code == 200:
            uuid = json.loads(r.content)['uuid']
            return make_response(jsonify({
              'redirect_url': REDIRECT_URL.format(uuid)
            }))
        else:
          data = {"$class": "org.identitychain.biznet.user","uuid": matched_token}
          response = requests.post('http://localhost:3100/api/user', data=data)
          uuid = json.loads(response.content)['uuid']
          return make_response(jsonify({
           'redirect_url': REDIRECT_URL.format(uuid)
          }))
      else:
        return make_response(jsonify({
          'redirect_url': REDIRECT_URL.format(face_token)
        }))

class AddNewImage(MethodView):
  def post(self):
    post_data = json.loads(request.get_data())
    image_base_64 = post_data['imageBase64']
    res = api.detect(image_base64=image_base_64)
    matched_result = None
    status = 'face not detected'
    if len(res['faces']) != 0:
      face_token = res['faces'][0]['face_token']
      search_results = api.search(face_token=face_token, faceset_token=FACESET_TOKEN)
      for res in search_results['results']:
        print res
        if res['confidence'] > 80:
          matched_result = res['face_token']
          break
      if not matched_result:
        api.faceset.addface(faceset_token=FACESET_TOKEN, face_tokens=[face_token])
        status = 'added new face to pool'
      else:
        status = 'face already exists'
    return make_response(jsonify({
      'status': status
    }))


facial_recognition.add_url_rule('/api/fr/capture', view_func=CapturedImage.as_view('capture'), methods=['POST'])
facial_recognition.add_url_rule('/api/fr/addnewface', view_func=AddNewImage.as_view('addnewface'), methods=['POST'])
