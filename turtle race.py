from turtle import *
from random import *
from time import *

setup(1366,768)
bgcolor("yellow")
penup()
goto(-200,200)
pendown()
s=('Courier',24,'bold')
write("Welcome to Turtle Race",align="right",font=s)
penup()
goto(-140,100)

for i in range(15):
    write(i)
    right(90)
    penup()
    forward(10)
    pendown()
    forward(150)
    backward(160)
    left(90)
    penup()
    forward(20)
    pendown()
#sleep(10)
a=Turtle()
a.shape("turtle")
a.color("red")
a.penup()
a.goto(-180,100)
a.pendown()
b=Turtle()
#ontimer(b,1)
b.shape("turtle")
b.color("blue")
b.penup()
b.goto(-180,80)
b.pendown()
c=Turtle()
c.shape("turtle")
c.color("green")
c.penup()
c.goto(-180,60)
c.pendown()
count=0
c1=0
c2=0
for i in range(15):
    co=randint(1,50)
    count=count+co
    k=a.forward(co)
    do=randint(1,50)
    c1=c1+do
    l=b.forward(do)
    fo=randint(1,50)
    c2=c2+fo
    m=c.forward(fo)
    
#print(count)
#print(c1)
#print(c2)
if count>c1 and count>c2:
    penup()
    goto(-100,-200)
    pendown()
    color("red")
    s=('Courier',20,'bold')
    write(("Congrats,Red turtle wins the game "),font=s)
if c1>count and c1>c2:
    penup()
    goto(-100,-200)
    pendown()
    color("blue")
    s=('Courier',20,'bold')
    write("Congrats,Blue turtle wins the game",font=s)
if c2>count and c2>c1:
    penup()
    goto(-100,-200)
    color("green")
    s=('Courier',20,'bold')
    write("Congrats,Green turtle wins the game",font=s)
    
    pendown()
hideturtle()
exitonclick()
#for j in range(15):
    #k=randint(1,50)
    
    #print(k)
