### sudden movements causing snake to die
####  in new life snake is smaller

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

s=Screen()
s.tracer(0.1)
s.bgcolor("black")
s.setup(600,600)
s.title("my snake game")

bud=Snake()
bud.create_snake()

foody=Food()

score=Score()

s.listen()
s.onkey(bud.up,"Up")
s.onkey(bud.down,"Down")
s.onkey(bud.left,"Left")
s.onkey(bud.right,"Right")

is_on=True
while is_on:
    s.update()
    time.sleep(0.1)

    bud.snake_movements()

    if bud.collision_tail():
        score.resett()
        bud.resett()
    if bud.collision_wall():
        score.resett()
        bud.resett()
    if bud.snake_head.distance(foody)<15 :
        foody.refresh()
        score.increase_score()
        bud.extend()
    # for segment in bud.segments:
    #     if segment == bud.snake_head:
    #         pass
    #     elif bud.snake_head.distance(segment) < 10:
    #         score.resett()
    #         bud.resett()




s.exitonclick()