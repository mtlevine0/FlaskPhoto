from flask import Flask, Blueprint, request, redirect, url_for
from werkzeug import secure_filename
import os

upload_api = Blueprint('upload_api', __name__)

ALLOWED_EXTENSIONS = set(['txt','gif','png','jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@upload_api.route('/upload', methods=['POST','PUT'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join("/home/ubuntu/workspace/static", filename))
        print(filename)

    return redirect("/static/" + filename, code=301)
