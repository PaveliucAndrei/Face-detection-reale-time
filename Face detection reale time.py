import cv2 as cv

# Create face detection and load cascade classifier
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open video
video_cap = cv.VideoCapture("vid.mp4") # 0 means open webcam

while True:
    # Get a frame from the webcam
    _, frame = video_cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Run frame detection
    faces = face_cascade.detectMultiScale(gray, 1.13, 7)
    for face in faces:
        # Extract face from frame
        x, y, w, h = face
        # Drow rectangle over video feed
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 100, 0), 2)

    # Show annotated frame
    cv.imshow("Face detection", frame)
    # Quit loop
    if cv.waitKey(1) == ord("q"): #or cv.getWindowProperty("Coin detection video",cv.WND_PROP_VISIBLE) == 0:
        break
# End while

# Close video feed
video_cap.release()
# Close all windows
cv.destroyAllWindows()
