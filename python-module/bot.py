from microbit import *

'''
Movement functions
'''
def drive(leftVelocity, rightVelocity):
    '''
    This function controls the robot's left and right motors, within the range -1023 to 1023.
    '''
    L = leftVelocity
    R = rightVelocity
    # Below controls the left wheel: forward, backward, stop at given speed
    if L > 0 and L <= 1023:
        FL.write_analog(abs(L))  # go forwards at speed given
        BL.write_analog(0)         # don't go backwards
    elif L < 0 and L >= -1023:
        FL.write_analog(0)         # don't go forwards
        BL.write_analog(abs(L))  # go backwards at speed given
    else:
        FL.write_analog(0)         # stop the left wheel
        BL.write_analog(0)
    # Below controls the right wheel: forward, backward, stop at given speed
    if R > 0 and R <= 1023:
        FR.write_analog(abs(R))  # go forwards at speed given
        BR.write_analog(0)         # don't go backwards
    elif R < 0 and R >= -1023:
        FR.write_analog(0)         # don't go forwards
        BR.write_analog(abs(R))  # go backwards at speed given
    else:
        FR.write_analog(0)         # stop the right wheel
        BR.write_analog(0)

def stop():
    '''
    This function turns off the motors.
    '''
    drive(0,0)

'''
Set up functions
'''
def config(leftForward=pin13, leftBackward=pin12, rightForward=pin15, rightBackward=pin14):
    '''
    This function assigns which micro:bit pin controls which motor direction.
    Use pinCheckLeft() and pinCheckRight() to physically check this before configuration.
    '''
    global FL, BL, FR, BR
    FL = leftForward
    BL = leftBackward
    FR = rightForward
    BR = rightBackward

def pinCheckLeft(A1A=pin13, A1B=pin12):
    '''
    This function is used to test the orientation of the left motor.
    By default, A1A on the motor driver is connected to pin13 of the microbit,
    and A1B on the motor driver is connected to pin12 of the microbit.
    '''
    on = 800
    off = 0
    # Check if A1A turns left motor forward
    display.show("F")
    A1A.write_analog(on)
    A1B.write_analog(off)
    sleep(2000)
    # Check if A1B turns left motor backward
    display.show("B")
    A1A.write_analog(off)
    A1B.write_analog(on)
    sleep(2000)
    # Turn motor off
    display.show(Image.NO)
    A1B.write_analog(off)

def pinCheckRight(B1A=pin15, B1B=pin14):
    '''
    This function is used to test the orientation of the right motor.
    By default, B1A on the motor driver is connected to pin15 of the microbit,
    and B1B on the motor driver is connected to pin14 of the microbit.
    '''
    on = 800
    off = 0
    # Check if B1A turns right motor forward
    display.show("F")
    B1A.write_analog(on)
    B1B.write_analog(off)
    sleep(2000)
    # Check if B1B turns right motor backward
    display.show("B")
    B1A.write_analog(off)
    B1B.write_analog(on)
    sleep(2000)
    # Turn motor off
    display.show(Image.NO)
    B1B.write_analog(off)
