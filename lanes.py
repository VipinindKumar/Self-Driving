import cv2
import numpy as np
import matplotlib.pyplot as plt

PATH = 'test2.png'
# thresholds for canny method
LOW_CANNY = 50
UPPPER_CANNY = 150
# ponits for triangular area for lane selection
P1 = 200
P2 = 1100
P3 = 550, 250

def region_wants(image):
	'''	remove the unwanted region, from the image and
		returns part of image that needed'''
	
	h = image.shape[0]
	tri_area = np.array([[(P1,h), (P2,h), P3]])
	
	mask = np.zeros_like(image)
	# fill the tri_aea in the mask with white
	cv2.fillPoly(mask, tri_area, 255)
	
	# bitwise-and to delete the unwanted areas in image
	image = cv2.bitwise_and(image, mask)
	
	return image

def average_lines_parameter(image, lines):
	''' average the lines by averaging the slope and
		intercept for left and right lane '''

def display_lines(image, lines):
	''' takes an image and returns the image with
		lines provided drawn on it'''
	
	image_with_lines = np.zeros_like(image)
	
	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line.flatten()
			
			# draw the line on the image_with_lines
			cv2.line(image_with_lines, (x1, y1), (x2, y2), color=(0,255,0), thickness=10)
	
	return image_with_lines

image = cv2.imread(PATH)

# grey scale of the image
img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# identifying the edges in image using cannny method
# by computing gradient, to identify change in pixels
# also applies GaussianBlur fn to reduce noise
img = cv2.Canny(img, LOW_CANNY, UPPPER_CANNY)

img = region_wants(img)

# get the lines from different almost in line points
lines = cv2.HoughLinesP(img, lines=np.array([]), rho=2, theta=np.pi/100, threshold=100, minLineLength=40, maxLineGap=5)

# average the lines to single line for each side
avg_lines = average_lines_parameter(image, lines)

# display the lines on the image
line_img = display_lines(image, lines)

# combine the lines with the original image
img = cv2.addWeighted(image, 0.8, line_img, 1, 1)

cv2.imshow('lanes', mat=img)
cv2.waitKey(0)