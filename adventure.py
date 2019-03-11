from sys import exit
import os
import time

# --------------------------- VARS ---------------------------


beast_alive = True

dragon_alive = True
sword = False
# ------------------------- ROUTINES -------------------------

# ROOM 1

def room_1():
    print ("You are in a big room with blood covered walls.")
    print ("It's really dark and all you can see is three doors.")
    print ("They lead east, north and west. What do you do?")

    choice = input("> ");

    if "west" in choice:
        room_2()
    elif "north" in choice:
        room_4()
    elif "east" in choice:
        game_over("""You carefully go through the narrow passage heading
east. After walking for three minutes, you see that
it ends with a solid wall. You turn around to get back
but you find yourself facing another wall. Somewhat,
you have trapped youself. Without water nor food, you
die some days later.""")
    else:
        room_1()

# ROOM 2

def room_2():
    print ("This room has a really low ceiling and you must crouch to walk.")
    print ("You see a passage leading west and a passage leading north.")
    print ("On the far end of the first one, you can see a bright light.")
    print ("From the second one, a really bad smell emanates.")
    print ("The passage to the east leads to the first room.")
    print ("What do you do?")

    choice = input("> ");

    if "west" in choice:
        game_over("""You follow the bright path. As you walk, the light
gets brighter and brighter, until you can't see anything.
Suddenly you can no longer feel the floor under your
feet and, as you fall in a pit of flames, you understand
where the light came from. You die screaming in pain.""")
    elif "north" in choice:
        room_3()
    elif "east" in choice:
        room_1()
    else:
        room_2()

# ROOM 3

def room_3():
    global beast_alive
    global sword
    if beast_alive:
        print ("As you walk into the room, you understand where the smell came from.")
        print ("The floor is littered with rotting corpses.")
        print ("Suddenly you hear a growl and a huge beast appears in front of you.")
        print ("You see a passage to the east, a flaming torch on the ground,")
        print ("a skeleton holding a sword and a hole on the far side of the room.")
        print ("The passage to the south leads to the second room.")
        print ("What do you do?")

        choice = input("> ")

        if "east" in choice:
            game_over("""As you run towards the east passage, the beast leaps
in front of you. You don't have the time to do anything,
because the beast opens its jaws and rips of your head.""")
        elif "torch" in choice:
            print ("""You take the flaming torch and wave it in front of the
beast. It leaps back in fear, stumbles and falls in the
hole, disappearing from the room.""")
            beast_alive = False
            room_3()
        elif "sword" in choice:
            print ("""You take the sword. Suddenly, it starts emanating a faint
glow and you feel invincible. Without knowing how, you
jump forward and kill the beast.""")
            beast_alive = False
            sword = True
            room_3()
        elif "hole" in choice:
            game_over("""You jump in the dark. It wasn't
such a good idea, though. You start falling in the void,
never again hitting a floor. You die days later, still
falling.""")
        elif "south" in choice:
            room_2()
        else:
            room_3()

    else:
        print ("The floor is littered with rotting corpses.")
        print ("You see a passage to the east, a flaming torch on the ground,")
        print ("a skeleton holding a sword and a hole on the far side of the room.")
        print ("The passage to the south leads to the second room.")
        print ("What do you do?")

        choice = input("> ")

        if "east" in choice:
            room_4()
        elif "torch" in choice:
            print ("""You take the flaming torch and wave it in the air.
You feel stupid and put it down.""")
            room_3()
        elif "sword" in choice:
            print ("""You take the sword.""")
            sword = True
            room_3()
        elif "hole" in choice:
            game_over("""You jump in the dark. It wasn't
such a good idea, though. You start falling in the void,
never again hitting a floor. You die days later, still
falling.""")
        elif "south" in choice:
            room_2()
        else:
            room_3()

# ROOM 4

def room_4():
    global dragon_alive
    if dragon_alive:

        print ("The room is huge, and for a good reasons. It is the home of a dragon.")

        if sword:
            print ("""Suddenly your sword starts to glow. An unknown force urges you to
leap forward and drive the sword in the heart of the dragons.
It dies with horrible screams.""")
            dragon_alive = False
            room_4()
        else:
            print ("There is a passage to the north, one to the east, one to the")
            print ("south and one to the west. What do you do?")

        choice = input("> ")

        game_over("The dragon leaps in front of you and roasts you alive.")

    else:

        print ("There is a passage to the north, one to the east, one to the")
        print ("south and one to the west. What do you do?")

        choice = input("> ")

        if "east" in choice:
            game_over("""You follow the east passage until you end up in a little room with a desk and piece of paper. A small 
                        creature with cloven feet and hands suddenly notices your presence. 'You should 
                        not have found me!' he says. 'I will bind you to this place.' He writes something on the paper, and you die.""")
        elif "south" in choice:
            room_1()
        elif "west" in choice:
            room_3()
        elif "north" in choice:
            room_5()
        else:
            room_4()

def room_5():
    print ("You come to a room with a large pool of water and no apparent exits except the way you came (south).")
    print ("""On the far wall from the pool of water is a large flat surface with a beautifully engraved circular mosaic-like design
            that is inlaid with copper and shalestone. There is an outer ring of 19 letters: 'ZQKARLCTMDVNFWOGXPJ'.""")
    print ("On the inside it reads 'Come, human, die by sword or spear.'")
    choice = input("> ")
    
    if "south" in choice:
            room_4()
    elif "orpar" in choice:
            print("Upon speaking the command word, the wall recedes and reveals a hallway sloping upward. Will you leave or stay?")
            choice = input("> ")
            if "leave" in choice:
                room_6()
            elif "stay" in choice:
                print("The wall returns to its original position.")
                room_5()
    else:
        room_5()

def room_6():
    print("""As the hallway continues north, the temperature increases and bell notes waft through the air. You hear the stone door behind you close, there is no return.
The flagstones and ceiling tiles ahead appear to have crumbled apart ahead to the point of opening a chasm in the corridor. 
There is a bridge made of aged wooden planks crossing the 5 foot wide, bottomless expanse below. On the far side is a small alcove.
Written on the three walls of the alcove in jagged script are the following three quotes:""")
    print()
    print("'First I am broken, then I am seized'")      
    print("'Easily broken, but we are unable to be touched'")
    print("'BBBBBRRRRRRRRAAAAAACCCCHHHHEEEE'")
    print()
    print("The last line, written on the right wall, is written with the final letters curling down, as if the scribe had fallen into the chasm while writing them.")     
    choice = input("> ")
    if "day" in choice:
        print()
        print("You hear flagstones shift within the chasm, as if some mechanism stirs.")
        print()
        time.sleep(10)
        
        if "promise" in choice:
            print()
            print("The grinding of stones propogates closer up the chasm, but looking down, you don't see anything yet.")
            print()
            time.sleep(5)
            if "frostbite" in choice or "frost bite" in choice:
                room_6a()
            else:
                room_6()
        else:
            room_6()
    else:
        room_6()
def room_6a():
    print("""The mechanism groans as it moves closer, its lubrication having settled out with age. Sequentially, stairs emerge
from the side wall of the cavern beneath. It appears to be the only way out.""")
    choice = input("> ")
    if "stairs" or "down" in choice:
        room_7()
    else:
        room_6a()

def room_7():
    print ("""You descend into a circular stone room with 4 locations for tiles and piles of tiles with numbers 1-8. On the wall is a torch
attached to a large mechanical track. The torch appears to be able to move freely along the gridded track but is at the leftmost position.""")
    
    from random import randint
    from sys import stdout

    correct = [randint(1,8), randint(1,8), randint(1,8), randint(1,8)]
    usr_guess = [0, 0, 0, 0]
    usr_guess_output = []
    usr_guess_output_n = []

    guesses = 0

    #print('Welcome to Mastermind. Guess the combination of numbers between 1 and 9. \
      #  If you get the correct number and place, a \'*\' will be printed. \
     #   If you get the correct number but wrong place, a \'-\' will be printed. If you get it wrong completely, a \'#\' will be printed. \
      #  The position of the output does not correlate to the positions in the actual list of numbers.')
    print ("   _ _ _ _")  
    while(True):
      usr_guess_output_n = []
      usr_guess_output = []
      correct_count = 0
      guesses += 1
  
    #  try: #Makes sure that the program still works even if the user messes up the input
          
      usr_guess = input(' > ').split()
            
      usr_guess = [int(x) for x in usr_guess ] #Converts all list items into integers for comparisons
            
      # print(str(usr_guess)) --debug code--
      #print(str(correct))   --debug code--

      print('')
      i = 0
      answer_key = ['i', 'i', 'i', 'i'];
      tempcorrect = ['i','i','i','i'];
      for i in range(0,4):
          tempcorrect[i] = correct[i]
          if correct[i] == usr_guess[i]:
              answer_key[i] = '*'
              tempcorrect[i] = '*'
          
      #print (correct, tempcorrect, answer_key)
      for i in range(0,4):
          if usr_guess[i] in tempcorrect and answer_key[i] != '*':
              answer_key[i] = '#'
              tempcorrect[tempcorrect.index(usr_guess[i])] = '#'
          
       
      for i in range(0,4):
         if answer_key[i] != '#' and answer_key[i] != '*':
              answer_key[i] = '-'
         
      

      if answer_key == ['*','*','*','*']:
          break

      print (answer_key)    
    print ("""The torch, having finished tracing a four-star pattern, falls off the wall. Piece by piece, the wall crashes out towards you. Behind it is a square 5'x5' room
        with several objects: a BOTTLE OF WINE labeled 'POISON' which is enclosed in a PUZZLE. There is also a LOCKED CHEST. In a recession
        in the back wall is a DRAGON SKULL filled with FIRE, a PEN, and several SHEETS OF PAPER.""")
    print (""" [[[ You may now interact with the other items in the room. The only thing you make take out of the room is BOTTLE OF WINE if it is
            separated from PUZZLE for the purpose of sharing it to drink. It must be returned when the next person enters.
            You are not permitted to destroy or hide any ITEMS but you may reset PUZZLES and LOCKS as you see fit, or leave WRITINGS on PAPER for others. 
            The DRAGON SKULL and FIRE consume all items put inside, you may not inspect or withdraw any items placed inside! Press Enter ONLY when you are done. ]]] """)
    choice = input(" Have you completed your journey? >")
    rebirth()
           
# START
def rebirth():
        
        os.system('cls')
        print("......")
        time.sleep(240)
        start()
        
def start():
    
    if sword is True:
        print()
        print ("You currently have a sword.")
        print()
    room_1()

# GAME OVER

def game_over(s):

    global beast_alive
    global dragon_alive
    global sword

    beast_alive = True
    dragon_alive = True
    sword = False

    print (s)
    print ("Do you want to play again? (y / n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice = input("> ")
        if choice == "y":

            start()
        elif choice == "n":
            exit(0)


# --------------------------- MAIN ---------------------------

start()
