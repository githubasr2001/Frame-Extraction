import os
import cv2
import time
import yt_dlp as youtube_dl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Function to set up Selenium and handle ads on YouTube
def setup_selenium_and_skip_ads(youtube_url):
    # Configure Selenium options (headless for background operation)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up Selenium WebDriver (automatically downloads the correct ChromeDriver)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open YouTube URL
    driver.get(youtube_url)
    
    # Wait for ads (you can adjust this wait time depending on the network speed)
    time.sleep(10)

    # Check if there is a "Skip Ad" button
    try:
        skip_button = driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button")
        if skip_button:
            skip_button.click()
            print("Ad skipped")
    except:
        print("No skippable ad found or already skipped")

    # Get the current URL after ads (if redirected)
    current_url = driver.current_url

    # Close the browser after handling the ad
    driver.quit()

    return current_url

# Function to download the video using yt-dlp
def download_youtube_video(youtube_url):
    ydl_opts = {
        'format': 'best',  # Get the best quality video
        'outtmpl': 'video.mp4',  # Name of the downloaded video
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

# Function to extract frames using OpenCV
def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save each frame as an image
        frame_path = os.path.join(output_folder, f"frame_{frame_count:05d}.jpg")
        cv2.imwrite(frame_path, frame)

        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames.")

# Main flow
def main(youtube_url):
    print("Processing YouTube video...")

    # Step 1: Handle YouTube ads and get the final video URL
    processed_url = setup_selenium_and_skip_ads(youtube_url)

    # Step 2: Download the video using yt-dlp
    print(f"Downloading video from: {processed_url}")
    download_youtube_video(processed_url)

    # Step 3: Extract frames from the downloaded video
    print("Extracting frames from video...")
    extract_frames('video.mp4', 'frames')

    print("Process completed.")

# Example usage
if __name__ == "__main__":
    youtube_video_url = "https://www.youtube.com/watch?v=7Y5q41D8_hs"  # Replace with your video URL
    main(youtube_video_url)
