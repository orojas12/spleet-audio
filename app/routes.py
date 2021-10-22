import os

from flask import Blueprint, request, render_template, current_app, make_response
from werkzeug.utils import secure_filename, send_file

from .separation import separate
from .utils import clean_folder, id_generator, zipped_output_file, get_file_names

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('base.html', title="Spleet Audio")

@bp.route('/spleet', methods=['POST'])
def spleet():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    output_folder = current_app.config['OUTPUT_FOLDER']

    upload = request.files.get('upload')
    if not upload:
        return '400'

    separation_type = request.form.get('separation_type')
    if not separation_type:
        return '400'

    filename = os.path.splitext(secure_filename(upload.filename))[0]

    upload_id = id_generator()
    upload_path = os.path.join(upload_folder, upload_id)
    upload.save(upload_path)
    
    separate(upload_path, output_folder, upload_id, separation_type)

    prediction_id = upload_id
    prediction_path = os.path.join(output_folder, prediction_id)
    track_names = get_file_names(prediction_path)

    # clean_folder(upload_folder)

    response = make_response(
        render_template('results.html', 
            upload_name=filename, 
            prediction_id=prediction_id, 
            track_names=track_names
        )
    )
    response.headers['Cache-Control'] = 'no-store, max-age=0'
    return response

@bp.route('/download/<id>/<file>', methods=['GET'])
def download(id, file):
    # return send_file(
    #     song_zip, 
    #     environ=request.environ, 
    #     as_attachment=True, 
    #     download_name=filename + '.zip', 
    #     mimetype='application/zip'
    # )
    pass
