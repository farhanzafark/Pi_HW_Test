import RPi.GPIO as GPIO
import time

#enA
#enB
in1=11
in2=12
in3=19
in4=21
enA=40
enB=38

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(in1,GPIO.OUT)
	GPIO.setup(in2,GPIO.OUT)	
	GPIO.setup(in3,GPIO.OUT)	
	GPIO.setup(in4,GPIO.OUT)
	GPIO.setup(enA,GPIO.OUT)	
	GPIO.setup(enB,GPIO.OUT)	
	#GPIO.output(LedPin,GPIO.LOW)

def motorControl():

	while True:
		print("Running Motor")
		GPIO.output(enA,GPIO.HIGH)
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.HIGH)
		GPIO.output(in3,GPIO.LOW)
		GPIO.output(in4,GPIO.HIGH)
		time.sleep(0.15)
		"""if GPIO.input(ProximityPin) == GPIO.HIGH:
			print(GPIO.input(ProximityPin))
			GPIO.output(LedPin,GPIO.HIGH)
			time.sleep(0.25)
		else:
			print("Sensor = LOW")
			GPIO.output(LedPin,GPIO.LOW)
			time.sleep(0.25)"""

def destroy():
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		motorControl()
	except KeyboardInterrupt:
		destroy()
