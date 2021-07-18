from flask import Blueprint, request, render_template

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('base.html', title="Audio Track Splitter")