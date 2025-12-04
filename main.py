from simulator import robot, FORWARD, BACKWARD, STOP



# TODO: Write your code here!

def draw_circle():
    for i in range (61):
        robot.motors(FORWARD, BACKWARD, .1)
        robot.motors(FORWARD, FORWARD, .2)

def draw_square():
    for i in range 

draw_circle()

print(robot.left_sonar())
print(robot.right_sonar())


# robot.motors(left, right, seconds)

# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator
while True:
    QUIT=input("Would you like to quit?")
    if QUIT == "Yes":
        robot.exit()