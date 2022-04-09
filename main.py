from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create a snake body
snake = Snake()
# generate a random food on screen
food = Food()
# create a scoreboard
scoreboard = ScoreBoard()

# control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# start the game
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    # move the snake
    snake.move()
    # Detect collision between snake head with food
    if snake.snake_head.distance(food) < 15:  # this will return distance b/w snake_head and food
        food.refresh_food_pos()
        # adding new instance to snake_segments
        snake.extend()
        # increasing the score by 1
        scoreboard.increase_score()

    # Detect collision between snake head with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or \
            snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset_position()

    # Detect collision with tail
    for segment in snake.snake_segments[1:]:  # checking each segment of snake with head of snake
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_position()

# exit the screen on click
screen.exitonclick()
