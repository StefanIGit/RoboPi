#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
        print(categorize(event))


'''
#import evdev
from evdev import InputDevice, categorize, ecodes
import robomove
import time

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)

def scaleSpeed ( x, in_min=0,  in_max=65535,  out_min=-100,  out_max=100):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min




#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
        #filters by event type
            if event.type == ecodes.EV_KEY:
                        print(event)
            elif event.type == ecodes.EV_ABS:
                        print(event)
                        print (event.code)
                        # code 1 y axis ( forwad/ backward)
                        if event.code == 1:
                            speed = scaleSpeed(event.value)
                            if speed > 0:
                                print ('Forward: %s'% speed)
                            elif speed < 0:
                                print ('Backward: %s'% speed)
                            else:
                                print ('For-/Backward: %s'% speed)

                            #robomove.enable_left_motor(speed)
                            #robomove.enable_right_motor(speed)
                        elif event.code == 0:
                            speed = scaleSpeed(event.value)
                            speed = scaleSpeed(event.value)
                            if speed > 0:
                                print ('Left: %s'% speed)
                            elif speed < 0:
                                print ('Right: %s'% speed)
                            else:
                                print ('Left / Right: %s'% speed)
'''