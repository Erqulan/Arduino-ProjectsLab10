import serial
import tkinter as tk
from tkinter import messagebox

# Set the serial port (modify according to your Arduino port)
PORT = "COM5"  # Windows: "COMx"  |  Linux/Mac: "/dev/ttyUSBx" or "/dev/ttyACMx"
BAUD_RATE = 9600

try:
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=1)
except Exception as e:
    messagebox.showerror("Error", f"Failed to connect to Arduino: {e}")
    exit()


# Send "on" command
def turn_on():
    arduino.write(b"on\n")
    status_label.config(text="LED Status: ON", fg="green")


# Send "off" command
def turn_off():
    arduino.write(b"off\n")
    status_label.config(text="LED Status: OFF", fg="red")


# Create GUI interface
root = tk.Tk()
root.title("Arduino LED Control")
root.geometry("300x200")

status_label = tk.Label(root, text="LED Status: Unknown", font=("Arial", 14))
status_label.pack(pady=10)

btn_on = tk.Button(root, text="Turn ON LED", font=("Arial", 12), bg="green", fg="white", command=turn_on)
btn_on.pack(pady=5)

btn_off = tk.Button(root, text="Turn OFF LED", font=("Arial", 12), bg="red", fg="white", command=turn_off)
btn_off.pack(pady=5)

root.mainloop()
