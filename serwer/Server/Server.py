from flask import Flask, request
import cv2 as cv2
import numpy as np
import dvc.api

app = Flask(__name__)

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
        return "Image has not been send correctly"

@app.route('/download_from_dvc', methods = ["POST", "GET"])
def download_from_dvc():
    if request.method == "POST":
        with dvc.api.open('\serwer\res\data\Images.zip.dvc', repo='https://https://github.com/Ich-czworo/Mobile-Paragon/tree/dvc') as fd:
            for i in fd:
                print(type(i))
        return "Files has been downloaded successfully"

    else:
        return "Wrong request method."

if __name__ == '__main__':
    app.run(debug=True)
