from roboflow import Roboflow
import cv2


#Specify your Roboflow API Key
rf = Roboflow(api_key="YOUR ROBOFLOW API KEY")
#Specify your Roboflow project name
project = rf.workspace().project("project-name")
#Specify your ROboflow project version
model = project.version(1).model

#Specify your video source, usually if you have only a webcam your source is 0 so cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    result = model.predict(frame, confidence=20, overlap=30).json()        
   
    for prediction in result['predictions']:
        x, y, width, height = int(prediction['x']), int(prediction['y']), int(prediction['width']), int(prediction['height'])
        label = prediction['class']
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Show screen with your predictions
    cv2.imshow("Roboflow realtime detection", frame)
    
    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Free webcam
cap.release()
cv2.destroyAllWindows()





