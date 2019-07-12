import time
import serial

ser=serial.Serial("/dev/ttyUSB0",baudrate=115200, timeout=1)


port.write("AT\r".encode())
data = ser.readline().decode()
time.sleep(1)

port.write("AT+IPR=57600\r".encode())
data = ser.readline().decode()
time.sleep(1)

port.close()

print("OK close port")


ser=serial.Serial("/dev/ttyUSB0",baudrate=57600, timeout=1)

port.write("AT\r".encode())
data = ser.readline().decode()
time.sleep(1)

port.write("AT+IPR?\r".encode())
data = ser.readline().decode()
data = ser.readline().decode()
data = ser.readline().decode()
time.sleep(1)

print("looks good")
port.close()
