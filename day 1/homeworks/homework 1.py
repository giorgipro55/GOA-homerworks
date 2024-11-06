from turtle import *


#we want to pation a house

# step 1:   draw a spuare
speed(74)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
 
# end of spuare

#drawing a door

forward(70)

color("yellow")
begin_fill()
left(90)
forward(70)
right(90)
forward(60)
right(90)
forward(70)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

begin_fill()
color("blue")
left(30)
forward(50)
left(90)
forward(70)
left(90)
forward(50)
left(90)
forward(70)
end_fill()

color("white")

goto(200, 200)

begin_fill()
color("blue")
right(630)
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()
exitonclick()