import os
import cv2
import numpy as np
from flask import Flask, render_template, Response, request
from werkzeug.utils import secure_filename
from ultralytics import YOLO

app = Flask(__name__)

YOLOV8_MODEL_PATH = 'output_of_Fire_and_smoke/kaggle/working/runs/detect/train2/weights/best.pt'

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}
video_path = None


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


model = YOLO(YOLOV8_MODEL_PATH)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    global video_path
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)
        file.save(filepath)
        video_path = filepath
        return render_template('index.html')

    return 'Invalid file type', 400


def generate_frames():
    global video_path
    if video_path is None:
        return None
    cap = cv2.VideoCapture(video_path)

    alpha = 0.4
    while True:
        success, frame = cap.read()
        if not success:
            break

        result = model(frame, verbose=False, conf=0.35)[0]

        bboxes = np.array(result.boxes.xyxy.cpu(), dtype="int")
        classes = np.array(result.boxes.cls.cpu(), dtype="int")
        confidence = np.array(result.boxes.conf.cpu(), dtype="float")

        for cls, bbox, conf in zip(classes, bboxes, confidence):
            (x1, y1, x2, y2) = bbox
            object_name = model.names[cls]
            if object_name == 'fire':

                color = (19, 127, 240)
            else:
                color = (145, 137, 132)

            cropped_image = frame[int(y1):int(y2), int(x1):int(x2)]
            white_layer = np.ones(cropped_image.shape, dtype=np.uint8) * 255
            cropped_image = cv2.addWeighted(cropped_image, 1 - alpha, white_layer, alpha, 0)
            frame[int(y1):int(y2), int(x1):int(x2)] = cropped_image
            cv2.rectangle(frame, (x1, y1 -30), (x1 + 200, y1), color, -1)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            cv2.putText(frame, f"{object_name.capitalize()}: {conf * 100:.2f}%", (x1, y1 - 5), cv2.FONT_HERSHEY_DUPLEX,
                        0.8, (255, 255, 255), 1)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)

    app.run(host='0.0.0.0', port=5000, debug=True)
