# YOLOv8 Real-Time Object Detection

This project implements a cross-platform, real-time object detection system using [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) and OpenCV. It processes webcam input, detects common objects, and displays bounding boxes with class labels and confidence scores. The system is optimized for high FPS and can be evaluated on standard datasets for accuracy metrics.

----------

## Features

-   Real-time webcam video processing
    
-   Fast and accurate object detection using YOLOv8n (nano)
    
-   Bounding boxes, class labels, and confidence scores overlay
    
-   Live FPS counter
    
-   Cross-platform: works on Windows, Linux, macOS, x86_64, and ARM
    
-   Easily extensible for model evaluation and dataset testing
    

----------

## Requirements

-   Python 3.8+
    
-   [ultralytics](https://pypi.org/project/ultralytics/) (YOLOv8)
    
-   [opencv-python](https://pypi.org/project/opencv-python/)
    
-   [torch](https://pytorch.org/)
    
-   numpy
    

Install all dependencies with:

bash

`pip install -r requirements.txt` 

----------

## Installation

1.  **Clone this repository:**
    

-   bash
    
    `git clone https://github.com/manasjuneja/objectrecognition 
    cd yolov8-realtime-detection` 
    
    
2.   **Install dependencies:**
    

-   bash
    
    `pip install -r requirements.txt` 
    

----------

## Usage

## Real-Time Webcam Detection

3.   **Run The Main Script:**

-   bash

`python main.py` 

 Press `q` to exit the video window.
