import turtle
import time
import random

window = turtle.Screen()
window.title("Snake Snake")
window.bgcolor("indigo")
window.setup(500, 650)
window.tracer(0)
delay = 0.1

head = turtle.Turtle()
head.speed(0)
head.color("gold")
head.shape("square")
head.up()
head.setpos(0, 0)
head.direction = "stop"

bodies = []

randx = random.randint(-230, 230)
randy = random.randint(-250, 300)
food = turtle.Turtle()
food.speed(0)
food.color("crimson")
food.shape("square")
food.up()
food.setpos(randx, randy)

sc = 0
hsc = 0
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.up()
score.hideturtle()
score.setpos(0, -302)
score.write(f"Score: {sc} High Score: {hsc}", align = "center", font = ("Arial", 24, "bold"))



def move_up():
    if head.direction != "down":
        time.sleep(0.001)
        head.direction = "up"
def move_down():
    if head.direction != "up":
        time.sleep(0.001)
        head.direction = "down"
def move_right():
    if head.direction != "left":
        time.sleep(0.001)
        head.direction = "right"
def move_left():
    if head.direction != "right":
        time.sleep(0.001)
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def buttonClick(x, y):
    print(f"Coordinate ({x}, {y})")
def resetGame():
    score.clear()
    score.write("You Lost!")
    time.sleep(1)
    head.setpos(0, 0)
    head.direction = "stop"
    for body in bodies:
        body.hideturtle()
    bodies.clear()

    randx = random.randint(-230, 230)
    randy = random.randint(-250, 300)
    food.setpos(randx, randy)
    score.clear()
    score.write(f"Score: {sc} High Score: {hsc}", align = "center", font = ("Arial", 24, "bold"))
    
window.listen()
window.onkeypress(move_up, "Up")
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "Down")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "Right")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "Left")
window.onkeypress(move_left, "a")
window.onscreenclick(buttonClick, 1)
print(sc)

while True:
    window.update()
    if head.distance(food) < 20:
        randx = random.randint(-230, 230)
        randy = random.randint(-250, 300)
        food.setpos(randx, randy)
        delay -= 0.002
        print(delay)    

        sc += 1
        score.clear()
        score.write(f"Score: {sc} High Score: {hsc}", align = "center", font = ("Arial", 24, "bold"))

        global newBody
        newBody = turtle.Turtle()
        newBody.up()
        newBody.shape("square")
        newBody.color("black")
        bodies.append(newBody)

        if sc > hsc:
            hsc = sc
            score.clear()
            score.write(f"Score: {sc} High Score: {hsc}", align = "center", font = ("Arial", 24, "bold"))

    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index-1].xcor() 
        y = bodies[index-1].ycor()
        bodies[index].setpos(x, y)

    if len(bodies) > 0: 
        x = head.xcor()
        y = head.ycor()
        bodies[0].setpos(x, y)

    


    if head.xcor() > 235 or head.xcor() < -237 or head.ycor() > 320 or head.ycor() < -305:
        sc = 0
        delay = 0.1
        resetGame()
    
    move()

    for body in bodies:
        if body.distance(head) < 20:
            sc = 0
            delay = 0.1
            resetGame()
            head.direction = "stop"
    
    time.sleep(delay)


window.mainloop()           