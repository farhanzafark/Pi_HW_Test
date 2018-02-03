import RPi.GPIO as GPIO
import time

LedPin = 11
ProximityPin = 15

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LedPin,GPIO.OUT)
	GPIO.setup(ProximityPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.output(LedPin,GPIO.LOW)

def proximityRead():

	while True:
		if GPIO.input(ProximityPin) == GPIO.HIGH:
			print("Sensor = LOW")
			GPIO.output(LedPin,GPIO.LOW)
			time.sleep(0.25)
		else:
			print("Sensor = HIGH")
			GPIO.output(LedPin,GPIO.HIGH)
			time.sleep(0.25)


def destroy():
	GPIO.output(LedPin,GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		proximityRead()
	except KeyboardInterrupt:
		destroy()
