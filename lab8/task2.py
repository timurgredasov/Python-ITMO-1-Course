import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    exit()

left_hits = 0
right_hits = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    height, width = frame.shape[:2]
    center_x = width // 2
    
    cv2.line(frame, (center_x, 0), (center_x, height), (255, 255, 255), 2)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    
    red_pixels = cv2.countNonZero(mask)
    
    if red_pixels > 500:
        points = cv2.findNonZero(mask)
        
        if points is not None:
            center = np.mean(points, axis=0)[0]
            marker_x = int(center[0])
            marker_y = int(center[1])
            
            cv2.circle(frame, (marker_x, marker_y), 10, (0, 255, 0), 2)
            
            if marker_x < center_x:
                left_hits += 1
                cv2.putText(frame, "LEFT", (marker_x - 30, marker_y - 20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                right_hits += 1
                cv2.putText(frame, "RIGHT", (marker_x - 30, marker_y - 20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.putText(frame, f"Left hits: {left_hits}", (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, f"Right hits: {right_hits}", (50, 100), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow('Red Marker Tracker', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()