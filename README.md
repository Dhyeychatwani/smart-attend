# 🎓 SmartAttend — AI-Powered Attendance System

An open-source, face-recognition-based attendance system built for classrooms and colleges. Uses Python, OpenCV, and the `face_recognition` library to automatically mark attendance by detecting and recognizing student faces in real time.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Made for GSSoC](https://img.shields.io/badge/Open%20Source-GSSoC%20Ready-orange)

---

## ✨ Features

- 📸 Real-time face detection via webcam
- 🧠 Face recognition using deep learning embeddings
- 📋 Auto-marks attendance with timestamp to CSV
- 🌐 Simple Flask web dashboard to view attendance logs
- 👤 Easy student enrollment (just add a photo)
- 📅 Filter attendance by date
- 📤 Export attendance report as CSV
- 🔒 No cloud required — runs fully offline

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Face Detection | OpenCV (Haar Cascade / HOG) |
| Face Recognition | `face_recognition` (dlib) |
| Web Dashboard | Flask + Jinja2 |
| Data Storage | CSV (lightweight, no DB needed) |
| Frontend | HTML, CSS, Vanilla JS |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/smart-attend.git
cd smart-attend
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

> ⚠️ `dlib` (required by `face_recognition`) may need CMake. See [docs/INSTALL_GUIDE.md](docs/INSTALL_GUIDE.md) for help.

### 4. Enroll students
Add one clear photo per student inside `data/known_faces/`:
```
data/known_faces/
├── Rahul_Sharma.jpg
├── Priya_Mehta.jpg
└── Arjun_Nair.jpg
```
Filename = student's name (used as display name).

### 5. Run the system
```bash
# Mark attendance via webcam
python src/mark_attendance.py

# Launch the web dashboard
python src/app.py
# Open http://localhost:5000
```

---

## 🗂️ Project Structure

```
smart-attend/
├── src/
│   ├── app.py                  # Flask web dashboard
│   ├── mark_attendance.py      # Webcam + recognition engine
│   ├── encode_faces.py         # Pre-compute face encodings
│   └── utils.py                # Helper functions
├── data/
│   ├── known_faces/            # Add student photos here
│   ├── encodings.pkl           # Auto-generated face encodings
│   └── attendance_logs/        # Auto-generated CSV logs
├── templates/
│   └── dashboard.html          # Web UI
├── static/
│   ├── css/style.css
│   └── js/main.js
├── docs/
│   └── INSTALL_GUIDE.md
├── models/                     # (optional) custom models
├── requirements.txt
├── CONTRIBUTING.md
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Good first issues:
- Add support for multiple cameras
- Add email/SMS notification on attendance marked
- Improve dashboard UI (charts, graphs)
- Add anti-spoofing (liveness detection)
- Support for video file input instead of webcam
- Add student management UI (enroll/remove via browser)

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgements

- [face_recognition](https://github.com/ageitgey/face_recognition) by Adam Geitgey
- [OpenCV](https://opencv.org/)
- Built with ❤️ for Indian classrooms
