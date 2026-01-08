from simulator import robot, FORWARD, BACKWARD, STOP
import random


# TODO: Write your code here!

def draw_circle():
    "Makes the robot draw a circle. Input an integer to make the robot go a certain amount of circles. The robot will then go that amount of circles."
    amount = int(input ("How many circles would you like to draw?"))
    for i in range (amount*12):
        LEFT_SENSOR = robot.left_sonar()
        RIGHT_SENSOR = robot.right_sonar()
        if LEFT_SENSOR > 10 and RIGHT_SENSOR > 10:
            robot.motors(FORWARD, BACKWARD, .5)
            robot.motors(FORWARD, FORWARD, 1)
        else:
            print("Too close to wall, backing up")
            robot.motors(BACKWARD,BACKWARD,1)
            break
    start()

def draw_square():
    "Makes the robot draw a circle. Input an integer to make the robot go a certain amount of squares. The robot will then go that amount of squares."
    amount = int(input("How many squares would you like to draw?"))
    for i in range (amount*4):
        LEFT_SENSOR = robot.left_sonar()
        RIGHT_SENSOR = robot.right_sonar()
        if LEFT_SENSOR > 32 and RIGHT_SENSOR > 32:
            robot.motors(FORWARD, FORWARD, 5)
            robot.motors(FORWARD, BACKWARD, 1.525)
        else:
            print("Too close to wall, backing up")
            robot.motors(BACKWARD,BACKWARD,2)
            break
    start()

def question():
    answer = int(input("Would you like to: 1. Continue, 2. Stop and go back to menu, 3. Quit the robot entirely"))
    if answer == 1:
        go()
    elif answer ==2:
        start()
    elif answer ==3:
        quit
    else:question()
def go():
    "Makes the robot go and bounce off walls. When near a wall, it will turn and take a new sonar reading. It then goes forward till near the wall and repeats."
    robot.motors (FORWARD, BACKWARD, .5)
    for i in range (5):
        LEFT_SENSOR = robot.left_sonar()
        RIGHT_SENSOR = robot.right_sonar()
        if LEFT_SENSOR < RIGHT_SENSOR:
            robot.motors(FORWARD, FORWARD, (LEFT_SENSOR/6)-2)
            robot.motors(BACKWARD, FORWARD, random.uniform(1.5, 3))
        elif RIGHT_SENSOR < LEFT_SENSOR:
            robot.motors(FORWARD, FORWARD, (RIGHT_SENSOR/6)-2)
            robot.motors(FORWARD, BACKWARD, random.uniform(1.5, 3))
        else:
            robot.motors(BACKWARD, BACKWARD, .7)
            robot.motors(FORWARD, BACKWARD, .5)
    question()

            

def start():
    "Initial question of what you want the robot to do. You can answer with 1 for Circle, 2 for Square, 3 for going randomly, and 4 for quitting"
    action = int(input("Would you like to: 1. Draw Circle, 2. Draw Square, 3. Go Randomly, 4. Quit the robot entirely"))
    if action == 1:
        draw_circle()
    elif action == 2:
        draw_square()
    elif action == 3:
        go()
    elif action == 4:
        quit
    else:
        print("Please input a valid number")
        start()




start()


robot.exit
#6 cm per sec

# robot.motors(left, right, seconds)

# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator
