from flask import Flask, request
import cv2 as cv2
import numpy as np

app = Flask(__name__)
# git test changes 

@app.route('/', methods=["POST", "GET"])
def serwer_run():
    return "Hellow world!"


@app.route('/sendImage', methods = ["POST", "GET"])
def send_image():
    if request.method == "POST":
        img_file_str = request.files["image"].read()
        img_array = np.fromstring(img_file_str, np.uint8) #fromstring method is deprecated.
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #cv2.imwrite("img.png", img)

        return "done"
    else:
        return "Something is not yes"

if __name__ == '__main__':
    app.run(debug=True)
