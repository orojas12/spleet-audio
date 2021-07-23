from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter

audio_loader = AudioAdapter.default()
sample_rate = 44100

def separate_2stems(src, dst, name):
    separator_2stems = Separator('spleeter:2stems')
    
    waveform, _ = audio_loader.load(src, sample_rate=sample_rate)
    prediction = separator_2stems.separate(waveform)
    separator_2stems.save_to_file(prediction, name, dst)

def separate_4stems(src, dst, name):
    separator_4stems = Separator('spleeter:4stems')

    waveform, _ = audio_loader.load(src, sample_rate=sample_rate)
    prediction = separator_4stems.separate(waveform)
    separator_4stems.save_to_file(prediction, name, dst)