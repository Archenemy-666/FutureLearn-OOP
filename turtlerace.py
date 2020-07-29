from turtle import Turtle
from random import randint
sid = Turtle()
sai = Turtle()
arc = Turtle()
anu = Turtle()

sid.color('blue')
sai.color('orange')
arc.color('red')
anu.color('green')


sid.penup()
sid.goto(-160,20 )
sid.pendown()
sai.penup()
sai.goto(-160,40)
sai.pendown()
arc.penup()
arc.goto(-160,60)
arc.pendown()
anu.penup()
anu.goto(-160,80)
anu.pendown()

sid.shape('turtle')
sai.shape('turtle')
arc.shape('turtle')
anu.shape('turtle')

sid.color('blue')
sai.color('orange')
arc.color('red')
anu.color('green')



for movement in range (100) :
    sid.forward(randint(1,5))
    sai.forward(randint(1,5))
    arc.forward(randint(1,5))
    anu.forward(randint(1,5))   

   

