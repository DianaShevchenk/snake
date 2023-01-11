import snake_objs
import time

delay = 0.2
color_wnd = 'gray'
color_head = 'pink'
color_snake = 'light blue'
color_food = 'green'

screen = snake_objs.Screen(600, 600, color_wnd)
food = snake_objs.Food(color_food, 'circle')

snakes = [snake_objs.Snake(i*30, i*50, 'turtle', color_snake, color_head)
          for i in range(3)]

screen.proc_event(snakes)

while True:
    screen.update()

    for snake in snakes:
        snake.step()
        if snake.check_food(food):
            snake.grow()
            food.move()

    time.sleep(delay)

