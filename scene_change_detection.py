import cv2
import os

def scene_change_detection():
    frame_folder = 'frames'
    result_dir = 'results/scene_change'
    os.makedirs(result_dir, exist_ok=True)

    previous_frame = None
    scene_changes = []

    for filename in sorted(os.listdir(frame_folder)):
        if filename.endswith('.jpg'):
            frame_path = os.path.join(frame_folder, filename)
            frame = cv2.imread(frame_path)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if previous_frame is not None:
                diff = cv2.absdiff(previous_frame, gray_frame)
                non_zero_count = cv2.countNonZero(diff)

                # Threshold for significant scene change
                if non_zero_count > 10000:  # Adjust threshold as needed
                    scene_changes.append(frame_path)

            previous_frame = gray_frame

    with open(os.path.join(result_dir, 'scene_change_results.txt'), 'w') as f:
        for scene in scene_changes:
            f.write(f"Scene Change Detected: {scene}\n")

if __name__ == "__main__":
    scene_change_detection()
