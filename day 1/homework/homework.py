from turtle import *

#squre

speed(11)
width(7)
color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(70)
left(90)
end_fill()
#door
color("gold")
begin_fill()
forward(120)
right(90)
forward(70)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

#roof
color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window
color("blue")
begin_fill()
penup()
goto(30, 180)
pendown()
left(120)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#second window
color("blue")
begin_fill()
right(90)
penup()
goto(140, 180)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#and thats it for the house

exitonclick()