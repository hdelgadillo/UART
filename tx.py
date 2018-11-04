import serial
arduino = serial.Serial('COM3', baudrate=9600, timeout=1.0)
while True:
    line = arduino.readline()
    print(line)