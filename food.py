from turtle import Turtle
import random
class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("circle")
    self.color("white")
    self.shapesize(stretch_wid=0.5, stretch_len=0.5)
    self.reappear()
    # I think that this line is not necessary at all
    # self.speed("fastest")

  def reappear(self):
    x_coord = random.randint(-280, 280)
    y_coord = random.randint(-280, 280)
    self.goto(x_coord, y_coord)
