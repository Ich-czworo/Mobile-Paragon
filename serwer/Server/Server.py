import cv2 as cv2
from flask import Flask, request
import numpy as np
import base64
from Fire_Base import get_data, save_scanned_receipt, init_fb_app, get_data_between_two_dates
from Utils import separate_articles
from process_image import process_image

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def server_run():
    return "Hellow world!"


@app.route('/send_receipt', methods=["POST", "GET"])
def send_receipt():
    if request.method == "POST":
        imageString = base64.b64decode(request.form['image'])
        nparr = np.fromstring(imageString, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR);
        text_read = process_image(img)

        if text_read is not None:
            articles = separate_articles(text_read)
            save_scanned_receipt(request.form["user_id"], articles)
        return "done"

    else:
        print("Somethings wrong")
        return "meh"


@app.route('/get_user_data', methods=["GET"])
def get_user_data():
    data = get_data(request.form["user_id"])
    return data


@app.route('/get_user_data_between_two_dates', methods=["GET"])
def get_user_data_between_dates():
    data = get_data_between_two_dates(request.form["user_id"], request.form["date_lower"], request.form["date_upper"])
    return data


if __name__ == '__main__':
    init_fb_app()
    app.run(debug=True, host="0.0.0.0")
