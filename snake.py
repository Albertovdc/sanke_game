from turtle import Turtle


class Snake:
  def __init__(self):
    self.position = [0, -20, -40]
    self.body_snake = []
    self.create_body()

  def create_body(self):
    for n in self.position:
      segment = Turtle("square")
      segment.color("white")
      segment.penup()
      segment.goto(n, 0)
      self.body_snake.append(segment)

  def move(self):
    for segm in range(len(self.body_snake) - 1, 0, -1):
      new_x = self.body_snake[segm - 1].xcor()
      new_y = self.body_snake[segm - 1].ycor()
      self.body_snake[segm].goto(new_x, new_y)

    self.body_snake[0].forward(20)
