#Dylan Grafius
#3/14/2018
#CSC-131
#lab 7
#The purpose of this lab is to familiarize the user with turtle
################################################################
################################################################
import turtle

def drawA(my_turtle):
    my_turtle.pencolor('green')

    my_turtle.penup()
    my_turtle.setposition(-100,0)
    my_turtle.pendown()
    my_turtle.setposition(0,250)
    my_turtle.setposition(100,0)

    my_turtle.penup()
    my_turtle.setposition(-64,90)
    my_turtle.pendown()
    my_turtle.setposition(64,90)


def drawX(my_turtle):
     #set turtle pen size
    my_turtle.pensize(5)

    #set turle pen color
    my_turtle.pencolor('green')

    #set turtle shape
    my_turtle.shape('turtle')

    my_turtle.penup()                   #pick up pen and place at point (-400,-300)
    my_turtle.setposition(-400,-300)
    my_turtle.pendown()                 #places pen down and begins to draw
    my_turtle.setposition(400,300)
    
    my_turtle.penup()
    my_turtle.setposition(400,-300)
    my_turtle.pendown()
    my_turtle.setposition(-400,300)

    my_turtle.penup()
    my_turtle.setposition(0,0)
    my_turtle.pendown()


def drawW(my_turtle):
     #set turtle pen size
    my_turtle.pensize(5)

    #set turle pen color
    my_turtle.pencolor('green')

    #set turtle shape
    my_turtle.shape('turtle')

    my_turtle.penup()
    my_turtle.setposition(-200,0)
    my_turtle.pendown()
    my_turtle.setposition(-100,-100)
    my_turtle.setposition(0,0)
    my_turtle.setposition(100,-100)
    my_turtle.setposition(200,0)


def moving_turtle(my_turtle):
    
    my_turtle.shape('turtle')
    my_turtle.turtlesize(8)
    my_turtle.pencolor('green')
    my_turtle.up()
    my_turtle.setposition(0,-300)
    my_turtle.down()

    my_turtle.speed('slowest')

    my_turtle.left(90)
    my_turtle.forward(100)

    my_turtle.turtlesize(6)
    my_turtle.forward(100)

    my_turtle.turtlesize(4)
    my_turtle.forward(100)

    my_turtle.turtlesize(3)
    my_turtle.forward(100)

    my_turtle.turtlesize(2)
    my_turtle.forward(100)

    my_turtle.turtlesize(1)
    my_turtle.forward(100)
    
    my_turtle.hideturtle()
    my_turtle.done()
    
   
def main():
    #set window size
    screen_width = 800
    screen_height = 600
    turtle.setup(screen_width,screen_height)

    #get reference to turtle window
    window = turtle.Screen()
    window.bgcolor('white')

    #set window title bar
    window.title('My First Turtle Graphing Program - Lab 7')

    #give turtle a name and print turtle
    my_turtle = turtle.getturtle()

    #create square (absolute positioning)
        #my_turtle.setposition(100,0)
        #my_turtle.setposition(100,100)
        #my_turtle.setposition(0,100)
        #my_turtle.setposition(0,0)

    #create a box (relative positioning)
        #my_turtle.forward(100)
        #my_turtle.left(90)
        #my_turtle.forward(100)
        #my_turtle.left(90)
        #my_turtle.forward(100)
        #my_turtle.left(90)
        #my_turtle.forward(100)

    drawA(my_turtle)

    drawX(my_turtle)

    drawW(my_turtle)

    moving_turtle(my_turtle)
    
    my_turtle.exitoneclick()
    
main()
