import cv2
import numpy as np
import mss
import time
import keyboard  # Import the keyboard library
#install the required libs before proceeding


# Set up the parameters
fps = 165
screen_width = 1920  # Adjust the screen width according to your monitor
screen_height = 1080  # Adjust the screen height according to your monitor
output_filename = "screen_recording.mp4"

# Create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec
out = cv2.VideoWriter(output_filename, fourcc, fps, (screen_width, screen_height))

# Use mss to capture the screen
with mss.mss() as sct:
    # Define the screen area to capture (entire screen in this case)
    monitor = {"top": 0, "left": 0, "width": screen_width, "height": screen_height}

    print("Recording started...")

    # Record the screen for a fixed duration
    start_time = time.time()
    try:
        while True:
            # Capture the screen
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

            # Write the frame to the video file
            out.write(frame)

            # Check for the 'Esc' key to stop recording
            if keyboard.is_pressed('esc'):  # Check if 'esc' key is pressed
                print("Escape key pressed, stopping recording.")
                break

            # Maintain the desired FPS
            elapsed_time = time.time() - start_time
            sleep_time = max(1.0 / fps - elapsed_time, 0)
            time.sleep(sleep_time)
            start_time = time.time()
    finally:
        # Release everything
        out.release()
        cv2.destroyAllWindows()

print(f"Recording saved as {output_filename}")
