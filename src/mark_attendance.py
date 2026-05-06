"""
mark_attendance.py
------------------
Main script: opens webcam, detects faces in real time,
recognizes students, and marks attendance.

Usage:
    python src/mark_attendance.py

Controls:
    Q  — Quit
"""

import os
import pickle
import cv2
import face_recognition
import numpy as np
from utils import mark_attendance

ENCODINGS_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'encodings.pkl')

# Tolerance: lower = stricter matching. 0.5 works well for most setups.
TOLERANCE     = 0.5
# Scale factor for faster processing (process at 1/4 resolution)
SCALE_FACTOR  = 0.25
# Minimum confidence display threshold
CONF_DISPLAY  = 0.45


def load_encodings():
    """Load pre-computed face encodings from disk."""
    if not os.path.exists(ENCODINGS_FILE):
        raise FileNotFoundError(
            "encodings.pkl not found. Run 'python src/encode_faces.py' first."
        )
    with open(ENCODINGS_FILE, 'rb') as f:
        data = pickle.load(f)
    print(f"✅ Loaded encodings for {len(data['names'])} student(s): {', '.join(data['names'])}")
    return data['encodings'], data['names']


def run_attendance():
    known_encodings, known_names = load_encodings()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Could not open webcam. Check camera connection.")
        return

    print("\n📸 SmartAttend is running. Press 'Q' to quit.\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read from webcam.")
            break

        # Resize for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=SCALE_FACTOR, fy=SCALE_FACTOR)
        rgb_small   = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces and compute encodings
        face_locations  = face_recognition.face_locations(rgb_small, model='hog')
        face_encodings  = face_recognition.face_encodings(rgb_small, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare against known encodings
            distances = face_recognition.face_distance(known_encodings, face_encoding)
            name      = "Unknown"
            color     = (0, 0, 220)   # Red for unknown

            if len(distances) > 0:
                best_idx  = int(np.argmin(distances))
                best_dist = distances[best_idx]
                confidence = 1 - best_dist

                if best_dist <= TOLERANCE:
                    name  = known_names[best_idx]
                    color = (0, 200, 80)   # Green for recognized

                    newly_marked = mark_attendance(name)
                    if newly_marked:
                        print(f"  ✅ Attendance marked: {name}  (confidence: {confidence:.0%})")
                    else:
                        print(f"  ℹ️  Already marked:   {name}")

            # Scale back up coordinates
            scale = int(1 / SCALE_FACTOR)
            top    *= scale
            right  *= scale
            bottom *= scale
            left   *= scale

            # Draw bounding box
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

            # Draw name label
            cv2.rectangle(frame, (left, bottom - 30), (right, bottom), color, cv2.FILLED)
            cv2.putText(
                frame, name,
                (left + 8, bottom - 8),
                cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1
            )

        # Display frame
        cv2.imshow('SmartAttend — Press Q to quit', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("\n👋 SmartAttend closed.")


if __name__ == '__main__':
    run_attendance()
