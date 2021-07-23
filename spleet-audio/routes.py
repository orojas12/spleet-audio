import os
from flask import Blueprint, request, render_template, current_app
from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
from werkzeug.utils import secure_filename

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('base.html', title="Spleet Audio")

@bp.route('/split', methods=['POST'])
def split():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    output_folder = current_app.config['OUTPUT_FOLDER']

    song = request.files.get('song')
    if song is None:
        return '400'

    filename = secure_filename(song.filename)
    filepath = os.path.join(upload_folder, filename)
    song.save(filepath)

    separator_2stems = Separator('spleeter:2stems')
    separator_4stems = Separator('spleeter:4stems')
    audio_loader = AudioAdapter.default()
    sample_rate = 44100

    waveform, _ = audio_loader.load(filepath, sample_rate=sample_rate)
    prediction = separator_2stems.separate(waveform)
    separator_2stems.save_to_file(prediction, filename, output_folder)
        
    return '200'