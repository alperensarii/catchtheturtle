import turtle
import random

score = 0
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("catch the turtle")
FONT = ("Ariel",30,"normal")
game_over = False
#turtle list

turtle_list = []

#score turtle

score_turtle = turtle.Turtle()

#countdown turtle

countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("dark blue")

    top_height = screen.window_height() / 2
    y = top_height * 0.88
    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score: 0",move=False,align="Center",font=FONT)


def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        #print(x,y)
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="Center", font=FONT)



    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.color("dark green")
    t.shapesize(2)
    t.goto(x * 15,y * 15)
    turtle_list.append(t)

x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10,20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


#recursive function (fonksiyon içinde fonksiyon çalıştırmak)
def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_randomly, 500)


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.color("black")

    top_height = screen.window_height() / 2
    y = top_height * 0.80
    countdown_turtle.setpos(0,y)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}",move=False,align="Center",font=FONT)
        screen.ontimer(lambda: countdown(time - 1) , 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over",move=False,align="Center",font=FONT)



hide_turtles()

turtle.tracer(0)

setup_score_turtle()
setup_turtles()

hide_turtles()
show_turtle_randomly()
countdown(10)
turtle.tracer(1)


turtle.mainloop()