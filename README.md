# Drone-Thermal-Imaging
This repository is a continuation of my MCE314 Mechatronics Engineering Design class. The goal of this project is to develop a system to send thermal imaging data from a drone to a remote laptop.

Project Overview
Thermal imaging is accomplished using the Adafruit MLX90640 IR thermal camera connected via I2C to a Raspberry Pi attached to the drone. Data transfer is achieved by interfacing with the Raspberry Pi via VNC. All thermal processing is handled within the Raspberry Pi, with multithreading implemented to improve frame rate performance.

# Drone Thermal Imaging Installation Guide

## Prerequisites
- **Raspberry Pi** (Model 3 or later recommended)
- **Adafruit MLX90640 IR Thermal Camera**
- **MicroSD card** (16GB or larger recommended) with Raspberry Pi OS installed
- **Power supply** for Raspberry Pi
- **VNC viewer** installed on a remote laptop

## Step 1: Set Up Raspberry Pi

### Install Raspberry Pi OS
- Download Raspberry Pi OS from the [official website](https://www.raspberrypi.org/downloads/).
- Flash the OS to the MicroSD card using [Raspberry Pi Imager](https://www.raspberrypi.org/software/).

### Initial Setup
- Insert the MicroSD card into the Raspberry Pi.
- Connect a monitor, keyboard, and mouse to the Raspberry Pi.
- Power on the Raspberry Pi and follow the on-screen instructions to complete the setup.

### Enable I2C
- Open the terminal and run:
  ```bash
  sudo raspi-config
- Navigate to Interfacing Options > I2C > Enable.
- Reboot the Raspberry Pi.

## Step 2: Install Dependencies
- Update the package list
  ```bash
  sudo apt update
- Install Python and Pip
  ```bash
  sudo apt install python3 python3-pip -y
- Install Required Libraries
   ```bash
  pip3 install numpy matplotlib adafruit-circuitpython-mlx90640
- Install additional packages for matplotlib animation
   ```bash
  sudo apt install python3-tk -y

## Step 3: Connect the MLX90640 to the Raspberry Pi
- Wire the MLX90640
    - Connect the MLX90640 to the Raspberry Pi's I2C pins:
        - MLX90640 VIN to Raspberry Pi 3.3V (Pin 1)
        - MLX90640 GND to Raspberry Pi GND (Pin 6)
        - MLX90640 SCL to Raspberry Pi SCL (Pin 5, GPIO 3)
        - MLX90640 SDA to Raspberry Pi SDA (Pin 3, GPIO 2)

## Step 4: Set Up VNC for Remote Access
Enable VNC on Raspberry Pi
- Open the terminal and run:
  ```bash
  sudo raspi-config
- Navigate to Interfacing Options > VNC > Enable.
- Reboot the Raspberry Pi.

## Step 5: Run the Thermal Imaging Code
Download the Code
- Clone or download the repository containing the thermal imaging code to your Raspberry Pi.
Run the Code
- Navigate to the directory containing the code.
- Run the script:
  ```bash
  python3 thermal4.py

## Viewing the Output
The thermal imaging data should now be displayed in a matplotlib window on the Raspberry Pi. You can view this output through VNC Viewer on your laptop.

## Troubleshooting
No Data from MLX90640
- Check the I2C connections.
- Ensure I2C is enabled in raspi-config.
- Run i2cdetect -y 1 to see if the MLX90640 is detected (should appear as 0x33).
VNC Connection Issues
- Ensure VNC is enabled and the Raspberry Pi is connected to the same network as your laptop.
- Check the IP address of the Raspberry Pi using
  ```bash
  hostname -I
