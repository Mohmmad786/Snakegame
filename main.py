import time
import turtle as t
import random
from game_objects import setup_screen, create_head, create_food, create_scoreboard
from control import move_snake, setup_controls

def reset_game(head, segments, scoreboard, score, high_score):
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Stop"
    
    # Move segments off-screen before clearing
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    
    scoreboard.clear()
    scoreboard.write(f"Score : 0  High Score : {high_score}", align="center", font=("candara", 24, "bold"))
    
    return 0, 0.1  # Return reset score and starting delay

def main():
    sc = setup_screen()
    h = create_head()
    f = create_food()
    p = create_scoreboard()
    
    setup_controls(sc, h)
    
    seg = []
    d = 0.1
    s = 0
    hs = 0
    run = True
    
    while run:
        try:
            sc.update()
            
            # 1. Wall collision
            if abs(h.xcor()) > 290 or abs(h.ycor()) > 290:
                s, d = reset_game(h, seg, p, s, hs)
                
            # 2. Food collision
            if h.distance(f) < 20:
                f.goto(random.randint(-270, 270), random.randint(-270, 270))
                new_seg = t.Turtle()
                new_seg.speed(0)
                new_seg.shape("square")
                new_seg.color("purple")
                new_seg.penup()
                seg.append(new_seg)
                
                # Prevent delay from dropping below zero (crash fix)
                d = max(0.02, d - 0.005) 
                s += 10
                
                if s > hs:
                    hs = s
                p.clear()
                p.write(f"Score : {s}  High Score : {hs}", align="center", font=("candara", 24, "bold"))
                
            # 3. Move body segments
            for i in range(len(seg) - 1, 0, -1):
                x = seg[i - 1].xcor()
                y = seg[i - 1].ycor()
                seg[i].goto(x, y)
                
            if len(seg) > 0:
                seg[0].goto(h.xcor(), h.ycor())
                
            move_snake(h)
            
            # 4. Self collision
            for segment in seg:
                if segment.distance(h) < 20:
                    s, d = reset_game(h, seg, p, s, hs)
                    break  # CRITICAL: Stop iterating over the list after we clear it
                    
            time.sleep(d)
            
        except t.Terminator:
            run = False # Clean exit when you close the window

if __name__ == "__main__":
    main()
