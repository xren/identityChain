from flask import Blueprint, render_template as view
from flask import request

nber = Blueprint('nber', __name__, static_folder='static', template_folder='templates')
uuidlist = {'Lanchao', 'Seven'}

@nber.route('/nber/<name>')
def index(name=None):
    """
    Show an index template
    :return:
    """
    return view('nber/index.html')


@nber.route('/nber/post_auth')
def post_auth():
    # http://identityChain.com/nber/post_auth?uuid=[uuid]
    uuid = request.args.get('uuid')
    if uuid in uuidlist: 
        return view('/nber/signin.html')
    else:
        return view('/nber/signup.html')

