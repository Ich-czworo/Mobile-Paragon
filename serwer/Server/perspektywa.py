import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib import image
frame = image.imread("C:/Users/justy/Desktop/paragon/p2")
roi_corners=[[0.0 *frame.shape[1],1.0*frame.shape[0]], # left, down
             [0.38*frame.shape[1],0.0*frame.shape[0]], # left, up
             [0.62*frame.shape[1],0.0*frame.shape[0]], # right, up
             [1.0 *frame.shape[1],1.0*frame.shape[0]]] # right, down

show_roi=True
"""if show_roi:
    #change the format of points list and draw it on image
    src = np.float32(roi_corners)
    pts = np.array(src, np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(frame,[pts],True,(255,0,0),10) # Red in RGB; width: 10

plt.figure(figsize=(16,9))
plt.imshow(frame)
plt.show()"""

def unwarp(img, roi_corners):
    '''
    Unwarp image using 4 points and getPerspectiveTransform
    '''
    src = np.float32(roi_corners)

    warped_size=(img.shape[1], img.shape[0])
    offset=int(warped_size[0]/3.0)
    dst = np.float32([[offset               , warped_size[1] ], #
                      [offset               , 0              ],
                      [warped_size[0]-offset, 0              ],
                      [warped_size[0]-offset, warped_size[1]]])

    Mpersp = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, Mpersp, dsize=warped_size)
    return warped

unwarped = unwarp(frame,roi_corners)

# Let's see the result
plt.figure(figsize=(16,9))
plt.imshow(unwarped)
plt.show()