from turtle import Turtle
FONT=("courier",18,"normal")
ALIGNMENT="center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scr=0
        with open("high_score.txt") as data:
            self.high_scr=int(data.read())
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.write(f"score:{self.scr} highscore:{self.high_scr}",align=ALIGNMENT,font=FONT)
    def increase_score(self):
        self.clear()
        self.scr+=1
        self.write(f"score:{self.scr} highscore:{self.high_scr}",align=ALIGNMENT,font=FONT)

    def resett(self):
        self.clear()
        if self.scr>self.high_scr:
            self.high_scr=self.scr
            with open("high_score.txt","w") as data:
                data.write(f"{self.high_scr}")
        self.scr=0
        self.write(f"score:{self.scr} highscore:{self.high_scr}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER ", align=ALIGNMENT, font=FONT)