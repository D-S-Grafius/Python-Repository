import turtle
#brings the turtle module into this program so we can use it
import random
#brings the random module into the program to allow the drunkard to take random steps 


print("This program simulates a random (Drunkard's) Walk")
walk_length = int(input("Enter number of seconds the drunkard will walk:"))
#takes input as the length of the walk 
walk_speed = int(input("Enter speed of the walk from 1 (slowest) to 10 (fastest):"))
#takes another input as the speed at which drunkard will walk
time = walk_length * walk_speed
#this gives me the time the drunkard will walk  

def start(heading, step_size):
    turtle.setheading(heading)
    turtle.forward(step_size)


def drunkardsWalk(step_size, steps):
    DIRECTIONS = (EAST, NORTH, WEST, SOUTH) = (0, 90, 180, 270)
    #sets each direction of the graph to its navigational titles
    for _ in range(steps):
        start(random.choice(DIRECTIONS), step_size)


def main():
    turtle.hideturtle()
    #this will make the turtle icon disappear when running
    turtle.speed(walk_speed)
    #get the input from the user for speed and apply it to the turtle
    turtle.pencolor('red')
    #customize the turtle to a specific color using ''
    drunkardsWalk(25, time)
    #this calls the function where the walking is taking place and returns the values for step size and steps

main()
    




