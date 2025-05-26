# 🤖 Hand Gesture Controlled Motor System

This project allows you to control a motor using real-time hand gestures. It uses a webcam, OpenCV, CVZone (built on top of MediaPipe), and PySerial for communication with an Arduino board. 

## 📸 How it Works

- A webcam captures your hand gestures.
- CVZone + MediaPipe detects how many fingers are up.
- Based on finger count, a command is sent to the Arduino.
- Arduino drives the motor accordingly.

## 🖐️ Gesture Controls

| Fingers Up | Command   | Action   |
|------------|-----------|----------|
| 0          | `0`       | Stop     |
| 1          | `1`       | Forward  |
| 2          | `2`       | Right    |
| 3          | `3`       | Left     |
| 4          | `4`       | Backward |

## 🧠 Tech Stack

- Python
  - OpenCV
  - CVZone
  - PySerial
- Arduino
  - C++ / Arduino IDE

## 🧪 Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt

