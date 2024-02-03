import turtle
import time
import random
import os

speed = 15
pause = 0.5

screen_x = 200
screen_y = 200
lives = 3

frame = turtle.Turtle()
frame.color('red')
frame.pensize(5)

def frames():
    frame.speed(10)
    frame.penup()
    frame.goto(screen_x + 50, screen_y + 20)
    frame.pendown()
    frame.seth(270)
    for i in range(4):
        frame.forward(screen_x * 3 - 100)
        frame.right(90)
    frame.hideturtle()

frames()

lives_label = turtle.Turtle()
lives_label.hideturtle()
lives_label.color('violet')
lives_label.penup()
lives_label.goto(-(screen_x + 45), (screen_y + 45))
lives_label.pendown()
lives_label.write('LIVES:', font=('Arial', 10, 'bold'))

total_lives = turtle.Turtle()
total_lives.hideturtle()
total_lives.color('red')
total_lives.penup()
total_lives.goto(-(screen_x + 45), screen_y + 25)
total_lives.pendown()
total_lives.write(str(lives), font=('Arial', 10, 'normal'))

label_score = turtle.Turtle()
label_score.hideturtle()
label_score.color('violet')
label_score.penup()
label_score.goto(screen_x, screen_y + 45)
label_score.pendown()
label_score.write('SCORES:', font=('Arial', 10, 'bold'))

total_score = turtle.Turtle()
total_score.hideturtle()
total_score.color('red')
total_score.penup()
total_score.goto(screen_x, screen_y + 25)
total_score.pendown()
total_score.write('0', font=('Arial', 10, 'normal'))

player_1 = turtle.Turtle()
points = 0

def scores():
    global points
    points += 1
    total_score.clear()
    total_score.write(str(points), font=('Arial', 10, 'normal'))

def jump():
    player_2.hideturtle()
    player_2.goto(random.randint(-screen_x, screen_y), random.randint(-screen_x, screen_y))
    player_2.showturtle()


player_1.seth(0)

player_2 = turtle.Turtle()

player_1.penup()
player_1.goto(-100, 100)
player_1.color('green')
player_1.shape('square')


player_2.penup()
jump()
player_2.color('red')
player_2.shape('triangle')

game_over = False

def p_1_LEFT():
    global speed
    player_1.seth(180)
    
    

def p_1_RIGHT():
    global speed
    player_1.seth(0)
    
    

def p_1_UP():
    global speed
    player_1.seth(90)
    
    

def p_1_DOWN():
    global speed
    player_1.seth(270)
    
    

scr1 = player_1.getscreen()
scr1.listen()

scr1.onkey(p_1_LEFT, 'a')
scr1.onkey(p_1_RIGHT, 'd')
scr1.onkey(p_1_UP, 'w')
scr1.onkey(p_1_DOWN, 's')
plr_width = 2

while lives > 0 and points < 11:
    if player_1.xcor() > screen_x + plr_width  or player_1.ycor() > screen_y + plr_width:
        player_1.hideturtle()
        player_1.goto(0,0)
        player_1.write('GAME OVER', font=('Arial', 15, "normal"))
        break
    
    player_1.forward(speed)

    if player_1.distance(player_2.xcor(), player_2.ycor()) < 30:
        player_1.shapesize(plr_width)
        plr_width += 1
        jump()
        scores()
        speed += 10

    time.sleep(pause)
turtle.exitonclick()










# project for students by Anton Vasko