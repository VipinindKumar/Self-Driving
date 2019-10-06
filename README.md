# Self-Driving - Lane Detection

## program to detect lanes in a video 

### Every frame from the video:
* is turned into grey-scale version using cv2.cvtColor function
* Finds edges in the frame using the [Canny86] algorithm by computing gradient, to identify change in pixels
* 
