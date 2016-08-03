from flask import Flask, Blueprint, request, redirect, url_for, Response
from werkzeug import secure_filename
import os
import peewee as pw
import database as db
import uuid

upload_api = Blueprint('upload_api', __name__)

ALLOWED_EXTENSIONS = set(['txt','gif','png','jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    
def save_file(file, imageID):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        fileExtension = filename.split(".")[1]
        try:
            file.save(os.path.join("/home/ubuntu/workspace/static/upload", imageID + "." + fileExtension))
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
    imageID = str(uuid.uuid4())[:7]
    filename = save_file(file, imageID)
    fileExtension = filename.split(".")[1]

    if filename:
        db.Image.create(fileName=filename,imageID=imageID)
        response = redirect("/static/upload/" + imageID + "." + fileExtension, code=302)
    else:
        response = Response("Internal Error" , status=500)

    return response
