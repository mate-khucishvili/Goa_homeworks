from turtle import *


#we want to paint a house

#step 1:   draw a square

speed(30)
width(7)
color("blue")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of squre



#drawing a door

forward(70)
color ("purple")
left(90)
forward(100)   #height of the door
right(90)
forward(60)
right(90)
forward(100)

#end drawing a door

#drawing a roof


penup()
goto(200, 200)
color ("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end drawing a roof

color("blue")
left(30)
forward(120)
penup()
left(90)
forward(10)
left(90)

pendown()
width(5)
forward(50)
right(90)
forward(45)
right(90)
forward(50)
right(90)
forward(45)
penup()

right(180)
forward(190)
left(90)

forward(10)
left(90)

forward(10)
pendown()
right(90)

forward(40)
left(90)

forward(45)
left(90)

forward(50)
left(90)

forward(45)
left(90)
forward(30)

#end drawing a house



exitonclick()