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
    song = request.files.get('song')
    if song is None:
        return '400'
    print('Saving file...')
    filename = secure_filename(song.filename)
    song.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    # audio_file = song.read()
    # separator = Separator('spleeter:2stems')
    # audio_loader = AudioAdapter.default()
    # sample_rate = 44100
    # waveform, _ = audio_loader.load(audio_file, sample_rate=sample_rate)
    # prediction = separator.separate(waveform)
    # print(prediction)

    return '200'