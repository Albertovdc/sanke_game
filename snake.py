from turtle import Turtle
# I added this modification because the moment the snake increases the size appears a white square in the center of the
# screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
  def __init__(self):
    self.body_snake = []
    self.create_body()

  def create_body(self):
    for coords in STARTING_POSITIONS:
      self.add_segment(coords)

  def add_segment(self, coord):
    segment = Turtle("square")
    segment.speed("fastest")
    segment.color("white")
    segment.penup()
    segment.goto(coord)
    self.body_snake.append(segment)

  def move(self):
    for segm in range(len(self.body_snake) - 1, 0, -1):
      new_x = self.body_snake[segm - 1].xcor()
      new_y = self.body_snake[segm - 1].ycor()
      self.body_snake[segm].goto(new_x, new_y)

    self.body_snake[0].forward(20)
  def up(self):
    if self.body_snake[0].heading() != 270:
      self.body_snake[0].setheading(90)
  def down(self):
    if self.body_snake[0].heading() != 90:
      self.body_snake[0].setheading(270)

  def right(self):
    if self.body_snake[0].heading() != 180:
      self.body_snake[0].setheading(0)

  def left(self):
    if self.body_snake[0].heading() != 0:
      self.body_snake[0].setheading(180)

  def reset(self):
    for item in self.body_snake:
      item.goto(1000,1000)
    self.body_snake.clear()
    self.create_body()