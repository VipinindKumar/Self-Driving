import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

PATH = 'test3.png'
PATHVID = 'VID3.mp4'
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

def coordinates(image, line):
	''' converts slope and intercept of a line
		into its coordinates having restricted
		y intercept '''
	
	m, c = line
	
	# return origin if no line was not found previously
	if [m,c] == [0,0]:
		return np.array([0,0,0,0])
	
	y1 = image.shape[0]
	# keeping y2 restricted to 1/2 of image length
	y2 = int(y1 * (1/2))
	x1 = int((y1 - c) / m)
	x2 = int((y2 - c) / m)
	
	return np.array([x1, y1, x2, y2])

def average_lines_parameter(image, lines):
	''' average the lines by averaging the slope and
		intercept for left and right lane and 
		returns their coordinates '''
	
	left_line = list()
	rigth_line = list()
	
	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line.flatten()
			
			# get slope and intercept for the line
			m, c = np.polyfit((x1, x2), (y1, y2), deg=1)
			
			# add the appropriate line to its corresponding list
			if m > 0:
				left_line.append([m, c])
			else:
				rigth_line.append([m, c])
		
		# average the lines parameters
		if not left_line:
			left_avg_line = np.array([0, 0])
		else:
			left_avg_line = np.average(left_line, axis=0)
		if not rigth_line:
			rigth_avg_line = np.array([0, 0])
		else:
			rigth_avg_line = np.average(rigth_line, axis=0)
		
		# convert slopes, intercept to coordinates
		left_avg_line = coordinates(image, left_avg_line)
		rigth_avg_line = coordinates(image, rigth_avg_line)
		
		return np.array([left_avg_line, rigth_avg_line])

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

# image = cv2.imread(PATH)

video = cv2.VideoCapture(PATHVID)
ret, frame = video.read()

while(ret):
	# grey scale of the frame
	img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

	# identifying the edges in frame using cannny method
	# by computing gradient, to identify change in pixels
	# also applies GaussianBlur fn to reduce noise
	img = cv2.Canny(img, LOW_CANNY, UPPPER_CANNY)

	img = region_wants(img)

	# get the lines from different almost in line points
	lines = cv2.HoughLinesP(img, lines=np.array([]), rho=2, theta=np.pi/100, threshold=100, minLineLength=40, maxLineGap=5)

	# average the lines to single line for each side
	avg_lines = average_lines_parameter(frame, lines)

	# display the lines on the frame
	line_img = display_lines(frame, avg_lines)

	# combine the lines with the original frame
	img = cv2.addWeighted(frame, 0.8, line_img, 1, 1)

	cv2.imshow('lanes', mat=img)
	if cv2.waitKey(1) == ord('z'):
		break
		
	ret, frame = video.read()

# destroy all cv2 windows
video.release()
cv2.destroyAllWindows()