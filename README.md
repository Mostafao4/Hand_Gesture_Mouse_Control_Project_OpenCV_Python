# Hand Recog. V1

This program uses your webcam to track your hand movements and control the mouse cursor using OpenCV, MediaPipe, and PyAutoGUI.

---

## 1. Prerequisites

- **Python 3.10 or newer** ([Download here](https://www.python.org/downloads/))
- A working webcam

---

## 2. Installation

1. **(Optional) Create and activate a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

2. **Install dependencies:**
   ```
   python -m pip install opencv-python mediapipe pyautogui
   ```

---

## 3. Running the Program

1. Connect your webcam.
2. Run the script:
   ```
   python code_1.py
   ```
3. A window will open showing the webcam feed. Your hand movements will control the mouse cursor. Press `Esc` to exit.

---

## 4. How It Works

- The program captures video from your webcam.
- It uses MediaPipe to detect hand landmarks.
- The tip of your index finger (landmark 8) moves the mouse cursor.
- When your thumb tip (landmark 4) and index tip (landmark 8) are close (vertical distance < 40 pixels), it triggers a mouse click.

---

## 5. Customizing the Code

You can change the following attributes in `code_1.py` to modify the program's behavior:

### **Camera Source**
- Change the camera index (default is `0`):
  ```python
  camera = cv2.VideoCapture(0)
  # Change 0 to 1 or another number if you have multiple cameras
  ```

### **Click Sensitivity**
- The click is triggered when the vertical distance between thumb and index tip is less than 40 pixels:
  ```python
  if(dist < 40):
      pyautogui.click()
  ```
  - Increase `40` to make clicking less sensitive.
  - Decrease `40` to make clicking more sensitive.

### **Mouse Movement Speed**
- The mouse moves to the position of your index finger tip:
  ```python
  pyautogui.moveTo(mouse_x, mouse_y)
  ```
  - To smooth or slow down movement, consider using `pyautogui.moveTo(mouse_x, mouse_y, duration=0.1)`

### **Drawing Options**
- To change the color or size of the circles drawn on fingertips:
  ```python
  cv2.circle(image, (x, y), 10, (0, 255, 255))
  # 10 is the radius, (0,255,255) is the color (BGR)
  ```

### **Window Name**
- Change the display window name:
  ```python
  cv2.imshow("Hand movement video capture", image)
  # Change the string to your preferred window title
  ```

---

## 6. Troubleshooting

- **Import errors:** Ensure all dependencies are installed in your current environment.
- **Webcam not detected:** Try changing the camera index in `cv2.VideoCapture(0)`.
- **Mouse not moving:** Ensure your hand is visible and well-lit for the camera.

---

## 7. Credits
- Built with [OpenCV](https://opencv.org/), [MediaPipe](https://mediapipe.dev/), and [PyAutoGUI](https://pyautogui.readthedocs.io/)

