from flask import Blueprint, render_template as view

nber = Blueprint('nber', __name__, static_folder='static', template_folder='templates')


@nber.route('/nber')
def index():
    """
    Show an index template
    :return:
    """
    return view('nber/index.html')
