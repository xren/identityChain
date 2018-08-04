from flask import Blueprint, request, abort, make_response, jsonify, url_for
from flask.views import MethodView
import json
import requests
from facepp import API
facial_recognition = Blueprint('facial_recognition', __name__)

api = API('J2WKF74Tb9d2ilM0PZDG6TQCiYulVbdW', 'ewUvvuO8yanG9fTb2HI9PzKPNNi92Amu')
FACESET_TOKEN = 'd73b8dff7aceb173137627124d8eba21'
REDIRECT_URL = '/nber/{}'

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
        if res['confidence'] > 70:
          matched_result = res['face_token']
          break
    if matched_result:
      if matched_result == '955908f21856a8ba3af0ac7362143fcb':
        name = 'rex'
      elif matched_result == '66824f9afa377043fc4ad7e1de6090b6':
        name = 'seven'
      redirect_url = REDIRECT_URL.format(name)
    print matched_result
    return make_response(jsonify({
      'name': name,
      'redirect_url': redirect_url
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
