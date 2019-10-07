# Self-Driving - Lane Detection: program to detect lanes in a video 

![afdfsdf](output.gif)

## Version 1.0:
* Added smoothness of the average line between frames, to make the average line much more stable

## Version 0.9:
* Added a average of all the lines, as a single line in the video

## Version 0.85:

* Increase the quality of lines predicted by dilating the frame after canny function, which increases the width of the foreground objects making it easier to capture lines

## Version 0.8:

* Improve lines detection, using improved parameters values for HoughLInesP

## Version 0.5:

### Every frame from the video:
* is turned into grey-scale version using cv2.cvtColor function
* Finds edges in the frame using the [Canny86] algorithm by computing gradient, to identify change in pixels
* Using region_wants function discards the non-important areas of the frame for lane detection
* cv2.HoughLinesP to detect different lines passing through points detected by canny method
* Draw these lines on blank image of frame's size
* Use cv2.addWeighted function, to combine the original frame and empty image with drawn lines
