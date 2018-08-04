from flask import Blueprint, render_template as view
from flask import request

nber = Blueprint('nber', __name__, static_folder='static', template_folder='templates')
uuidlist = {
    'dd4693d9c8ce73b42e65418c31d76fc5': 'chengliang',
    'ec543e8975947be3f1e9702ccaff1d07': 'lanchao',
    '66824f9afa377043fc4ad7e1de6090b6': 'seven',
    '955908f21856a8ba3af0ac7362143fcb': 'rex',
    '9326a1f61e17af29ee93ca0b467925d2': 'xinyuan',
    'ff4091ff21f8ddb75c331770e2f10761': 'zack'
}

@nber.route('/nber/<name>')
def index(name=None):
    """
    Show an index template
    :return:
    """
    return view('nber/index.html')


@nber.route('/nber/post_auth/<uuid>')
def post_auth(uuid=None):
    # http://identityChain.com/nber/post_auth/uuid=[uuid]
    uuid = request.args.get('uuid')
    if uuid in uuidlist:
        return view('/nber/signin.html', name=name)
    else:
        return view('/nber/signup.html')

