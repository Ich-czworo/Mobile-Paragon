import numpy as np
import cv2

# Assuming that variable points is a list containing 4 corners.
# for example points = [[0,0], [0,1], [1,1], [1,0]]
def image_perspective_correction(image, points):
    height, width = image.shape[:2]
    points_np = np.float32(points)

    warped_size = (height, width)
    offset = int(warped_size[0] / 3.0)
    dst = np.float32([[offset, warped_size[1]],
                      [offset, 0],
                      [warped_size[0] - offset, 0],
                      [warped_size[0] - offset, warped_size[1]]])

    Mpersp = cv2.getPerspectiveTransform(points_np, dst)
    warped = cv2.warpPerspective(image, Mpersp, dsize=warped_size)
    return warped

