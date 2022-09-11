from cv2 import cv2 #install opencv2
import  cvzone #install cvzone
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('#haarcascade_frontalface_default.xml') #copy and paste xml file & remove hashtag
overlay = cv2.imread('image.png', cv2.IMREAD_UNCHANGED) #image.png is any given image for overlay image
while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0, 255, 0),2)
        overlay_resize = cv2.resize(overlay, (int(w*1.5),int(w*1.5))) #overlay_resize for img.png
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75]) #frame overlay
    cv2.imshow('#name', frame)
    if cv2.waitKey(10) == ord('q'):
        break
