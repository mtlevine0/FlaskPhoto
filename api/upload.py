from flask import Flask, Blueprint, request, redirect, url_for, Response
from werkzeug import secure_filename
import os

upload_api = Blueprint('upload_api', __name__)

ALLOWED_EXTENSIONS = set(['txt','gif','png','jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    
def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        try:
            file.save(os.path.join("/home/ubuntu/workspace/static/upload", filename))
        except IOError:
            # TODO: Handle IOError exception
            filename = False
    else:
        # TODO: handle multiple returns
        filename = False
    
    return filename

@upload_api.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = save_file(file)
    
    if filename:
        response = redirect("/static/upload/" + filename, code=302)
    else:
        response = Response("Internal Error" , status=500)

    return response
