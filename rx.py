#!/usr/bin/python
import serial
import time

arduino=serial.Serial('COM3',baudrate=9600, timeout = 3.0)
cadena=''
 
while True:
      var = input("Introduzca  un Comando: ")
      arduino.write(var.encode())
      time.sleep(5)
      
