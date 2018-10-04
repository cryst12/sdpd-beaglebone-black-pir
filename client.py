import Adafruit_BBIO.GPIO as GPIO
import socket
         
GPIO.setup("P8_13", GPIO.OUT)
GPIO.setup("P8_19", GPIO.IN)

GPIO.add_event_detect("P8_19", GPIO.RISING)
    #your amazing code here
    #detect wherever:
str1="Initialising"

serverAddr = ('10.42.0.1', 6666)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(serverAddr)

while True:
    if GPIO.event_detected("P8_19"):
        if GPIO.input("P8_14"):
            str1="Motion Detected"
            GPIO.output("P8_13", GPIO.HIGH)
        else:
            str1="No Motion Detected"
            GPIO.output("P8_13", GPIO.LOW)
        client.send(str1)
        time.sleep(1)

client.close()
GPIO.cleanup()