import cv2
import numpy as np

PATH = '' # to be filled
# thresholds for canny method
LOW_CANNY = 50
UPPPER_CANNY = 150

img = cv2.imread(PATH)

# image copy to make changes
img_cp = np.copy(img)
