import cv2 as cv2
from flask import Flask, request
import numpy as np
import base64

from Server.process_image import process_image

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def serwer_run():
    return "Hellow world!"


@app.route('/sendImage', methods = ["POST", "GET"])
def send_image():
    if request.method == "POST":
        img_file_str = request.files["image"].read()
        img_array = np.fromstring(img_file_str, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #cv2.imwrite("img.png", img)

        return "done"
    else:
        return "Image has not been send correctly"

@app.route('/send_string', methods = ["POST", "GET"])
def send_string():
    if request.method == "POST":
        imageString = base64.b64decode(request.form['image'])

        #  convert binary data to numpy array
        nparr = np.fromstring(imageString, np.uint8)

        #  let opencv decode image to correct format
        img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR);
        process_image(img)
        return "Whatever"

    else:
        print("Somethings wrong")
        return "meh"

if __name__ == '__main__':
    app.run(debug=True)
