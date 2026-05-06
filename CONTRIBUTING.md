# Contributing to SmartAttend 🙌

Thanks for your interest! Here's how to get involved.

## Getting Started

1. Fork the repo and clone it locally
2. Create a virtual environment: `python -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run encoding: `python src/encode_faces.py`
5. Start the app: `python src/mark_attendance.py`

## Making Changes

```bash
git checkout -b feature/your-feature-name
# make changes
git commit -m "feat: your change description"
git push
# open a Pull Request
```

## Commit Message Guide

```
feat:     new feature
fix:      bug fix
docs:     documentation only
refactor: code improvement, no behavior change
test:     adding tests
```

## Good First Issues

- Add chart/graph to dashboard showing attendance trends
- Add email notification when attendance is marked
- Support for video file input (not just webcam)
- Add a student management page (enroll/remove via browser)
- Improve mobile layout of dashboard
- Add dark/light mode toggle to dashboard
- Write unit tests for `utils.py`

## Code Style

- Follow PEP 8 for Python
- Add docstrings to all functions
- Keep functions small and focused

We appreciate all contributions — big or small! 🎓
