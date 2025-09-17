import cv2
from ultralytics import YOLO

video_path = r"C:\Users\Dharani Gunasekaran\Downloads\Temperorary\4K Road traffic video for object detection and tracking.mp4"

model = YOLO('yolov8n.pt')

count_line_y = 615
car_count = 0
counter_Ids = set()

video = cv2.VideoCapture(video_path)

if not video.isOpened():
    print("Error: could not open the video")

else:
    while True:
        ret, frame = video.read()

        if not ret:
            print("end of video stream")
            break

        results1 = model.predict(source = frame)
        
        for r in results1:
            anotted_frame = r.plot()

        cv2.line(anotted_frame, (0, count_line_y), (frame.shape[1], count_line_y), (0,255,0), 2)
        results2 = model.track(source = frame, persist = True, tracker = 'bytetrack.yaml')

        for r1 in results2:
            boxes = r1.boxes
        
        if boxes.id is not None:
            for box in boxes:
                track_id = int(box.id.item())
                x1, y1, x2, y2 = box.xyxy[0]
                centre_y = (y1+y2)/2

                if centre_y > count_line_y and track_id not in counter_Ids:
                    car_count += 1
                    counter_Ids.add(track_id)
        cv2.putText(anotted_frame, f'COUNT:{car_count}', (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)   

        
        
        cv2.imshow("Vehicle_Detection", anotted_frame)

        if cv2.waitKey(25) == ord('q'):
            break


video.release()
cv2.destroyAllWindows()

print('Video stream ended.')