import os
import string
import random
from io import BytesIO
from zipfile import ZIP_DEFLATED, ZipFile

def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def zipped_output_file(path):
    temp_file = BytesIO()
    with ZipFile(temp_file, 'w', ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(path):
            for file in files:
                zip_file.write(os.path.join(root, file))
    temp_file.seek(0)
    return temp_file