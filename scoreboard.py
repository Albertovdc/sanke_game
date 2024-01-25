from turtle import Turtle


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    # To close and open th document
    with open("score.txt") as score_file:
      # Read the content (read, append an writtings)
      data = score_file.read()
      self.high_score = int(data)
    self.score = 0
    self.goto(0, 280)
    self.color("Green")
    self.hideturtle()
    self.update_text()

  def update_text(self):
    self.clear()
    self.write(f"Score : {self.score} Highscore {self.high_score}", align="center", font=("Arial", 14, "normal"))

  def increase_score(self):

    self.score += 1
    self.update_text()

  def update_highscore(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("score.txt", "w") as score_file:
        score_file.write(str(self.high_score))
    self.score = 0
    self.update_text()

  # def game_over(self):
  #   self.goto(0, 0)
  #   self.write("GAME OVER", align="center", font=("Arial", 14, "normal"))
