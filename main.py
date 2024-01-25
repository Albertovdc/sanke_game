from turtle import Screen
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Screen set up
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Create snake body
# position = [0, -20, -40]
# body_snake = []
# for n in position:
#   segment = Turtle("square")
#   segment.color("white")
#   segment.penup()
#   segment.goto(n, 0)
#   body_snake.append(segment)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Snake directions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Move snake
game_on = True
while game_on:
  screen.update()
  time.sleep(0.1)

  # for segm in body_snake:
  #   segm.forward(20)
  #   time.sleep(0.03)
  # for segm in range(len(body_snake) - 1, 0, -1):
  #   new_x = body_snake[segm - 1].xcor()
  #   new_y = body_snake[segm - 1].ycor()
  #   body_snake[segm].goto(new_x, new_y)
  # body_snake[0].forward(20)
  snake.move()

  # snake detect food
  if snake.body_snake[0].distance(food) < 15:
    food.reappear()
    snake.add_segment(snake.body_snake[-1].position())
    scoreboard.increase_score()

  # snake colides with the wall
  if snake.body_snake[0].xcor() > 280 or snake.body_snake[0].xcor() < -280 or snake.body_snake[0].ycor() > 280 or \
      snake.body_snake[0].ycor() < -280:
    # game_on = False
    # scoreboard.game_over()
    snake.reset()
    scoreboard.update_highscore()

  for segment in snake.body_snake[1:]:
    # if segment == snake.body_snake[0]:
    #   pass
    if snake.body_snake[0].distance(segment) < 10:
      # game_on = False
      # scoreboard.game_over()
      snake.reset()
      scoreboard.update_highscore()

screen.exitonclick()
