#import evdev
from evdev import InputDevice, categorize, ecodes
import robomove
import time

#creates object 'gamepad' to store the data
#you can call it whatever you like
while True:
    try:
        gamepad = InputDevice('/dev/input/event0')
        break
    except:
        print('Controller not found sleeping for 2 Sec...')
        time.sleep(2)
        


#prints out device info at start
print(gamepad)

def scaleSpeed ( x, in_min=0,  in_max=65535,  out_min=-100,  out_max=100):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min




xSpeed = 0
ySpeed = 0
leftSpeed = 0
rightSpeed = 0
#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():

    #filters by event type
    if event.type == ecodes.EV_KEY:
        if event.code == 304 and event.value == 1:
            bOpressed = True
            robomove.enable_left_motor(0)
            robomove.enable_right_motor(0)
            leftSpeed  = 0
            rightSpeed = 0
            xSpeed  = 0
            ySpeed = 0            
        else:
            bOpressed = False
        if event.code == 312 and event.value == 1:
            bDPadUpPressed = True
            
        else:
            bDPadUpPressed = False
        if bDPadUpPressed and bOpressed:
            starttime = time.epoch()
        

        #print(event.code, event.sec, event.timestamp)
        print(event)
    elif event.type == ecodes.EV_ABS:
                #print(event)
                #print ('button/axis: %s : %s' %(event.code,event.value))
                # code 1 y axis ( forwad/ backward)^
                '''
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
                if event.code == 1:
                    ySpeed = event.value
                    ySpeed = scaleSpeed(ySpeed) *-1
                if event.code == 0:
                    xSpeed = event.value
                    xSpeed = scaleSpeed(xSpeed) #*-1
                
                RpL = (100-abs(xSpeed)) * (ySpeed/100) + ySpeed
                RmL = (100-abs(ySpeed)) * (xSpeed/100) + xSpeed
                leftSpeed =  (RpL + RmL)/2
                rightSpeed = (RpL - RmL)/2


                #print ('Leftmotor: %s / Rightmotor: %s'% (leftSpeed, rightSpeed))
                leftSpeed = scaleSpeed(leftSpeed, in_min=-100, in_max=100, out_min=-50, out_max=50)
                rightSpeed = scaleSpeed(rightSpeed, in_min=-100, in_max=100, out_min=-50, out_max=50)
                #print ('\nySpeed: {0}\t-\txSpeed: {1}\nRpL: {2}\t-\tRmL: {3}\nleftSpeed: {4}\t-\trightSpeed: {5}\n'
                #            .format(ySpeed, xSpeed, RpL, RmL, leftSpeed, rightSpeed))

                robomove.enable_left_motor(leftSpeed)
                robomove.enable_right_motor(rightSpeed)
                    
                #robomove.enable_left_motor(0)
                #robomove.enable_right_motor(0)
                leftSpeed  = 0
                rightSpeed = 0
                xSpeed  = 0
                ySpeed = 0
