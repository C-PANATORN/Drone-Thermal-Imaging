# Drone-Thermal-Imaging
This repository is a continuation of my MCE314 Mechatronics Engineering Design class. The goal of this project is to develop a system to send thermal imaging data from a drone to a remote laptop.

Project Overview
Thermal imaging is accomplished using the Adafruit MLX90640 IR thermal camera connected via I2C to a Raspberry Pi attached to the drone. Data transfer is achieved by interfacing with the Raspberry Pi via VNC. All thermal processing is handled within the Raspberry Pi, with multithreading implemented to improve frame rate performance.
