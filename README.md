# Vehicle Detection and Counting 🚗

## Overview
This project is a real-time computer vision application that detects, tracks, and counts vehicles from a video stream. It uses a combination of deep learning models and traditional computer vision techniques to provide accurate and actionable data, which can be applied to traffic analysis, smart city initiatives, and autonomous systems.

The system is built to identify different types of vehicles (e.g., cars, trucks, buses) and provides a count of how many have passed a specified line or region of interest.

## Key Features
- **Object Detection:** Utilizes the state-of-the-art **YOLOv8** model for high-accuracy and efficient vehicle detection.
- **Multi-Object Tracking:** Implements **ByteTrack** to maintain the identity of each vehicle across frames, preventing double-counting and providing consistent tracking.
- **Real-time Processing:** Designed to process video frames in real-time, making it suitable for live monitoring applications.
- **Directional Counting:** Counts vehicles passing a predefined virtual line, allowing for valuable traffic flow analysis.
- **Customizable:** The model weights and video source can be easily swapped out to adapt to different use cases and datasets.

## Installation

### Prerequisites
* Python 3.8 or higher
* Git

### Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dharanigitac/Vehicle_detection.git
    ```

2.  **Install dependencies:**
    Before you can run the script, you need to install all the required libraries. Navigate to your project directory and run the following command:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the application, ensure all dependencies are installed and execute the main Python script from your terminal:

```bash
python RL_Counter_App.R1.py
