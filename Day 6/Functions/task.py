#reeborg.ca
def squard_quick():
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()

def squard_long():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()

#nw
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

#nwnw
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()