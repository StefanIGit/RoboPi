#!/usr/bin/python
__author__ = 'Artur Poznanski'


import time
import atexit
import pygame
import robomove2


robomove = robomove2.robomove2()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    robomove.disable_motors()

atexit.register(turnOffMotors)

pygame.init()
size = [50, 70]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

def scaleSpeed ( x, in_min=-1,  in_max=1,  out_min=-100,  out_max=100):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# not sure if needed but does not do harm too 
xSpeedScaled = 0
ySpeedScaled = 0
leftSpeed = 0
rightSpeed = 0


done = False
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
            done = True
            time.sleep(1.0)
            print joystick.get_numaxes()

    axis0 = joystick.get_axis( 4 )
    right_speed = scaleSpeed(axis0)
    print("Axis {} value: {:>6.3f} speed: {}".format(4, axis0, right_speed) )
    if right_speed < 0:
        robomove.enable_right_motor_forward(abs(right_speed))
        #robomove.enable_left_motor_forward(abs(right_speed))
    else: 
        robomove.enable_right_motor_backward(abs(right_speed))
        #robomove.enable_left_motor_backward(abs(right_speed))

    time.sleep(0.01)
    
    axis1 = joystick.get_axis( 1 )
    left_speed = scaleSpeed(axis1)
    print("Axis {} value: {:>6.3f} speed: {}".format(1, axis1, left_speed) )

    if left_speed < 0:
        robomove.enable_left_motor_forward(abs(left_speed))
        #robomove.enable_right_motor_backward(abs(left_speed))
    else: 
        robomove.enable_left_motor_backward(abs(left_speed))
        #robomove.enable_right_motor_forward(abs(left_speed))

    time.sleep(0.01)
