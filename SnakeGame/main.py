from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

for positions in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(positions)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)




screen.exitonclick()