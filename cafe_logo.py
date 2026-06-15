from turtle import *
import turtleBeads 

turtleBeads.noTrace()
hideturtle()
pendown()

# draw bottom circle of the wifi part
turtleBeads.teleport(0, -175)
pensize(8)
pencolor("#00a1e7")
begin_fill()
turtleBeads.drawCircle(30)
fillcolor("#ffc80e")
end_fill()

# Draw arc
def draw_arc(radius, heading):
    setheading(heading)
    circle(radius, 130)

# The lines
def lines(head):
    setheading(head)
    forward(35)

# first one
turtleBeads.teleport(76, -115)
begin_fill()
lines(230)
draw_arc(60, 115)
lines(146)
draw_arc(-90, -291)
fillcolor("#ffc80e")
end_fill()

# second one
turtleBeads.teleport(122, -55)
begin_fill()
lines(228)
draw_arc(120, 117)
lines(148)

#liquid 
pencolor("#ffc80e")
fillcolor("#ffc80e")
def liquid(num, direction):
    setheading(direction)
    for i in range(num):
        circle(30, 30)
        circle(-30, 30)

liquid(3, 25)
liquid(2, 0)
liquid(2, 335)
print(pos())
liquid(3, 310)
end_fill()

turtleBeads.teleport(122, -55)
pencolor("#00a1e7")
draw_arc(150, 118)

# third one
turtleBeads.teleport(145, -20)
draw_arc(180, 119)
turtleBeads.teleport(168, 5)
draw_arc(210, 120)
    
lines(330)
turtleBeads.teleport(145, -20)
lines(46)

#drawing straw
turtleBeads.teleport(44.07,-4.87)
setheading(60)
begin_fill()
fillcolor("#fdadc8")
pencolor("#fdadc8")
def straw(up):
    forward(up)
    right(90)

straw(150)
straw(20)
straw(150)
straw(20)
end_fill()

# word
turtleBeads.teleport(-150, 110)
pencolor("#fe832f")
write("CAFE", font = ("Arial Rounded MT Bold", 60))

turtleBeads.showPicture()
mainloop()