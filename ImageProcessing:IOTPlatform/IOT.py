import RPi.GPIO as GPIO
import urllib.request
Import time
Import sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)

def buzzer():
	GPIO.output(14,GPIO.HIGH)
	time.sleep(3)
	GPIO.output(14, GPIO.LOW)

def led();
	GPIO.output(18,GPIO.HIGH)
	time.sleep(3)
	GPIO.output(18, GPIO.LOW)

while True:
c = urllib.request.urlopen('https://drip--abhinavkolli1.repl.co/status').read().decode()
	print(c)
    if c == "on":
		led()
		buzzer()
		GPIO.cleanup()
		sys.exit()
	time.sleep(2)
}
