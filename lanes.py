import cv2
import numpy as np
import matplotlib.pyplot as plt

PATH = '' # to be filled
# thresholds for canny method
LOW_CANNY = 50
UPPPER_CANNY = 150

img = cv2.imread(PATH)

# image copy to make changes
img_cp = np.copy(img)

# grey-scale version of image
grey = cv2.cvtColor(img_cp, cv2.COLOR_RGB2GRAY)

# identifying the edges in image using cannny method
# by computing gradient, to identify change in pixels
# also applies GaussianBlur fn to reduce noise
cann = cv2.Canny(grey, LOW_CANNY, UPPPER_CANNY)




