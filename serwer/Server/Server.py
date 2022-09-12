import cv2 as cv2
from flask import Flask, request
import numpy as np
import base64
from Fire_Base import save_scanned_receipt, init_fb_app, get_data_between_two_dates
from process_image import read_from_image
from process_image import process_image

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def server_run():
    return "Hellow world!"


@app.route('/send_receipt', methods=["POST", "GET"])
def send_receipt():
    if request.method == "POST":
        image_string = base64.b64decode(request.form['image'])
        decoded_image_array = np.fromstring(image_string, np.uint8)
        image = cv2.imdecode(decoded_image_array, cv2.IMREAD_ANYCOLOR)

        processed_image = process_image(image)
        text_read = read_from_image(processed_image)

        '''
        print("---------------------------------")
        for i in text_read:
            print(i)
        print("---------------------------------")
        '''

        if text_read is not None:
            save_scanned_receipt(request.form["user_id"], text_read)
            return "Image has been read correctly."
        else:
            return "Receipt could not been read."


@app.route('/get_user_data_between_two_dates', methods=["POST"])
def get_user_data_between_dates():
    data = get_data_between_two_dates(request.form["user_id"], request.form["lower_date"], request.form["upper_date"])
    return data


if __name__ == '__main__':
    init_fb_app()
    app.run(debug=True, host="0.0.0.0")
