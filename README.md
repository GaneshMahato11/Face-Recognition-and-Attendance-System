# Face Recognition & Attendance System

This project is a small real-time face recognition attendance tracker built in Python. It uses the webcam to detect faces, compare them against a set of known reference images, and append a matching person's name with a timestamp to `attendance.csv`.

## Overview

The application is implemented in `attendance.py` and is designed to:

- load known face images from the project folder
- encode those faces into numerical vectors
- capture live frames from the default webcam
- detect and encode faces from the live feed
- compare the live face against known faces
- log attendance when a recognized person is detected and not already recorded in the current runtime session
- display the webcam feed in a window until the user presses `q`

## Project Files

- `attendance.py` — main face recognition and attendance logic
- `run.bat` — Windows launcher script
- `attendance.csv` — attendance log file written by the script
- `gm.jpg` — one of the known reference images currently present in the project root
- `rtg.jpg` — expected reference image for one known person
- `AK.jpg` — expected reference image for one known person

## How It Works

The script does the following:

1. Loads three known face images from the project folder:
   - `gm.jpg`
   - `rtg.jpg`
   - `AK.jpg`
2. Encodes each image using `face_recognition.face_encodings()`.
3. Stores the encodings and labels in arrays:
   - `known_face_encodings`
   - `known_face_names`
4. Opens the webcam using `cv2.VideoCapture(0)`.
5. Reads each frame and resizes it to reduce processing load.
6. Detects faces in the frame and computes their encodings.
7. Compares each detected face against the known encodings using `face_recognition.face_distance()`.
8. Chooses the closest match using `np.argmin()`.
9. If the closest distance is below a threshold of `0.5`, it treats the person as recognized.
10. If the name is not already in `logged_users`, it writes:
    - person name
    - current timestamp
    to `attendance.csv`.
11. Displays the live webcam feed until the user presses `q`.

## Attendance Log Format

The script appends rows to `attendance.csv` in this format:

```csv
Name,YYYY-MM-DD HH:MM:SS
```

Example:

```csv
Ganesh Mahato,2026-09-14 00:10:06
Aishwaray Tiwary,2026-09-14 00:11:33
```

## Dependencies

This project relies on the following Python packages:

- `opencv-python`
- `face_recognition`
- `numpy`

The launcher in `run.bat` installs the required packages via `uv`:

```bat
uv run --with opencv-python --with face_recognition --with numpy python attendance.py
```

## Setup and Run

### Option 1: Use the batch file on Windows

Double-click `run.bat` in the project folder.

### Option 2: Run manually with `uv`

From the project directory, execute:

```bash
uv run --with opencv-python --with face_recognition --with numpy python attendance.py
```

## Important Notes

- The script uses the default webcam (`cv2.VideoCapture(0)`).
- It compares against the known names hard-coded in the file:
  - `Ganesh Mahato`
  - `Aishwaray Tiwary`
  - `ANURAG KUMAR`
- Duplicate names are prevented in the same runtime session by checking `logged_users`.
- The script appends to `attendance.csv` instead of replacing it, so repeated runs will add more attendance entries.
- In the current workspace, only `gm.jpg` is visibly present. The code also expects `rtg.jpg` and `AK.jpg` to exist in the same directory, so those files should be added before running the recognition pipeline if they are not already there.

## Runtime Behavior

When the script is running:

- a live video window opens
- recognized faces can be seen in the feed
- valid matches are logged to `attendance.csv`
- press `q` in the video window to close the program

## Current Project State

From the files in the workspace, the project appears to be a prototype or local test project with a live webcam attendance mechanism and a simple CSV-based attendance log. It does not include a full database, user management system, or a web interface.

## License

No specific license file is present in this project. The repository currently contains the source code and image assets without an explicit project license declaration.
