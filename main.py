from turtle import Turtle, Screen
import time
# Screen set up
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Create snake body
position = [0, -20, -40]
body_snake = []
for n in position:
  segment = Turtle("square")
  segment.color("white")
  segment.penup()
  segment.goto(n, 0)
  body_snake.append(segment)

# Move snake
game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)
  # for segm in body_snake:
  #   segm.forward(20)
  #   time.sleep(0.03)
  for segm in range(len(body_snake) - 1, 0, -1):
    new_x = body_snake[segm - 1].xcor()
    new_y = body_snake[segm - 1].ycor()
    body_snake[segm].goto(new_x, new_y)

  body_snake[0].forward(20)
  body_snake[0].left(90)

screen.exitonclick()
