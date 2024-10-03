from flask import Flask, render_template, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    youtube_url = request.form['youtube_url']
    
    # Call the YouTube frame extractor script
    subprocess.run(['python', 'youtube_frame_extractor.py', youtube_url])
    
    # Run analysis scripts
    subprocess.run(['python', 'color_analysis.py'])
    subprocess.run(['python', 'face_detection.py'])
    subprocess.run(['python', 'scene_change_detection.py'])
    
    # Prepare results
    results = {
        'color_analysis': get_file_content('results/color_analysis/color_analysis_results.txt'),
        'face_detection': get_file_content('results/face_detection/face_detection_results.txt'),
        'scene_change': get_file_content('results/scene_change/scene_change_results.txt')
    }
    
    return render_template('results.html', results=results)

def get_file_content(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return "Analysis results not available."

if __name__ == '__main__':
    app.run(debug=True)