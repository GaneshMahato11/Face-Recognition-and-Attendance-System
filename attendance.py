import cv2
import face_recognition
import numpy as np
from datetime import datetime
import csv

# 1. Load sample image and encode
known_image = face_recognition.load_image_file("gm.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

known_image_1 = face_recognition.load_image_file("rtg.jpg")
known_encoding_1 = face_recognition.face_encodings(known_image_1)[0]

known_image_2 = face_recognition.load_image_file("AK.jpg")
known_encoding_2 = face_recognition.face_encodings(known_image_2)[0]

known_face_encodings = [known_encoding, known_encoding_1,known_encoding_2]
known_face_names = ["Ganesh Mahato", "Aishwaray Tiwary","ANURAG KUMAR"]
logged_users = set()

# 2. Start webcam feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # 3. Locate & Encode live face
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(distances)

        if distances[best_match_index] < 0.5:  # Tolerance threshold
            name = known_face_names[best_match_index]

            # 4. Log Attendance (prevent duplicate logs in same session)
            if name not in logged_users:
                logged_users.add(name)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open("attendance.csv", "a", newline="") as f:
                    csv.writer(f).writerow([name, timestamp])

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
