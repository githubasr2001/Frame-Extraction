import os
import cv2
from collections import Counter

# Function to get the dominant color
def get_dominant_color(frame):
    img = cv2.resize(frame, (100, 100))
    pixels = img.reshape(-1, 3)

    color_count = Counter(map(tuple, pixels))
    dominant_color = color_count.most_common(1)[0][0]

    return dominant_color

# Analyze frames and categorize by dominant color
def analyze_frames():
    frame_folder = 'frames'
    result_dir = 'results/color_analysis'
    os.makedirs(result_dir, exist_ok=True)  # Create results directory if it doesn't exist

    color_categorized_frames = {}

    for filename in os.listdir(frame_folder):
        if filename.endswith('.jpg'):
            frame_path = os.path.join(frame_folder, filename)
            frame = cv2.imread(frame_path)

            # Get dominant color
            dominant_color = get_dominant_color(frame)

            if dominant_color not in color_categorized_frames:
                color_categorized_frames[dominant_color] = []
            color_categorized_frames[dominant_color].append(frame_path)

    # Save results to a text file in the specific results folder
    with open(os.path.join(result_dir, 'color_analysis_results.txt'), 'w') as f:
        for color, frames in color_categorized_frames.items():
            f.write(f"Color (RGB): {color}, Number of Frames: {len(frames)}\n")

if __name__ == "__main__":
    analyze_frames()
