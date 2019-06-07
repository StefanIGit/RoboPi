#!/bin/python
'''
Script to control a 3D printed RoboPi with a bluetooth gamepad (joystick , OUYA Controller)
there is a 2x H-bridge for the motors connected to some GPIOs

connect the gamepad...
see RoboPi\doc\connect_bluetooth_gamepad.txt

Install the linux evdev library (I think...)
    sudo pip install python-evdev

this mus run as root...... or pi if u know how let me know :)

'''


from evdev import InputDevice, categorize, ecodes
import robomove
import time
import os

#creates object 'gamepad' to store the data
#you can call it whatever you like
path = '/dev/input'
bFoundGamepad = False 
while not bFoundGamepad:
    eventList = os.listdir(path)
    print (eventList)
    for eventDevice in eventList:
        try:
            gamepad = InputDevice(path + '/' + eventDevice)
            if gamepad.name.startswith('OUYA'):
                bFoundGamepad = True
                break
            time.sleep(1)
        except:
            print('Controller not found sleeping for 2 Sec...')
            time.sleep(2)
        


#prints out device info at start
print(gamepad)



def scaleSpeed ( x, in_min=0,  in_max=65535,  out_min=-100,  out_max=100):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)




# not sure if needed but does not do harm too 
xSpeedScaled = 0
ySpeedScaled = 0
leftSpeed = 0
rightSpeed = 0

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():

    #filters by event type
    if event.type == ecodes.EV_KEY:
        # Stops the motos if O is pressed
        # and some experiments to press more than one a button
        if event.code == 304 and event.value == 1:
            bOpressed = True
            robomove.enable_left_motor(0)
            robomove.enable_right_motor(0)
            leftSpeed  = 0
            rightSpeed = 0
            xSpeedScaled  = 0
            ySpeedScaled = 0            
        else:
            bOpressed = False
        if event.code == 312 and event.value == 1:
            bDPadUpPressed = True
            
        else:
            bDPadUpPressed = False
        if bDPadUpPressed and bOpressed:
            starttime = time.time()
        

        #print(event.code, event.sec, event.timestamp)
    elif event.type == ecodes.EV_ABS:
                # try to use the left and right lower triggers(, I have no idea hown they are called)
                # so go forward and the O to reverse
                # did no work that well since the values are strange form the gamepad
                # code 1 y axis ( forwad/ backward)^
                
                '''
                print ('button/axis: %s : %s' %(event.code,event.value))
                if event.code == 2 and event.value >= 26000:
                    leftSpeed = scaleSpeed(event.value, in_min=26000,  in_max=65535, out_min=0,  out_max=100) *-1
                    print ('button/axis: %s : %s' %(event.code,event.value))
                if event.code == 5:
                    rightSpeed = scaleSpeed(event.value, out_min=0,  out_max=100) *-1
                    print ('button/axis: %s : %s' %(event.code,event.value))

                if 304 in gamepad.active_keys():
                    robomove.enable_left_motor(-leftSpeed)
                    robomove.enable_right_motor(-rightSpeed)
                else:
                    robomove.enable_left_motor(leftSpeed)
                    robomove.enable_right_motor(rightSpeed)

                
                
                continue
                '''
                # the left joystick...
                # based on http://home.kendra.com/mauser/Joystick.html
                #
                if event.code == 4:#1:
                    ySpeed = event.value
                    if 125 < ySpeed <130:
                        ySpeed = 128
                    elif ySpeed <13:
                        ySpeed = 0
                    ySpeedScaled = scaleSpeed(ySpeed,0,255,-100,100) *-1
                    #print (event.value, ySpeed, ySpeedScaled)
                if event.code == 3:#0:
                    xSpeed = event.value
                    if 125 < xSpeed <130:
                        xSpeed = 128
                    elif xSpeed >230:
                        xSpeed = 255
                    xSpeedScaled = scaleSpeed(xSpeed,0,255,-100,100) *-1
                    #print (event.value, xSpeed, xSpeedScaled)
                #continue
                RpL = (100-abs(xSpeedScaled)) * (ySpeedScaled/100) + ySpeedScaled
                RmL = (100-abs(ySpeedScaled)) * (xSpeedScaled/100) + xSpeedScaled
                leftSpeed =  (RpL + RmL)/2
                rightSpeed = (RpL - RmL)/2


                #print ('Leftmotor: %s / Rightmotor: %s'% (leftSpeed, rightSpeed))
                # speec limit ;)
                #leftSpeed = scaleSpeed(leftSpeed, in_min=-100, in_max=100, out_min=-50, out_max=50)
                #rightSpeed = scaleSpeed(rightSpeed, in_min=-100, in_max=100, out_min=-50, out_max=50)
                print ('\nySpeed: {0}\t-\txSpeed: {1}\nRpL: {2}\t-\tRmL: {3}\nleftSpeed: {4}\t-\trightSpeed: {5}\n'
                            .format(ySpeedScaled, xSpeedScaled, RpL, RmL, leftSpeed, rightSpeed))

                robomove.enable_left_motor(leftSpeed)
                robomove.enable_right_motor(rightSpeed)

                # not sure if needed here    
                #robomove.enable_left_motor(0)
                #robomove.enable_right_motor(0)
                leftSpeed  = 0
                rightSpeed = 0
                xSpeedScaled  = 0
                ySpeedScaled = 0
