import time
import serial

print("start")

try:
	ser=serial.Serial("/dev/ttyUSB0",baudrate=115200, timeout=1)
	print("OK! 115200 port open")
except:
	print ("baudrate is not 115200 !!!")

else:
	ser.write("AT\r".encode())
	data = ser.readline().decode()
	print(data)
	time.sleep(1)

	ser.write("AT+IPR=57600\r".encode())
	data = ser.readline().decode()
	print(data)
	time.sleep(1)

finally:
	ser.close()

	print("OK close port")

try:
	ser=serial.Serial("/dev/ttyUSB0",baudrate=57600, timeout=1)
	print("OK! 57600 port open")
except:
	print "baudrate is not 57600 !!!"

else:
	ser.write("AT\r".encode())
	data = ser.readline().decode()
	print(data)
	time.sleep(1)

	ser.write("AT+IPR?\r".encode())
	data = ser.readline().decode()
	print(data)
	data = ser.readline().decode()
	print(data)
	data = ser.readline().decode()
	print(data)
	time.sleep(1)

finally:
	print("looks good")
	ser.close()
