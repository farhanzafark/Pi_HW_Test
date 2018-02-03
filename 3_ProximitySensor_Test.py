import RPi.GPIO as GPIO
import time

LeftProximityPin = 11
CenterProximityPin = 13
RightProximityPin = 15

def setup():
	GPIO.setmode(GPIO.BOARD)
	#GPIO.setup(LedPin,GPIO.OUT)
	GPIO.setup(LeftProximityPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(CenterProximityPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(RightProximityPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	#GPIO.output(LedPin,GPIO.LOW)

def proximityRead():

	while True:
		"""if GPIO.input(LeftProximityPin) == GPIO.HIGH:
			print("Sensor = LOW")
			GPIO.output(LedPin,GPIO.LOW)
			time.sleep(0.25)
		else:
			print("Sensor = HIGH")
			GPIO.output(LedPin,GPIO.HIGH)
			time.sleep(0.25)"""
		left = GPIO.input(LeftProximityPin)
		center = GPIO.input(CenterProximityPin)
		right = GPIO.input(RightProximityPin)
		print("Left = %s, Center = %s, Right= %s" %(left,center,right))
		time.sleep(0.25)


def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		proximityRead()
	except KeyboardInterrupt:
		destroy()
