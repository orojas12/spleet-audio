import os, shutil, string, random
from io import BytesIO
from zipfile import ZIP_DEFLATED, ZipFile

def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def zipped_output_file(path):
    temp_file = BytesIO()
    with ZipFile(temp_file, 'w', ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(path):
            for file in files:
                zip_file.write(os.path.join(root, file), file)
    temp_file.seek(0)
    return temp_file

def clean_folder(dir_path):
    for item in os.listdir(dir_path):
        path = os.path.join(dir_path, item)
        try:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        except OSError as e:
            print(f"Failed to delete item: {path}. {e}")

def get_prediction_data(prediction_path, prediction_id):
    """
        Return a list of dicts (one dict for each file) that contain: 
        song_id, filename, download_url
    """
    prediction_data = []
    for file in os.listdir(prediction_path):
        track = {}
        track['id'] = prediction_id
        track['filename'] = file
        prediction_data.append(track)

def get_file_names(dir_path):
    file_names = []
    for file in os.listdir(dir_path):
        file_names.append(file)
    return file_names