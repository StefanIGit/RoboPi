import time
import RPi.GPIO as GPIO

# 13, 19, 26  33, 35, 37
# 16, 20, 21  36, 38, 40

motorLeftEnable = 37
#motorLeftInA = 35
#motorLeftInB = 33
motorLeftInA = 33
motorLeftInB = 35

motorRightEnable = 40 
motorRightInA = 36
motorRightInB = 38
#motorRightInA = 38
#motorRightInB = 36


GPIO.setwarnings(False)

# RPi.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BOARD)

# Pin 18 (GPIO 24) auf Input setzen
GPIO.setup(motorLeftEnable, GPIO.OUT)
speedLeft = GPIO.PWM(motorLeftEnable, 50)
GPIO.setup(motorLeftInA, GPIO.OUT)
GPIO.setup(motorLeftInB, GPIO.OUT)

GPIO.setup(motorRightEnable, GPIO.OUT)
speedRight = GPIO.PWM(motorRightEnable, 50)
GPIO.setup(motorRightInA, GPIO.OUT)
GPIO.setup(motorRightInB, GPIO.OUT)

# disable motors
def disable_motors():
    disable_left_motor()
    disable_right_motor()


def disable_left_motor():
    speedLeft.stop()
    GPIO.output(motorLeftInA, GPIO.LOW)
    GPIO.output(motorLeftInB, GPIO.LOW)


def disable_right_motor():
    speedRight.stop()
    GPIO.output(motorRightInA, GPIO.LOW)
    GPIO.output(motorRightInB, GPIO.LOW)


def enable_left_motor_forward(speed=30.0):
    speedLeft.start(speed)
    GPIO.output(motorLeftInA, GPIO.HIGH)
    GPIO.output(motorLeftInB, GPIO.LOW)


def enable_right_motor_forward(speed=30.0):
    speedRight.start(speed)
    GPIO.output(motorRightInA, GPIO.HIGH)
    GPIO.output(motorRightInB, GPIO.LOW)


def enable_left_motor_backward(speed=30.0):
    speedLeft.start(speed)
    #GPIO.output(motorLeftEnable, GPIO.HIGH)
    GPIO.output(motorLeftInA, GPIO.LOW)
    GPIO.output(motorLeftInB, GPIO.HIGH)


def enable_right_motor_backward(speed=30.0):
    speedRight.start(speed)
    #GPIO.output(motorRightEnable, GPIO.HIGH)
    GPIO.output(motorRightInA, GPIO.LOW)
    GPIO.output(motorRightInB, GPIO.HIGH)



def enable_left_motor(speed=30.0):
    '''
    speed = -100 - +100
    '''
    #print('left %s' %speed)
    if -20 < int(speed) < 20:
        speed = 0
    speedLeft.stop()
    GPIO.output(motorLeftInA, GPIO.LOW)
    GPIO.output(motorLeftInB, GPIO.LOW)
    if int(speed) >0:
        speedLeft.start(speed)
        GPIO.output(motorLeftInA, GPIO.LOW)
        GPIO.output(motorLeftInB, GPIO.HIGH)
    else:
        GPIO.output(motorLeftInA, GPIO.HIGH)
        GPIO.output(motorLeftInB, GPIO.LOW)
        speedLeft.start(-speed)


def enable_right_motor(speed=30.0):
    '''
    speed = -100 - +100
    '''
    #print('right %s' %speed)
    if -20 < int(speed) < 20:
        speed = 0
    speedRight.stop()
    GPIO.output(motorRightInA, GPIO.LOW)
    GPIO.output(motorRightInB, GPIO.LOW)
    if int(speed) >0:
        GPIO.output(motorRightInA, GPIO.LOW)
        GPIO.output(motorRightInB, GPIO.HIGH)
        speedRight.start(speed)
    else:
        GPIO.output(motorRightInA, GPIO.HIGH)
        GPIO.output(motorRightInB, GPIO.LOW)
        speedRight.start(-speed)











if __name__ == '__main__':
    disable_motors()
    enable_left_motor_forward()
    time.sleep(5)
    disable_motors()
    enable_left_motor_backward()
    time.sleep(5)
    disable_motors()

    enable_right_motor_forward()
    time.sleep(5)
    disable_motors()
    enable_right_motor_backward()
    time.sleep(5)
    disable_motors()
    
    
    enable_right_motor_forward()
    enable_left_motor_forward()
    time.sleep(5)
    disable_motors()
    
    
    #for in in range(5):
    #    GPIO.output(motorLeftEnable, GPIO.HIGH)












    GPIO.cleanup()

