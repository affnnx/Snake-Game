from turtle import Turtle
MOVE_DISTANCE = 10
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head=self.segments[0]

    def create_snake(self):
        x = 0
        for i in range(3):
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(x, 0)
            self.segments.append(t)
            x -= 20

    def snake_movements(self):
        for k in range(len(self.segments) - 1, 0, -1):
            x = self.segments[k - 1].xcor()
            y = self.segments[k - 1].ycor()
            self.segments[k].goto(x, y)
        self.snake_head.forward(MOVE_DISTANCE)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def extend(self):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(self.segments[-1].position())
        self.segments.append(t)

    def collision_tail(self):
        for segment in self.segments[1:]:
            if self.snake_head.distance(segment)<10:
               return True

    def collision_wall(self):
        if  self.snake_head.xcor()>280 or self.snake_head.xcor()<-280 or self.snake_head.ycor()>280 or self.snake_head.ycor()<-280:
            return True

    def resett(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head=self.segments[0]
        