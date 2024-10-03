YouTube Video Frame Extraction & Analysis

This project extracts frames from YouTube videos and performs analysis on the extracted frames. Currently, the system supports **color analysis**, **face detection**, and **scene change detection**.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Frame Analyses](#frame-analyses)
- [Folder Structure](#folder-structure)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [Contributions](#contributions)

## Overview

The project automates the extraction of frames from a provided YouTube video URL. Once the frames are extracted, analyses such as color analysis, face detection, and scene change detection are performed on them. This project aims to categorize video content and provide insight into the structure of video frames.

## Features

- **Frame Extraction**: Extracts frames from YouTube videos (ignores ads).
- **Color Analysis**: Analyzes dominant colors in each frame.
- **Face Detection**: Detects faces in each frame using OpenCV’s Haar cascades.
- **Scene Change Detection**: Detects significant scene transitions in the video.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Youtube-Video-Frame-Extraction-Analysis.git
cd Youtube-Video-Frame-Extraction-Analysis
```

### 2. Set up a Virtual Environment

```bash
python3 -m venv yt_env
source yt_env/bin/activate   # For Linux/Mac
yt_env\Scripts\activate      # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract for OCR (optional, for text detection)

- Mac: `brew install tesseract`
- Ubuntu: `sudo apt install tesseract-ocr`
- Windows: [Download the Tesseract installer](https://github.com/tesseract-ocr/tesseract/wiki)

## Usage

### 1. Extract Frames from YouTube Video

Run the frame extraction script by providing a YouTube video link:

```bash
python youtube_frame_extractor.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Frames will be saved in the `frames/` directory.

### 2. Perform Frame Analysis

You can run different analysis scripts on the extracted frames:

- **Color Analysis**:

  ```bash
  python color_analysis.py
  ```

- **Face Detection**:

  ```bash
  python face_detection.py
  ```

- **Scene Change Detection**:

  ```bash
  python scene_change_detection.py
  ```

## Frame Analyses

### 1. **Color Analysis**

Detect dominant colors in each frame and store the results in `results/color_analysis/`.

### 2. **Face Detection**

Detect human faces in the frames and save annotated images with bounding boxes in `results/face_detection/`.

### 3. **Scene Change Detection**

Identifies and logs frames where a scene change occurs, and the results are stored in `results/scene_change/`.

## Folder Structure

```
Youtube-Video-Frame-Extraction-Analysis/
├── frames/                   # Extracted frames from the video
├── results/                  # Analysis results
│   ├── color_analysis/
│   ├── face_detection/
│   └── scene_change/
├── youtube_frame_extractor.py # Main script to extract frames
├── color_analysis.py          # Script for color analysis
├── face_detection.py          # Script for face detection
├── scene_change_detection.py  # Script for scene change detection
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Results

Each analysis stores results in a separate folder inside the `results/` directory. This keeps the outputs of different types of analysis organized.

## Future Improvements

- **Object Detection**: Add support for detecting objects using models like YOLOv3 or YOLOv4.
- **Text Detection (OCR)**: Implement text extraction from frames using Tesseract OCR.
- **Motion Detection**: Add the ability to detect motion across consecutive frames.
- **Video Summarization**: Integrate summarization techniques to highlight key moments in the video.

## Contributions

Feel free to submit pull requests for new features, bug fixes, or improvements. Any contributions are welcome!

