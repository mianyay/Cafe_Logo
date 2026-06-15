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
