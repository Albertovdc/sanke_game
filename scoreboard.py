from turtle import Turtle
class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.goto(0, 280)
    self.color("Green")
    self.hideturtle()
    self.increase_score()

  def update_score(self):
    self.write(f"Score : {self.score}", align="center", font=("Arial", 14, "normal"))
    self.score += 1


  def increase_score(self):
    self.clear()
    self.update_score()
