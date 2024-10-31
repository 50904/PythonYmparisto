# A SIMPLE VEBCAM VIEWER
# ======================

# LIBRARIES AND MODULES
# ---------------------

# OpenCV library for imaging
import cv2

# APPLICATION SETTINGS
# --------------------

# Which camera to use for streaming 0 is 1st web camera
camIX = 1

# Define the name of Video Window
windowName = "Kamera " + str(camIX)


# Create a capture object for the video stream
capture = cv2.VideoCapture(camIX)
 
# MAIN LOOP FOR THE APP TO RUN
# ============================

# While getting the stream show video on a window 
while capture.isOpened():
    ret, frame = capture.read()
    
    # If no stream returned exit the loop
    if not ret:
        print("Can't receive frames. Exiting ...")
        break
 
    # Define a key press (q) to interrupt/quit the program 
    cv2.imshow(windowName, frame)
    if cv2.waitKey(1) == ord('q'):
        break
 
# Finally release capture object and close the window
capture.release()
cv2.destroyAllWindows()
