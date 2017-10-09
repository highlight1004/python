import turtle
#画长方形
def Rectangle(x, y, width, height):
        #设置画笔
        turtle.penup()
        turtle.color("red", "red")
        turtle.goto(x, y)
        turtle.pendown()
        #开始画
        turtle.begin_fill()
        for i in range(2):
                turtle.forward(width)
                turtle.right(90)
                turtle.forward(height)
                turtle.right(90)
        turtle.end_fill()
#画五角星
def Star(radius):
        #设置画笔
        turtle.penup()
        turtle.color("yellow", "yellow")
        turtle.pendown()
        #开始画
        #确定五个顶点的位置坐标
        turtle.penup()
        p1 = turtle.position()
        turtle.circle(-radius, 72)
        p2 = turtle.position()
        turtle.circle(-radius, 72)
        p3 = turtle.position()
        turtle.circle(-radius, 72)
        p4 = turtle.position()
        turtle.circle(-radius, 72)
        p5 = turtle.position()
        turtle.circle(-radius, 72)
        turtle.pendown()
        #连接五个顶点并且填充为黄色
        turtle.begin_fill()
        turtle.goto(p3)
        turtle.goto(p5)
        turtle.goto(p2)
        turtle.goto(p4)
        turtle.goto(p1)
        turtle.end_fill()
#画大五角星
def BigStar(Bigcenter_x,Bigcenter_y, radius):
        #设置初始位置
        turtle.penup()
        turtle.goto(Bigcenter_x, Bigcenter_y + radius)
        turtle.pendown()
        #开始画大五角星
        Star(radius)
def SmallStar(center_x, center_y, radius):
        #设置初始位置
        turtle.penup()
        turtle.home()
        turtle.goto(center_x, center_y)
        angle = turtle.towards(Bigcenter_x, Bigcenter_y) - 90
        turtle.goto(center_x, center_y + radius)
        turtle.circle(-radius, -angle)
        turtle.pendown()
        #开始画小五角星
        Star(radius)
'''
Rectangle(600, 400)
Bigcenter_x = 100
Bigcenter_y = -100
BigStar(100, -100, 60)
SmallStar(200, -40, 20)
SmallStar(240, -80, 20)
SmallStar(240, -140, 20)
SmallStar(200, -180, 20)
'''
#定义尺寸和左上角位置坐标
#左上角位置坐标
x = -400
y = 200
#国旗宽度
width = 800
height =width * 2 / 3
per = width / 30
Bigcenter_x = x + per * 5
Bigcenter_y = y - per * 5
Bigradius = per * 3
center_x = [x + per * 10,x + per * 12, x + per * 12, x + per * 10]
center_y = [y - per * 2, y - per * 4, y - per * 7, y - per * 9]
Smallradius = per
#开始画
turtle.hideturtle()
Rectangle(x, y, width, height)
BigStar(Bigcenter_x, Bigcenter_y, Bigradius)
for i in range(4):
        SmallStar(center_x[i], center_y[i], Smallradius)
