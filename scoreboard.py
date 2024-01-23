from turtle import Turtle


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.goto(0, 280)
    self.color("Green")
    self.hideturtle()
    self.update_score()

  def update_score(self):
    self.write(f"Score : {self.score}", align="center", font=("Arial", 14, "normal"))

  def increase_score(self):
    self.clear()
    self.score += 1
    self.update_score()

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", align="center", font=("Arial", 14, "normal"))
