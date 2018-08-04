from flask import Blueprint, render_template as view

identitychain = Blueprint('identitychain', __name__, static_folder='static', template_folder='templates')


@identitychain.route('/identitychain')
def index():
    """
    Show an index template
    :return:
    """
    return view('identitychain/index.html')

@identitychain.route('/addnewface')
def addnewface():
    """
    Show an index template
    :return:
    """
    return view('identitychain/addnewface.html')
