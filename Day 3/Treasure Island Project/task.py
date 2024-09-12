print('''
 .d88b.  8888b. 88888b.d88b.  .d88b.  
d88P"88b    "88b888 "888 "88bd8P  Y8b   
888  888.d888888888  888  8888888888 
Y88b 888888  888888  888  888Y8b.         
 "Y88888"Y888888888  888  888 "Y8888  
     888                                      
Y8b d88P                                      
 "Y88P"                     
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

game_over = ('''
              ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO|
       ::::::;       ;          OOOOO|
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

''')


treasure = ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."| ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


lake_p = ('''
                  _
             .''.' |    _  __
 ___         './    '. ' `'  `
    '._______.'       |
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'                               
 ___.'       '.       /               '-._                        
             .'|    .' ._,.__,        ____|____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _|    'o'
                                      .-'

''')


island = ('''
                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /|         /sssssSSSSSSSSSSSSSSSssssssssssss.                  
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''')


#road
cross_road = input("""
You're at a cross road. Where do you want to go?
    Type 'left' or 'right'.
""").lower()
if cross_road == "left" or cross_road == "l":
    print(f"""
        {lake_p}               
    You've come to a lake. there is an island in the middle of the lake.
    """)
    lake = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    #lake
    if lake == "wait" or lake == "w":
        print(f"""
                {island}
                You arrive at the island unharmed.
                """)
        doors = input("There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        #doors
        if doors == "red" or doors == "r":
            print(f"""
                {game_over}
                It's a room full of fire. Game over.
                """)
        elif doors == "yellow" or doors == "y":
            print(f"""
                {treasure}
                You found the treasure! You Win!
                """)
        elif doors == "blue" or doors == "b":
            print(f"""
                {game_over}
                You enter a room of beasts. Game over.
                """)
        else:
            print(f"""
                {game_over}
                You have not fulfilled the conditions.Game over.
                """)
    elif lake == "swim" or lake == "s":
        print(f"""
        {game_over}
        You get attacked by angry trout. Game Over.
        """)
    else:
        print(f"""
        {game_over}
        You have not fulfilled the conditions.Game over.
        """)
elif cross_road == "right" or cross_road == "r":
    print(f"""
        {game_over}           
        You fell into a hole. Game over.
        """)
else:
    print(f"""
        {game_over}
        You have not fulfilled the conditions.Game over.
        """)