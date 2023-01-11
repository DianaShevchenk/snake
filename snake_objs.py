import turtle as t
import random


class Snake:
    def __init__(self, x, y, shape, color_snake, color_head):
        self.head = self.create_turtle(x, y, 'turtle', color_head)
        self.snake = [self.create_turtle(-20 * (i + 1) + x, y, 'turtle', color_snake) for i in range(4)]
        self.color_snake = color_snake

    def create_turtle(self, x, y, shape, color):
        print(x, y)
        tmp = t.Turtle()
        tmp.shape(shape)
        tmp.penup()
        tmp.color(color)
        tmp.setx(x)
        tmp.sety(y)
        return tmp

    def step(self):
        (pos, hd) = (self.head.pos(), self.head.heading())
        for s in self.snake:
            (tmp_pos, tmp_hd) = (s.pos(), s.heading())
            s.setheading(hd)
            s.setpos(pos)
            (hd, pos) = (tmp_hd, tmp_pos)
        self.head.forward(20)

    def check_food(self, food):
        if self.head.distance(food.food) < 20:
            return True
        else:
            return False

    def grow(self):
        [x, y] = self.snake[-1].pos()
        self.snake.append(self.create_turtle(x, y, 'turtle', self.color_snake))

    def turn(self, angle):
        self.head.setheading(angle)



class Screen:

    def __init__(self, width, height, color):
        self.wn = t.Screen()
        self.wn.title('Test game')
        self.wn.bgcolor(color)
        self.wn.setup(width=width, height=height)
        self.wn.tracer(0)

    def proc_event(self, obj):
        self.objs = obj
        self.wn.listen()
        self.wn.onkeypress(self.goleft, "Left")
        self.wn.onkeypress(self.goright, "Right")
        self.wn.onkeypress(self.goup, "Up")
        self.wn.onkeypress(self.godown, "Down")

    def goleft(self):
         for i in range(len(self.objs)):
            head= self.objs[i]
            head.turn((180+i*180)%360) 

    def goright(self):
         for i in range(len(self.objs)):
            head= self.objs[i]
            head.turn((0+i*180)%360) 

    def goup(self):
         for i in range(len(self.objs)):
            head= self.objs[i]
            head.turn((270+i*180)%360) 

    def godown(self):
         for i in range(len(self.objs)):
            head= self.objs[i]
            head.turn((90+i*180)%360) 

    def update(self):
        self.wn.update()


class Food:
    def __init__(self, color, shape):
        self.food = t.Turtle()
        self.food.shape(shape)
        self.food.penup()
        self.food.color(color)
        self.move()

    def move(self):
        self.food.setpos(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))








