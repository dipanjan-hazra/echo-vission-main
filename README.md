# EchoVision - AI Powered Attendance Management System
# Live Demon - https://echo-vission-main.streamlit.app/

## Overview

EchoVision is an AI-powered attendance management system that automates student attendance using Facial Recognition and Voice Verification. The system enables teachers to manage subjects, enroll students, and record attendance through biometric identification instead of manual attendance marking.

The project combines Computer Vision, Machine Learning, Voice Recognition, Authentication, and Cloud Database technologies to create a smart attendance solution.

---

## Features

### Teacher Module

* Secure Teacher Registration and Login
* Subject Creation and Management
* Student Enrollment Management
* Attendance Monitoring
* Attendance Report Generation

### Student Module

* Student Registration
* Facial Biometric Enrollment
* Voice Biometric Enrollment
* Attendance History Tracking

### AI Features

* Face Recognition using Dlib Embeddings
* Speaker Verification using Resemblyzer
* SVM-based Student Identification
* Automated Attendance Logging

### Security Features

* Password Hashing using bcrypt
* Secure Authentication Workflow
* Cloud Database Storage using Supabase

---

## System Architecture

Teacher / Student
│
▼
Streamlit UI
│
▼
Application Logic
│
┌──────┴──────┐
▼             ▼
Face AI     Voice AI
(Dlib)    (Resemblyzer)
│
▼
Supabase
(PostgreSQL Database)

---

## Technology Stack

### Programming Language

* Python

### Frontend

* Streamlit

### Database

* Supabase
* PostgreSQL

### Machine Learning

* Scikit-Learn
* NumPy
* Pandas

### Computer Vision

* Dlib
* face_recognition_models

### Voice Recognition

* Resemblyzer
* Librosa

### Security

* bcrypt

### Version Control

* Git
* GitHub

---

## Machine Learning Workflow

### Face Recognition Pipeline

1. Capture Student Face
2. Detect Face using Dlib
3. Generate Face Embedding
4. Train SVM Classifier
5. Predict Student Identity
6. Verify Confidence Threshold
7. Mark Attendance

### Voice Recognition Pipeline

1. Record Student Voice
2. Audio Preprocessing
3. Generate Speaker Embedding
4. Compare Similarity Score
5. Verify Identity
6. Attendance Confirmation

---

## Project Structure

```bash
src/
│
├── screens/
│   ├── home_screen.py
│   ├── teacher_screen.py
│   └── student_screen.py
│
├── database/
│   └── db.py
│
├── face/
│   └── facepipeline.py
│
├── voice/
│   └── voicepipeline.py
│
├── components/
│   ├── dialogs/
│   ├── forms/
│   └── widgets/
│
└── app.py
```



## Future Improvements

* Face Liveness Detection
* Anti-Spoofing Mechanism
* Mobile Application Support
* Real-Time Analytics Dashboard
* Attendance Export to PDF/Excel
* Multi-Camera Attendance System
* JWT Authentication
* Cloud Deployment on AWS/GCP

---

## Learning Outcomes

This project helped in understanding:

* Machine Learning Pipelines
* Computer Vision
* Facial Recognition Systems
* Speaker Recognition
* Authentication Systems
* Cloud Databases
* Full Stack Development
* Deployment and Project Architecture

---

## Author

Dipanjan Hazra

Information Technology Undergraduate

GitHub: https://github.com/dipanjan-hazra
