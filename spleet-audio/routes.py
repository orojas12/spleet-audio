import os

from flask import Blueprint, request, render_template, current_app
from werkzeug.utils import secure_filename, send_file

from .separation import separate_2stems, separate_4stems
from .utils import id_generator, zipped_output_file

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('base.html', title="Spleet Audio")

@bp.route('/spleet', methods=['POST'])
def spleet():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    output_folder = current_app.config['OUTPUT_FOLDER']

    song = request.files.get('song')
    if song is None:
        return '400'

    filename = os.path.splitext(secure_filename(song.filename))[0]
    if filename == '' or filename is None:
        filename = id_generator()

    filepath = os.path.join(upload_folder, filename)
    song.save(filepath)

    if request.form.get('separation_type') == '2stems':
        separate_2stems(filepath, output_folder, filename)
    elif request.form.get('separation_type') == '4stems':
        separate_4stems(filepath, output_folder, filename)
    
    prediction_path = os.path.join(output_folder, filename)

    song_zip = zipped_output_file(prediction_path)
    
    return send_file(song_zip, environ=request.environ, as_attachment=True, download_name=filename + '.zip', mimetype='application/zip')
    