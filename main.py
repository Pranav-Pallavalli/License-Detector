import cv2

video = cv2.VideoCapture(0)
video.set(3,640)
video.set(4,480)
video.set(10,150)
cascade = cv2.CascadeClassifier("resources/haarcascade_russian_plate_number.xml")
count = 1
while True:
    bool,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    plate = cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in plate:
        area = w*h
        if area>500:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"Number Plate",(x,y-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
            img = frame[y:y+h,x:x+w]
            cv2.imshow("filtered",img)
    cv2.imshow("Result",frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite("Resources/Plate numbers/Platenum"+str(count)+".jpg",img)
        cv2.rectangle(frame,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(frame,"Scan Saved",(150,260),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("saved",frame)
        cv2.waitKey(1)
        count+=1
    if key == ord('q'):
         break
        