
# 🔥 YOLOv8 Fire and Smoke Detection with Flask Integration

This repository showcases an advanced **real-time video streaming** web application that uses **YOLOv8** for detecting fire and smoke in live video feeds. The solution is built with **Flask**, enabling fast, responsive detection and visual feedback for safety monitoring purposes.

## Read this article for full understanding of the code:


## 🚀 Project Overview

In this project, we integrate **YOLOv8**, a state-of-the-art deep learning object detection model, with Flask to create a web interface that supports video uploads and real-time fire and smoke detection. The application processes video frames, detects fire and smoke with high accuracy, and highlights these regions using bounding boxes.

### Key Features:
- **Real-time video streaming**: The application continuously processes video frames and updates detection results live.
- **YOLOv8 model integration**: Detects fire and smoke with precise bounding boxes and confidence scores.
- **Flask-based web interface**: Simple and intuitive UI for video uploads and live results display.
- **Visual highlighting**: Detected fire and smoke are visually marked on the video using colored bounding boxes.

## 🛠️ Technologies Used
- **YOLOv8**: Cutting-edge object detection model.
- **Flask**: Lightweight web framework for serving video streams.
- **OpenCV**: Used for handling video frames and processing images.
- **NumPy**: For efficient array manipulation.
- **Werkzeug**: Secure file handling.

## 📄 Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+**
- **YOLOv8** (from the `ultralytics` library)
- **Flask**
- **OpenCV**
- **NumPy**

```bash
pip install ultralytics
pip install -U Flask
pip install opencv-python
```

## 🚀 Getting Started

Follow these steps to set up and run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/yolov8-fire-smoke-detection.git
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd yolov8-fire-smoke-detection
   ```

3. **Place the YOLOv8 model**:
   Make sure to download your trained YOLOv8 model and place the `.pt` file in the specified path within the code:
   ```python
   YOLOV8_MODEL_PATH = 'model/fire_and_smoke_model.pt'
   ```

4. **Run the Flask app**:
   Start the server by running the following command:
   ```bash
   python main.py
   ```

5. **Access the application**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

6. **Upload a video file**:
   Upload your video via the interface and see the real-time fire and smoke detection in action.

## 📂 Project Structure

```
yolov8-fire-smoke-detection/
│
├── uploads/                        # Uploaded video files
├── templates/                      # HTML files for the web interface
│   └── index.html                  # Main UI for uploading and displaying video
├── app.py                          # Main Flask application script
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🖼️ How It Works

1. **Video Upload**: Users can upload videos directly from the web interface.
2. **Real-time Detection**: The YOLOv8 model processes video frames in real-time, detecting instances of fire and smoke.
3. **Visual Feedback**: Bounding boxes and labels (e.g., "Fire") are rendered over the detected areas in the video, with confidence scores displayed.
4. **User Interface**: A live feed is shown in the browser, updating continuously as the model processes the video frames.

## 💡 Potential Use Cases
- **Surveillance systems**: Automatically detect fire hazards in real-time in industrial and public spaces.
- **Safety monitoring**: Integrate this solution with existing monitoring systems for fire and smoke detection in high-risk areas.

## 🚧 Challenges and Solutions
- **Real-time Performance**: Managing efficient real-time processing on lower-end systems can be a challenge. Leveraging frame resizing and model optimizations can help in such scenarios.
- **False Positives**: To minimize detection errors, confidence thresholds can be fine-tuned, and multiple video streams analyzed simultaneously to cross-verify results.

## 📈 Future Enhancements
- **Integration with live camera feeds**: Extend the application to work with live video streams from security cameras.
- **Alarm systems**: Automatically trigger alerts or notifications when fire or smoke is detected.
- **Mobile-friendly interface**: Optimize the app UI for mobile browsers for more flexibility.

## 👨‍💻 Contributing
We welcome contributions! Please fork the repository and submit a pull request to improve the project.

## 📧 Contact

For any questions, feel free to reach out or raise an issue in the GitHub repository.
