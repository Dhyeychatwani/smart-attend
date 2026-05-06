# Installation Guide

## Installing dlib (Required for face_recognition)

`dlib` requires CMake and a C++ compiler. Follow the steps for your OS:

---

### Windows

1. Install [CMake](https://cmake.org/download/) and add it to PATH
2. Install Visual Studio Build Tools (C++ workload)
3. Then run:
```bash
pip install dlib
pip install face-recognition
```

Or use a prebuilt wheel (easier):
```bash
pip install https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl
```

---

### Ubuntu / Debian

```bash
sudo apt-get update
sudo apt-get install -y cmake build-essential libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev
pip install dlib face-recognition
```

---

### macOS

```bash
brew install cmake
pip install dlib face-recognition
```

---

## Troubleshooting

**"No module named 'face_recognition'"**
→ Make sure your virtual environment is activated.

**"Could not open webcam"**
→ Check that your camera is not being used by another app.

**"No face detected in photo"**
→ Use a clear, well-lit frontal face photo. Avoid sunglasses or heavy shadows.

**Low recognition accuracy**
→ Lower the `TOLERANCE` value in `mark_attendance.py` (e.g. 0.45) for stricter matching.
