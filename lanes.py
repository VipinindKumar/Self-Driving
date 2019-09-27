import cv2
import numpy as np
import matplotlib.pyplot as plt

PATH = 'test.jpg' # to be filled
# thresholds for canny method
LOW_CANNY = 50
UPPPER_CANNY = 150
# ponits for triangular area for lane selection
P1 = 200
P2 = 1100
P3 = 550, 250

def region_wants(img):
	'''	remove the unwanted region, from the img and
		returns part of image that needed'''
	
	h = img.shape[0]
	tri_area = np.array([[(P1,h), (P2,h), P3]])
	
	mask = np.zeros_like(img)
	# fill the tri_aea in the mask with white
	cv2.fillPoly(mask, tri_area, 255)
	
	# bitwise-and to delete the unwanted areas in image
	img = cv2.bitwise_and(img, mask)
	
	return mask

def display_lines(img, lines):
	''' takes an image and returns the image with
		lines provided drawn on it'''
	
	img_with_lines = np.zeros_like(img)
	
	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line.flatten()
			
			# draw the line on the img_with_lines
			cv2.line(img_with_lines, (x1, y1), (x2, y2), color=(0,255,0), thickness=10)
	
	return img_with_lines

image = cv2.imread(PATH)

# identifying the edges in image using cannny method
# by computing gradient, to identify change in pixels
# also applies GaussianBlur fn to reduce noise
img = cv2.Canny(image, LOW_CANNY, UPPPER_CANNY)
img = region_wants(img)

# get the lines from different almost in line points
lines = cv2.HoughLinesP(img, lines=np.array([]), rho=2, theta=np.pi/100, threshold=100, minLineLength=40, maxLineGap=5)

line_img = display_lines(img, lines)

# combine the lines with the original image
img = cv2.addWeighted(image, 0.8, line_img, 1, 1)

cv2.imshow(img)
cv2.waitKey(0)