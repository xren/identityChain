from flask import Blueprint, request, abort, make_response, jsonify, url_for

facial_recognition = Blueprint('facial_recognition', __name__)

@facial_recognition.route('/fr/helloworld', methods=['GET'])
def helloworld():
  return make_response(jsonify({
    'name': 'hello world'
  }))