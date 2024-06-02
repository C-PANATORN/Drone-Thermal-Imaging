import time
import board
import busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import subprocess

# Function to get screen size on Linux
def get_screen_size():
    output = subprocess.check_output(['xrandr']).decode('utf-8').split()
    index = output.index('current')
    width, height = int(output[index+1]), int(output[index+3].replace(',', ''))
    return width, height

# Global variables
data_array = np.zeros((24, 32))
mlx = None
last_update_time = time.time()
frame_count = 0
fig = None

def initialize_sensor():
    global mlx
    i2c = busio.I2C(board.SCL, board.SDA)
    mlx = adafruit_mlx90640.MLX90640(i2c)
    mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ

def acquire_data():
    global data_array
    global mlx
    while True:
        frame = np.zeros((24*32,))
        mlx.getFrame(frame)
        data_array = np.reshape(frame, (24, 32))

def update_data():
    global data_array
    while True:
        yield data_array

def on_key(event):
    if event.key == 'escape':
        plt.close()
        print("Program terminated by user.")
    elif event.key == 'ctrl+c':
        plt.close()
        print("Program terminated by user.")
        import sys
        sys.exit()

def main():
    global fig
    initialize_sensor()

    # Get screen size
    screen_width, screen_height = get_screen_size()

    # Create threads
    data_thread = threading.Thread(target=acquire_data)

    # Start data acquisition thread
    data_thread.start()

    # Set up the plot
    fig = plt.figure(figsize=(screen_width/100, screen_height/100))  # Adjust size dynamically
    fig.canvas.mpl_connect('key_press_event', on_key)
    ax = fig.add_subplot(111)
    therm1 = ax.imshow(np.zeros((24, 32)), vmin=0, vmax=60, cmap='inferno', interpolation='bilinear')
    cbar = fig.colorbar(therm1)
    cbar.set_label('Temperature [C]', fontsize=14)
    plt.title('Thermal Image')

    # Text annotations for temperature values
    max_temp_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, color='white')
    min_temp_text = ax.text(0.02, 0.90, '', transform=ax.transAxes, color='white')
    avg_temp_text = ax.text(0.02, 0.85, '', transform=ax.transAxes, color='white')
    center_temp_text = ax.text(0.02, 0.80, '', transform=ax.transAxes, color='white')

    # Update function for animation
    def update(frame):
        global last_update_time
        global frame_count

        # Update the thermal image data
        therm1.set_data(np.fliplr(frame))
        therm1.set_clim(vmin=np.min(frame), vmax=np.max(frame))

        # Calculate temperature values
        max_temp = np.max(frame)
        min_temp = np.min(frame)
        avg_temp = np.mean(frame)
        center_temp = frame[12, 16]

        # Update text annotations
        max_temp_text.set_text(f'Max Temp: {max_temp:.2f} C')
        min_temp_text.set_text(f'Min Temp: {min_temp:.2f} C')
        avg_temp_text.set_text(f'Avg Temp: {avg_temp:.2f} C')
        center_temp_text.set_text(f'Center Temp: {center_temp:.2f} C')

        # Calculate FPS
        current_time = time.time()
        elapsed_time = current_time - last_update_time
        frame_count += 1
        if elapsed_time > 1.0:
            fps = frame_count / elapsed_time
            print(f"FPS: {fps:.2f}")
            last_update_time = current_time
            frame_count = 0

    ani = animation.FuncAnimation(fig, update, update_data, interval=1)

    plt.show()

    # Join data acquisition thread
    data_thread.join()

if __name__ == '__main__':
    main()