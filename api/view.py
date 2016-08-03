from flask import Flask, Blueprint, request, redirect, url_for, Response, send_from_directory
import peewee as pw
import database as db

view_api = Blueprint('view_api', __name__)

@view_api.route('/<imageID>', methods=['GET'])
def view(imageID):
    imageIDRaw = imageID.split(".")[0]
    print(imageIDRaw)
    query = db.Image.update(viewCount=db.Image.viewCount + 1).where(db.Image.imageID==imageIDRaw)
    print(db.Image.viewCount)
    query.execute()
    
    return send_from_directory("static/","upload/" + imageID)