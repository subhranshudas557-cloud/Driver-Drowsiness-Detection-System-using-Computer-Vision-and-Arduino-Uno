# 🚗 Driver-Drowsiness-Detection-System-using-Computer-Vision-and-Arduino-Uno
Driver drowsiness detection system using computer vision and Arduino Uno to monitor driver alertness and trigger real-time alerts.

## 🚀 Overview

This project detects **driver drowsiness in real-time** using computer vision techniques and triggers alerts using an **Arduino Uno**.

The system continuously monitors the driver's eye state and sends a signal to Arduino when drowsiness is detected.

## 🎯 Objective

To improve road safety by detecting driver fatigue and providing **instant alerts** to prevent accidents.

## ⚙️ How It Works

1. Camera captures real-time video of the driver  
2. Python detects face and eyes using computer vision  
3. Eye state is analyzed (open / closed)  
4. If eyes remain closed for a threshold time:
   - Drowsiness is detected  
   - Signal is sent to Arduino  
5. Arduino triggers:
   - Buzzer  
   - LED alert  

## 🧠 Technologies Used

- Python !! Works only in version 3.10 or less 
- OpenCV (Computer Vision)  
- Dlib / Haar Cascades (Face & Eye Detection)  
- Arduino Uno  
- Serial Communication (Python ↔ Arduino)  

## 📁 Project Structure

Driver-Drowsiness-Detection/

│

├── drowsiness_detection.py # Python code

├── arduino_code.ino # Arduino code

├── README.md


## ▶️ How to Run

## 🔹 Step 1: Install dependencies

```bash
pip install opencv-python mediapipe pyserial numpy 
```
##🔹 Step 2: Upload Arduino Code
- Install Arduino IDE
- Open arduino_code.ino in Arduino IDE
- Select correct COM port
- Upload to Arduino Uno

## 🔹 Step 3: Run Python Script

```bash
python drowsiness_detection.py
```
## ⚠️ Important Notes
- Ensure webcam is connected
- Arduino must be connected via USB
- COM port in Python must match Arduino

## 🎥 Demo Video

👉 Watch the demo here:
[https://drive.google.com/file/d/11ugk-UoDEehzUtxeL-uh1IIqiCvIYFLf/view?usp=sharing]

## 💡 Features
- Real-time drowsiness detection
- Automatic alert system
- Integration with hardware (Arduino)
- Lightweight and fast
