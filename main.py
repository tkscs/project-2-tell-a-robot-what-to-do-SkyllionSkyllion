from simulator import robot, FORWARD, BACKWARD, STOP



# TODO: Write your code here!

def draw_circle():
    "Makes the robot draw a circle. Input an integer to make the robot go a certain amount of circles. The robot will then go that amount of circles."
    amount = int(input ("How many circles would you like to draw?"))
    for i in range (amount*61):
        robot.motors(FORWARD, BACKWARD, .1)
        robot.motors(FORWARD, FORWARD, .2)
    start()

def draw_square():
    "Makes the robot draw a circle. Input an integer to make the robot go a certain amount of squares. The robot will then go that amount of squares."
    amount = int(input("How many squares would you like to draw?"))
    for i in range (amount*4):
        robot.motors(FORWARD, FORWARD, 5)
        robot.motors(FORWARD, BACKWARD, 1.525)
    start()


def go():
    "Makes the robot go and bounce off walls. When near a wall, it will turn and take a new sonar reading. It then goes forward till near the wall and repeats."
    robot.motors (FORWARD, BACKWARD, .1)
    for i in range (100):
        LEFT_SENSOR = robot.left_sonar()
        RIGHT_SENSOR = robot.right_sonar()
        if LEFT_SENSOR < RIGHT_SENSOR:
            robot.motors(FORWARD, FORWARD, (LEFT_SENSOR/6)-1.5)
            robot.motors(BACKWARD, FORWARD, 2)
        elif RIGHT_SENSOR < LEFT_SENSOR:
            robot.motors(FORWARD, FORWARD, (RIGHT_SENSOR/6)-1.5)
            robot.motors(FORWARD, BACKWARD, 2)

        else:
            robot.motors(BACKWARD, BACKWARD, .5)
            robot.motors(FORWARD, BACKWARD, .3)

            
def start():
    "Initial question of what you want the robot to do. You can answer with 1 for Circle, 2 for Square, and 3 for going randomly"
    action = int(input("Would you like to 1. Draw Circle, 2. Draw Square, 3. Go Randomly"))
    if action == 1:
        draw_circle()
    elif action == 2:
        draw_square()
    elif action == 3:
        go()
    else:
        print("Please input a valid number")
        start()

print(robot.left_sonar())
print(robot.right_sonar())

start()

print(robot.left_sonar())
print(robot.right_sonar())

draw_circle()
draw_square()
#6 cm per sec

# robot.motors(left, right, seconds)

# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator
while True:
    QUIT=input("Would you like to quit?")
    if QUIT == "Yes":
        robot.exit()