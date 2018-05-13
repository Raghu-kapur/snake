
#threading function
import time
from threading import Thread
from queue import *
from turtle import *
import turtle
import random


canvas=turtle.getscreen()
canvas.setup(500,500)
turtle.left(90)
turtle.fd(220)
turtle.clear()
turtle.bgcolor("brown")
turtle.write("WELCOME TO THE SNAKE GAME",move=False,align="center",font=("Arial",16,"bold"))


def sleeper(q):
  print(q.get())
  #boundry for the game
  boundry=Turtle()
  boundry.speed(10)
  boundry.goto(200,0)
  boundry.clear()
  boundry.left(90)
  boundry.forward(200)
  t1=boundry.position()
  boundry.left(90)
  boundry.forward(400)
  t2=boundry.position()
  boundry.left(90)
  boundry.forward(400)
  t3=boundry.position()
  boundry.left(90)
  boundry.forward(400)
  t4=boundry.position()
  boundry.left(90)
  boundry.forward(400)
  print(t1,t2,t3,t4)

  turtle1=Turtle()
  #making of fruit
  fruit=Turtle()
  fruit.shape("circle")
  fruit.color("red")
  fruit.resizemode("user")
  fruit.shapesize(0.4,0.4,0.4)
  fruit.speed(10)
  fruit.pencolor("white")
  fruit.goto(random.randint(-20,20)*10,random.randint(-20,20)*10)
  fruit.clear()
  print(fruit.position())
  i=1
  while i==1:
    print("snake: ")
    print(snake.position())
    print("\nFruit: ")
    print(fruit.position())
    time.sleep(0.1)
    if(snake.xcor()>=200 or snake.xcor()<=-200 or snake.ycor()>=200 or snake.ycor()<=-200):
      turtle1.write("YOU LOST",move=False,align="center",font=("Arial",16,"bold"))
      i=2
    elif  not q.empty():
      key_press = q.get()
      if key_press == "Up":
        print("Up\n")
        snake.clear()
        global last_pressed
        if last_pressed == 'Left':
          snake.rt(90)
          snake.fd(length)
        elif last_pressed == 'Right':
          snake.lt(90)
          snake.fd(length)
        elif last_pressed == 'Up':
          snake.fd(length)
        else:
          snake.rt(180)
          snake.fd(length)
        last_pressed = 'Up'
        #if snake.position()==fruit.position():
        #if snake.xcor() == fruit.xcor() and snake.ycor() == fruit.ycor():
        if snake.distance(0,0)==fruit.distance(0,0) and snake.heading()==fruit.heading():
          time.sleep(5)
          fruit.goto(random.randint(-19,19)*10,random.randint(-19,19)*10)
          print(fruit.position())
          fruit.clear()

      elif key_press == "Down":
        print("Down\n")
        snake.clear()
        global last_pressed
        if last_pressed == 'Left':
          snake.lt(90)
          snake.fd(length)
        elif last_pressed == 'Right':
          snake.rt(90)
          snake.fd(length)
        elif last_pressed == 'Up':
          snake.rt(180)
          snake.fd(length)
        else:
          snake.fd(length)
        last_pressed = 'Down'
               #if snake.position()==fruit.position():
        #if snake.xcor() == fruit.xcor() and snake.ycor() == fruit.ycor():
        if snake.distance(0,0)==fruit.distance(0,0) and snake.heading()==fruit.heading():
          time.sleep(5)
          fruit.goto(random.randint(-19,19)*10,random.randint(-19,19)*10)
          print(fruit.position())
          fruit.clear()
      elif key_press == "Right":
        print("Right\n")
        snake.clear()
        global last_pressed
        if last_pressed == 'Left':
          snake.rt(180)
          snake.fd(length)
        elif last_pressed == 'Right':
          snake.fd(length)
        elif last_pressed == 'Up':
          snake.rt(90)
          snake.fd(length)
        else:
          snake.lt(90)
          snake.fd(length)
        last_pressed = 'Right'
               #if snake.position()==fruit.position():
        #if snake.xcor() == fruit.xcor() and snake.ycor() == fruit.ycor():
        if snake.distance(0,0)==fruit.distance(0,0) and snake.heading()==fruit.heading():
          time.sleep(5)
          fruit.goto(random.randint(-19,19)*10,random.randint(-19,19)*10)
          print(fruit.position())
          fruit.clear()
      elif key_press == "Left":
        print("Left\n") 
        snake.clear()
        global last_pressed
        if last_pressed == 'Left':
          snake.fd(length)
        elif last_pressed == 'Right':
          snake.lt(180)
          snake.fd(length)
        elif last_pressed == 'Up':
          snake.lt(90)
          snake.fd(length)
        else:
          snake.rt(90)
          snake.fd(length)
        last_pressed = 'Left'
               #if snake.position()==fruit.position():
        #if snake.xcor() == fruit.xcor() and snake.ycor() == fruit.ycor():
        if snake.distance(0,0)==fruit.distance(0,0) and snake.heading()==fruit.heading():
          time.sleep(5)
          fruit.goto(random.randint(-19,19)*10,random.randint(-19,19)*10)
          print(fruit.position())
          fruit.clear()
          
      elif key_press=="Escape":
        quitsnake()
      else:
        snake.fd(length)
    else:
      snake.clear()
      snake.fd(length)
    
               


#creating the snake
wn = turtle.Screen()
snake=Turtle()
last_pressed = 'Up'
q=Queue()
length=10
def setup(col, x, y, w, s, shape):
  snake.up()
  snake.turtlesize(0.2)
  snake.color("red")
  snake.shape("circle")
  snake.lt(90)
  snake.down()
  t = Thread(target=sleeper, args=(q,))
  t.start()
  wn.onkey(move_up, "Up")
  wn.onkey(move_left, "Left")
  wn.onkey(move_right, "Right")
  wn.onkey(move_back, "Down")
  wn.onkey(quitSnake, "Escape")

  wn.listen()
  wn.mainloop()


def move_up():
  q.put("Up")

  """
  
"""
def move_left():
  q.put("Left")
  """
  
    
"""


def move_right():
  q.put("Right")
  
  """
  
"""    
    
def move_back():
  q.put("Down")
  """
  
"""    
def quitSnake():
  wn.bye()
setup("blue",-200,200,2,2,"turtle")  


 
      
