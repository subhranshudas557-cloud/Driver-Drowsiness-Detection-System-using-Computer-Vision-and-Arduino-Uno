import cv2
import mediapipe as mp
import time
import serial

ser = serial.Serial('COM13', 9600)

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def eye_ratio(landmarks, eye):
    vertical = abs(landmarks[eye[1]].y - landmarks[eye[5]].y)
    horizontal = abs(landmarks[eye[0]].x - landmarks[eye[3]].x)
    return vertical / horizontal   # more accurate

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

THRESHOLD = 0.25   # better range
counter = 0        # frame counter
FRAME_LIMIT = 10   # instead of time delay

state = "A"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark

            left = eye_ratio(landmarks, LEFT_EYE)
            right = eye_ratio(landmarks, RIGHT_EYE)
            eye_val = (left + right) / 2

            cv2.putText(frame, f"Eye: {eye_val:.2f}", (30, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            #  Eye Closed
            if eye_val < THRESHOLD:
                counter += 1

                if counter > FRAME_LIMIT:
                    if state != "S":
                        ser.write(b'S')
                        state = "S"

                    cv2.putText(frame, "SLEEP DETECTED!", (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            #  Eye Open
            else:
                counter = 0

                if state != "A":
                    ser.write(b'A')
                    state = "A"

    else:
        cv2.putText(frame, "No Face", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()