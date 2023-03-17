import rover, time

# Servo numbers
servo_FL = 9
servo_RL = 11
servo_FR = 15
servo_RR = 13
servo_MA = 0

#======================================================================
# Motion Functions

def goForward(speed):
    rover.setServo(servo_FL, 0)
    rover.setServo(servo_FR, 0)
    rover.setServo(servo_RL, 0)
    rover.setServo(servo_RR, 0)
    rover.forward(speed)

def goReverse(speed):
    rover.setServo(servo_FL, 0)
    rover.setServo(servo_FR, 0)
    rover.setServo(servo_RL, 0)
    rover.setServo(servo_RR, 0)
    rover.reverse(speed)

def goSide(angle, speed):
    rover.setServo(servo_FL, angle)
    rover.setServo(servo_FR, angle)
    rover.setServo(servo_RL, -angle)
    rover.setServo(servo_RR, -angle)
    rover.turnForward(speed, speed)

def defaultState():
    rover.setServo(servo_FL, 0)
    rover.setServo(servo_FR, 0)
    rover.setServo(servo_RL, 0)
    rover.setServo(servo_RR, 0)
    rover.brake()

# End of Motion Functions
#======================================================================

rover.init(0)

speed = 50

try:

    while True:

        defaultState()

        angles = [-90, -67.5, -45, -22.5, 0, 22.5, 45, 67.5, 90]
        distances = []

        for i in range(len(angles)):
            rover.setServo(0, angles[i])
            distances.append(rover.getDistance())
        
        for i in range(len(distances)):
            if(distances[i] == max(distances)):
                index = i
                break   

        if(index == 0):
            goReverse(speed)
            time.sleep(1)
            goSide(-45, speed)
            time.sleep(2)       
        if(index == 1):
            goSide(-45, speed)
            time.sleep(1.5)      
        if(index == 2):
            goSide(-45, speed)
            time.sleep(1)       
        if(index == 3):
            goSide(-45, speed)
            time.sleep(0.5)       
        if(index == 4):
            goForward(speed)
            time.sleep((distance-15)/speed)  
        if(index == 5):
            goSide(45, speed)
            time.sleep(0.5)
        if(index == 6):
            goSide(45, speed)
            time.sleep(1)
        if(index == 7):
            goSide(45, speed)
            time.sleep(1.5)
        if(index == 8):
            goReverse(speed)
            time.sleep(5/{})
            goSide(45, speed)
            time.sleep(2)
        else:
            continue

finally:
    rover.cleanup()
