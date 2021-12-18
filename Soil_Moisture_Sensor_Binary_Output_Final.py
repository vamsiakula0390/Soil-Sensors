import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

while True:
	if GPIO.input(channel):
		# if input is LOW
		print("No Water Detected")
	else:
		# if input is HIGH
		print("Water Detected")
	time.sleep(1)

GPIO.cleanup()