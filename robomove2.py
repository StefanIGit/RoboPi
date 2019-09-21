import time
import RPi.GPIO as GPIO



class robomove2():

    def __init__(self): 
        # 13, 19, 26  33, 35, 37
        # 16, 20, 21  36, 38, 40

        self.motorLeftEnable = 37
        #self.motorLeftInA = 35
        #self.motorLeftInB = 33
        self.motorLeftInA = 33
        self.motorLeftInB = 35

        self.motorRightEnable = 40 
        self.motorRightInA = 36
        self.motorRightInB = 38
        #self.motorRightInA = 38
        #self.motorRightInB = 36


        GPIO.setwarnings(False)

        # RPi.GPIO Layout verwenden (wie Pin-Nummern)
        GPIO.setmode(GPIO.BOARD)

        # Pin 18 (GPIO 24) auf output setzen
        GPIO.setup(self.motorLeftEnable, GPIO.OUT)
        self.speedLeft = GPIO.PWM(self.motorLeftEnable, 50)
        GPIO.setup(self.motorLeftInA, GPIO.OUT)
        GPIO.setup(self.motorLeftInB, GPIO.OUT)

        GPIO.setup(self.motorRightEnable, GPIO.OUT)
        self.speedRight = GPIO.PWM(self.motorRightEnable, 50)
        GPIO.setup(self.motorRightInA, GPIO.OUT)
        GPIO.setup(self.motorRightInB, GPIO.OUT)

    # disable motors
    def disable_motors(self):
        self.disable_left_motor()
        self.disable_right_motor()


    def disable_left_motor(self):
        self.speedLeft.stop()
        GPIO.output(self.motorLeftInA, GPIO.LOW)
        GPIO.output(self.motorLeftInB, GPIO.LOW)


    def disable_right_motor(self):
        self.speedRight.stop()
        GPIO.output(self.motorRightInA, GPIO.LOW)
        GPIO.output(self.motorRightInB, GPIO.LOW)


    def enable_left_motor_forward(self, speed=30.0):
        self.speedLeft.start(speed)
        GPIO.output(self.motorLeftInA, GPIO.HIGH)
        GPIO.output(self.motorLeftInB, GPIO.LOW)


    def enable_right_motor_forward(self, speed=30.0):
        self.speedRight.start(speed)
        GPIO.output(self.motorRightInA, GPIO.HIGH)
        GPIO.output(self.motorRightInB, GPIO.LOW)


    def enable_left_motor_backward(self, speed=30.0):
        self.speedLeft.start(speed)
        #GPIO.output(self.motorLeftEnable, GPIO.HIGH)
        GPIO.output(self.motorLeftInA, GPIO.LOW)
        GPIO.output(self.motorLeftInB, GPIO.HIGH)


    def enable_right_motor_backward(self, speed=30.0):
        self.speedRight.start(speed)
        #GPIO.output(self.motorRightEnable, GPIO.HIGH)
        GPIO.output(self.motorRightInA, GPIO.LOW)
        GPIO.output(self.motorRightInB, GPIO.HIGH)



    def enable_left_motor(self, speed=30.0):
        '''
        speed = -100 - +100
        '''
        #print('left %s' %speed)
        if -20 < int(speed) < 20:
            speed = 0
        self.speedLeft.stop()
        GPIO.output(self.motorLeftInA, GPIO.LOW)
        GPIO.output(self.motorLeftInB, GPIO.LOW)
        if int(speed) >0:
            self.speedLeft.start(speed)
            GPIO.output(self.motorLeftInA, GPIO.LOW)
            GPIO.output(self.motorLeftInB, GPIO.HIGH)
        else:
            GPIO.output(self.motorLeftInA, GPIO.HIGH)
            GPIO.output(self.motorLeftInB, GPIO.LOW)
            self.speedLeft.start(-speed)


    def enable_right_motor(self, speed=30.0):
        '''
        speed = -100 - +100
        '''
        #print('right %s' %speed)
        if -20 < int(speed) < 20:
            speed = 0
        self.speedRight.stop()
        GPIO.output(self.motorRightInA, GPIO.LOW)
        GPIO.output(self.motorRightInB, GPIO.LOW)
        if int(speed) >0:
            GPIO.output(self.motorRightInA, GPIO.LOW)
            GPIO.output(self.motorRightInB, GPIO.HIGH)
            self.speedRight.start(speed)
        else:
            GPIO.output(self.motorRightInA, GPIO.HIGH)
            GPIO.output(self.motorRightInB, GPIO.LOW)
            self.speedRight.start(-speed)











if __name__ == '__main__':
    print "Start..."
    rm = robomove2()
    rm.disable_motors()
    rm.enable_left_motor_forward(50)
    time.sleep(5)
    print "next"
    rm.disable_motors()
    rm.enable_left_motor_backward()
    time.sleep(5)
    rm.disable_motors()
    print "next"
    rm.enable_right_motor_forward()
    time.sleep(5)
    rm.disable_motors()
    rm.enable_right_motor_backward()
    time.sleep(5)
    rm.disable_motors()
    print "next" 
    
    rm.enable_right_motor_forward()
    rm.enable_left_motor_forward()
    time.sleep(5)
    rm.disable_motors()
    print "End" 
    
    #for in in range(5):
    #    GPIO.output(self.motorLeftEnable, GPIO.HIGH)












    GPIO.cleanup()


