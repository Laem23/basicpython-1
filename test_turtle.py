import sys
print(sys.version)

import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Rectangle():
    for i in range(4):
        tao.forward(100)
        tao.left(90)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(200,200)
Rectangle()
Go(-200,-200)
Rectangle()
Go(100,100)
Rectangle()
Go(0,0)
Rectangle()
Go(-100,-100)
Rectangle()
Go(-200,200)
Rectangle()
Go(-100,100)
Rectangle()
Go(100,-100)
Rectangle()
Go(200,-200)
Rectangle()
