# users/picture_handler.py

import os
from PIL import Image  ##for picture
from flask import url_for, current_app


def add_profile_pic(pic_upload, username):
    filename = pic_upload.filename

    # "mypicture" + "." + "jpg"
    ext_type = filename.split('.')[-1]
    # username.jpg so all users will have their pictures
    storage_filename = str(username) + '.' + ext_type

    filepath = os.path.join(current_app.root_path, 'static\profile_pics', storage_filename)

    # make sure same size
    output_size = (200, 200)

    pic = Image.open(pic_upload)
    # squeeze it to pixel the size you want
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
