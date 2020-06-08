import cv2

#cap = cv2.VideoCapture('name.avi')
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()

    if ret==True:

        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        out.write(frame)

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame', gray)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()