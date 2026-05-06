"""
encode_faces.py
---------------
Pre-computes and saves face encodings for all known students.
Run this once after adding/updating photos in data/known_faces/.

Usage:
    python src/encode_faces.py
"""

import os
import pickle
import face_recognition
from PIL import Image
import numpy as np

KNOWN_FACES_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'known_faces')
ENCODINGS_FILE  = os.path.join(os.path.dirname(__file__), '..', 'data', 'encodings.pkl')

SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.webp')


def encode_all_faces():
    """Scan known_faces directory and compute encodings for each student."""
    known_encodings = []
    known_names     = []
    errors          = []

    image_files = [
        f for f in os.listdir(KNOWN_FACES_DIR)
        if f.lower().endswith(SUPPORTED_FORMATS)
    ]

    if not image_files:
        print("⚠️  No images found in data/known_faces/")
        print("    Add student photos named as 'StudentName.jpg' and run again.")
        return

    print(f"Found {len(image_files)} student photo(s). Encoding...\n")

    for filename in image_files:
        student_name = os.path.splitext(filename)[0].replace('_', ' ')
        filepath = os.path.join(KNOWN_FACES_DIR, filename)

        try:
            image = face_recognition.load_image_file(filepath)
            encodings = face_recognition.face_encodings(image)

            if not encodings:
                print(f"  ⚠️  No face detected in '{filename}' — skipping.")
                errors.append(filename)
                continue

            if len(encodings) > 1:
                print(f"  ⚠️  Multiple faces in '{filename}' — using first face.")

            known_encodings.append(encodings[0])
            known_names.append(student_name)
            print(f"  ✅ Encoded: {student_name}")

        except Exception as e:
            print(f"  ❌ Error processing '{filename}': {e}")
            errors.append(filename)

    # Save encodings
    data = {'encodings': known_encodings, 'names': known_names}
    with open(ENCODINGS_FILE, 'wb') as f:
        pickle.dump(data, f)

    print(f"\n✅ Done! Encoded {len(known_names)} student(s).")
    print(f"   Saved to: {ENCODINGS_FILE}")
    if errors:
        print(f"   ⚠️  Skipped {len(errors)} file(s): {', '.join(errors)}")


if __name__ == '__main__':
    encode_all_faces()
