import os
import cv2

# Load the pre-trained Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in a frame
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return len(faces) > 0  # Return True if faces are detected

# Analyze frames based on face detection
def analyze_frames():
    frame_folder = 'frames'
    result_dir = 'results/face_detection'
    os.makedirs(result_dir, exist_ok=True)  # Create results directory if it doesn't exist

    face_categorized_frames = {'with_faces': [], 'without_faces': []}

    for filename in os.listdir(frame_folder):
        if filename.endswith('.jpg'):
            frame_path = os.path.join(frame_folder, filename)
            frame = cv2.imread(frame_path)

            # Check for faces in the frame
            if detect_faces(frame):
                face_categorized_frames['with_faces'].append(frame_path)
            else:
                face_categorized_frames['without_faces'].append(frame_path)

    # Save results to a text file in the specific results folder
    with open(os.path.join(result_dir, 'face_detection_results.txt'), 'w') as f:
        for category, frames in face_categorized_frames.items():
            f.write(f"Category: {category}, Number of Frames: {len(frames)}\n")

if __name__ == "__main__":
    analyze_frames()
