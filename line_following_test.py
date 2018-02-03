import RPi.GPIO as GPIO
import time

#enA
#enB
in1=11
in2=12
in3=13
in4=15
enA=40
enB=38

LeftProximityPin = 19
CenterProximityPin = 21
RightProximityPin = 22


def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(in1,GPIO.OUT)
	GPIO.setup(in2,GPIO.OUT)	
	GPIO.setup(in3,GPIO.OUT)	
	GPIO.setup(in4,GPIO.OUT)
	GPIO.setup(enA,GPIO.OUT)	
	GPIO.setup(enB,GPIO.OUT)	
	#GPIO.output(LedPin,GPIO.LOW)
	GPIO.setup(LeftProximityPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(CenterProximityPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(RightProximityPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def motorControl():

	while True:
		left = GPIO.input(LeftProximityPin)
		center = GPIO.input(CenterProximityPin)
		right = GPIO.input(RightProximityPin)
		print("Left = %s, Center = %s, Right= %s" %(left,center,right))
		if left == 0 and center==1 and right==1:
			print("Turn Left")
			GPIO.output(enA,GPIO.HIGH)
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(enB,GPIO.LOW)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
		elif left == 1 and center==0 and right==1:
			print("Straight")
			GPIO.output(enA,GPIO.HIGH)
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(enB,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
		elif left == 1 and center==1 and right==0:
			print("Turn Right")
			GPIO.output(enA,GPIO.LOW)
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(enB,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
		else:
			print("STOP")
			GPIO.output(enA,GPIO.LOW)
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(enB,GPIO.LOW)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.LOW)
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
	GPIO.output(enA,GPIO.LOW)
	GPIO.output(enB,GPIO.LOW)
	GPIO.cleanup()

if __name__ == '__main__':
	setup()
	try:
		motorControl()
	except KeyboardInterrupt:
		destroy()
