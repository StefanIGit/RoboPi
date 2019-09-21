import time
import RPi.GPIO as GPIO


button1Pin = 17

GPIO.setwarnings(False)

# RPi.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BCM)

# Pin 18 (GPIO 24) auf Input setzen
GPIO.setup(button1Pin, GPIO.IN)

while True: # Run forever
    if GPIO.input(button1Pin) == GPIO.HIGH:
        print("Button was pushed!")
        startTime = time.time()
        while GPIO.input(button1Pin) == GPIO.HIGH:
            time.sleep(0.1)

        if time.time() - startTime >2:
            print("Going down...")
            from subprocess import call
            call("sudo nohup shutdown -h now", shell=True)

GPIO.cleanup()

