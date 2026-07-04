import turtle as t
import random

def setup_screen():
    sc = t.Screen()
    sc.title("Snake Game")
    sc.bgcolor("#add8e6")
    sc.setup(width=600, height=600)
    sc.tracer(0)
    return sc

def create_head():
    h = t.Turtle()
    h.speed(0)
    h.shape("square")
    h.color("white")
    h.penup()
    h.goto(0, 0)
    h.direction = "Stop"
    return h

def create_food():
    f = t.Turtle()
    f.speed(0)
    f.shape(random.choice(["circle", "square", "triangle"]))
    f.color(random.choice(["red", "green", "black"]))
    f.penup()
    f.goto(0, 100)
    return f

def create_scoreboard():
    p = t.Turtle()
    p.speed(0)
    p.hideturtle()
    p.penup()
    p.goto(0, 250)
    p.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))
    return p