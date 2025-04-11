# ---------------------------------------------------------
# Mobile Camera to Desktop Webcam Viewer
# Implemented by Lokesh Adivishnu
# ---------------------------------------------------------

# Required Libraries
import cv2  # OpenCV for capturing and displaying video
import numpy as np  # (Optional here, but useful for future image processing)

# IP Camera Stream URL
# Replace this IP with your phone's IP shown in the IP camera app (like 'IP Webcam' on Android)
url = "http://192.168.137.124:8080/video"

# Start capturing video from the mobile camera stream
cp = cv2.VideoCapture(url)

# Error Handling
if not cp.isOpened():
        print("Error: Could not connect to the stream. Please check the URL and try again.")
        return

# Main Loop: Continuously read and display the video feed
while True:
    # Read a frame from the video stream
    camera, frame = cp.read()

    # Check if a frame was successfully received
    if frame is not None:
        # Display the current frame in a window titled "Frame"
        cv2.imshow("Frame", frame)

    # Listen for key presses (waits 1ms)
    # If 'q' is pressed, break the loop and quit
    if cv2.waitKey(1) == ord("q"):
        break

# Cleanup: Close all OpenCV windows
cv2.destroyAllWindows()
