from flask import Flask, send_from_directory
from api import upload, view
import os

app = Flask(__name__)

@app.route("/")
def main():
    return send_from_directory("static/", "index.html")

PORT = int(os.getenv('PORT', '8080'))

if __name__ == '__main__':
    
    app.register_blueprint(upload.upload_api)
    app.register_blueprint(view.view_api)
    app.run(debug=True, host="0.0.0.0", port=PORT)