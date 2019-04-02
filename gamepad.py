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

def scaleSpeed ( x, in_min=0,  in_max=65535,  out_min=-99,  out_max=99):
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
                            ySpeed = scaleSpeed(event.value) *-1
                            '''
                            if ySpeed < 0:
                                print ('Forward: %s'% ySpeed)
                            elif ySpeed > 0:
                                print ('Backward: %s'% ySpeed)
                            else:
                                print ('For-/Backward: %s'% ySpeed)
                            '''
                        #else:
                        #    ySpeed = 0
                        if event.code == 0:
                            xSpeed = scaleSpeed(event.value) *-1
                            '''if xSpeed < 0:
                                print ('Left: %s'% xSpeed)
                            elif xSpeed > 0:
                                print ('Right: %s'% xSpeed)
                            else:
                                print ('Left / Right: %s'% xSpeed)
                            '''
                        #else:
                        #    xSpeed = 0
                        
#                        leftSpeed = scaleSpeed(ySpeed + xSpeed, -200, 200, -100, 100)
#                        rightSpeed = scaleSpeed(ySpeed - xSpeed, -200, 200, -100, 100)
                        print ('ySpeed: %s / xSpeed: %s'% (ySpeed, xSpeed))
                        #if ySpeed > 0  and xSpeed == 0:
                        #    leftSpeed =  ySpeed - xSpeed
                        #    rightSpeed = ySpeed + xSpeed
                        #    print ('Leftmotor: %s / Rightmotor: %s'% (leftSpeed, rightSpeed))
                        #elif ySpeed < 0  and xSpeed == 0:
                        #    leftSpeed =  ySpeed + xSpeed
                        #    rightSpeed = ySpeed - xSpeed
                        #    print ('Leftmotor: %s / Rightmotor: %s'% (leftSpeed, rightSpeed))
                        if ySpeed >= 0:#xSpeed:
                        #if True:
                            leftSpeed =  ySpeed
                            rightSpeed = ySpeed
                            if xSpeed >= 0:
                                leftSpeed -= xSpeed
                            else:
                                rightSpeed -= abs(xSpeed)

                        else:
                            leftSpeed =  ySpeed
                            rightSpeed = ySpeed
                            if xSpeed >= 0:
                                leftSpeed += xSpeed
                            else:
                                rightSpeed += abs(xSpeed)                            
                        
                        if ySpeed ==0 and xSpeed != 0:
                            leftSpeed =  xSpeed * -1
                            rightSpeed = xSpeed
                        #if ySpeed ==0 and xSpeed < 0:
                        #    leftSpeed =  xSpeed 
                        #    rightSpeed = xSpeed * -1
                        #    print ('Leftmotor: %s / Rightmotor: %s'% (leftSpeed, rightSpeed))



                        #if ySpeed > 0  and xSpeed > 0:
                        #    leftSpeed =  ySpeed - xSpeed
                        #    rightSpeed = ySpeed
                        #    print ('Leftmotor: %s / Rightmotor: %s'% (leftSpeed, rightSpeed))
                        #elif ySpeed == 0  and xSpeed < 0:
                        #    leftSpeed =  ySpeed + xSpeed
                        #    rightSpeed = ySpeed - xSpeed
                        #    print ('Leftmotor: %s / Rightmotor: %s'% (leftSpeed, rightSpeed))
                        print ('Leftmotor: %s / Rightmotor: %s'% (leftSpeed, rightSpeed))
                        robomove.enable_left_motor(leftSpeed)
                        robomove.enable_right_motor(rightSpeed)
                            

