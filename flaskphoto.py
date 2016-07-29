from flask import Flask
from api import upload
import os

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def main():
    return "Hello World!"

PORT = int(os.getenv('PORT', '8080'))

if __name__ == '__main__':

    app.register_blueprint(upload.upload_api)
    app.run(debug=True, host="0.0.0.0", port=PORT)