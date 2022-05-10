from flask import Flask, request
import cv2 as cv2
import numpy as np
import dvc.api

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

"""
@app.route('/dvc_update', methods = ["POST", "GET"])
def dvc_update():
    if request.method == "POST":
        with dvc.api.open('Images.zip',repo='https://github.com/Ich-czworo/Mobile-Paragon/blob/MP-19-python-dvc/serwer/res/data/Images.zip.dvc') as images:
            a = type(images)
        return a
    else:
        return "xDDD"




path = "C:/Users/48728/Desktop/fr_with_picts/pictures_2021-03-14-211101"
valid_images = [".jpg",".gif",".png",".tga"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() in valid_images:
        new_row = {'img': os.path.join(path,f), 'img_name': os.path.basename(f),'path':path}
        df_img = df_img.append(new_row, ignore_index = True)     
"""

if __name__ == '__main__':
    app.run(debug=True)
