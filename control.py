def go_up(head):
    if head.direction != "down":
        head.direction = "up"

def go_down(head):
    if head.direction != "up":
        head.direction = "down"

def go_left(head):
    if head.direction != "right":
        head.direction = "left"

def go_right(head):
    if head.direction != "left":
        head.direction = "right"

def move_snake(head):
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

def setup_controls(screen, head):
    screen.listen()
    
    # Arrow Keys
    screen.onkeypress(lambda: go_up(head), "Up")
    screen.onkeypress(lambda: go_down(head), "Down")
    screen.onkeypress(lambda: go_left(head), "Left")
    screen.onkeypress(lambda: go_right(head), "Right")
    
    # WASD Keys
    for key, func in [("w", go_up), ("s", go_down), ("a", go_left), ("d", go_right),
                      ("W", go_up), ("S", go_down), ("A", go_left), ("D", go_right)]:
        screen.onkeypress(lambda f=func: f(head), key)

    # Mouse Click Controls (calculates direction based on click position relative to snake)
    def click_direction(x, y):
        screen.listen() # Regain window focus on click
        hx, hy = head.xcor(), head.ycor()
        dx, dy = x - hx, y - hy
        
        # Determine if click was more horizontal or vertical
        if abs(dx) > abs(dy): 
            if dx > 0: go_right(head)
            else: go_left(head)
        else:
            if dy > 0: go_up(head)
            else: go_down(head)

    screen.onscreenclick(click_direction)