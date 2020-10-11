import turtle
wn = turtle.Screen()
wn.title("draw land")
wn.bgcolor("lime")
player = turtle.Turtle()
player.shape("circle")
player.penup()
def move_up():
    y = player.ycor()
    y += 10
    player.sety(y)
def move_down():
    y = player.ycor()
    y -= 10
    player.sety(y)
def move_left():
    x = player.xcor()
    x -= 10
    player.setx(x)
def move_right():
    x = player.xcor()
    x += 10
    player.setx(x)
def red():
    player.color("red")
def black():
    player.color("black")
def brown():
    player.color("brown")
def blue():
    player.color("blue")
def green():
    player.color("green")
def pink():
    player.color("hot pink")
def pu():
    player.penup()
def pd():
    player.pendown()
def erase():
    player.penup()
    player.clear()
    player.home()
wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeypress(black, "1")
wn.onkeypress(red, "2")
wn.onkeypress(brown, "3")
wn.onkeypress(blue, "4")
wn.onkeypress(green, "5")
wn.onkeypress(pink, "6")
wn.onkeypress(pu, "Up")
wn.onkeypress(pd, "Down")
wn.onkeypress(erase, "0")
while True:
    wn.update()
