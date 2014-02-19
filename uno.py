print """
Welcome to the Python Uno Game!
In this game, each player starts off with 7 Cards. Each which either have the colors Blue, Red, Green, or Yellow on one side.
On the other side, there is a number that is in the range from 1 to 10. The first player puts a random card from their deck
to start a stack in the middle of the table. The Objective in the game is to put down a card that is matching the card in 
the central stack by either the color or the number. Each time you put down a matching card, you lose a card. If you don't
have a card with a matching color or number, you will have to draw a random card. The first player to have 1 Card and call
out 'UNO!' wins!
Warning: Makes sure you type 'UNO' if you have 1 Card!Or else you will be stuck in an infinite loop until you type 'UNO'!"""
print " "
import random
import sys
colors = ["Blue", "Red", "Green", "Yellow"]
numbers = range(1, 10)
user_deck = []
com_deck = []
choices = ["", "deck", "draw", "pass", "exit", "com", "uno", "decks"]
count = 1
count_deck = " "
while type(count_deck) != int:
            try:
                count_deck = int(raw_input("How many cards do you want in each deck? Number must be greater than 3 and less than 36."))
                if count_deck > 3 and count_deck < 36:
                    None
                else:
                    count_deck = " "
            except ValueError:
                None
while len(user_deck) < count_deck:
    user_card_color = random.choice(colors)
    user_card_num = random.choice(numbers)
    user_card = [user_card_color, user_card_num]
    if user_card not in user_deck:
        user_deck.append(user_card)
while len(com_deck) < count_deck:
    com_card_color = random.choice(colors)
    com_card_num = random.choice(numbers)
    com_card = [com_card_color, com_card_num]
    if com_card not in com_deck:
        com_deck.append(com_card)
def random_user_card():
    rand_color = random.choice(colors)
    rand_num = random.choice(numbers)
    rand_card = [rand_color, rand_num]
    if rand_card not in user_deck:
        user_deck.append(rand_card)
        print
        print "You have drawn: %s" % "[" + rand_card[0] + " : " + str(rand_card[1]) + "]"
def random_com_card():
    rand_color = random.choice(colors)
    rand_num = random.choice(numbers)
    rand_card = [rand_color, rand_num]
    if rand_card not in com_deck:
        com_deck.append(rand_card)
        print " "
        print "The Computer has drawn a card."
print " "
print "-*-"
print "Your Deck:"
for i in user_deck:
    i[1] = str(i[1])
    print "[" + i[0] + " : " + i[1] + "]"
    i[1] = int(i[1])
print " "
print "Computer Deck:"
for i in com_deck:
    i[1] = str(i[1])
    print "[" + i[0] + " : " + i[1] + "]"
    i[1] = int(i[1])
print "-*-"
while len(user_deck) > 1 or len(com_deck) > 1:
    ask = "foo"
    while ask.lower() not in choices:
        print " "
        print "Press [Enter] if you would like to continue."
        print "Type [Deck] if you would like to see your deck and statistics."
        print "Type [Draw] if you believe it is necessary to draw a card."
        print "Type [Pass] if you would like to skip a turn."
        print "Type [Exit] to exit the program if needed."
        ask = raw_input("")
    if ask.lower() == choices[0]:
        if count % 2 != 0:
            print "-*-"
            print "Round #%d:" % count
            stack_card = [" "]
            while stack_card not in user_deck:
                color_card = raw_input("Enter a Color:")
                try:
                    num_card = int(raw_input("Enter a Number:"))
                    stack_card = [color_card, num_card]    
                except ValueError:
                    None
            if color_card in colors and num_card in numbers:     
                user_deck.remove(stack_card)
                for i in com_deck:
                    com_card_color = i[0]
                    com_card_num = i[1]
                    if color_card == com_card_color or num_card == com_card_num:
                        print " "
                        print "You put down the card: %s" % stack_card
                        print "The Computer put down: %s" % i
                        print "-*-"
                        prev_card = i
                        if color_card == com_card_color:
                            if num_card == com_card_num:
                                com_deck.remove(i)
                                break
                            else:
                                com_deck.remove(i)
                                break
                        elif num_card == com_card_num:
                            if color_card == com_card_color:
                                com_deck.remove(i)
                                break
                            else:
                                com_deck.remove(i)
                                break
                        else:
                            random_com_card()
                            break
                count += 1
            else:
                print " "
                print "The card you specified is not in either deck."
        elif count % 2 == 0:
            print "-*-"
            print "Round #%d:" % count
            while stack_card not in user_deck:
                color_card = raw_input("Enter a Color:")
                try:
                    num_card = int(raw_input("Enter a Number:"))
                    stack_card = [color_card, num_card]    
                except ValueError:
                    None
            if color_card in colors and num_card in numbers:     
                if color_card in prev_card or num_card in prev_card:
                    user_deck.remove(stack_card)
                    for i in com_deck:
                        com_card_color = i[0]
                        com_card_num = i[1]
                        if color_card == com_card_color or num_card == com_card_num:
                            print " "
                            print "You put down the card: %s" % stack_card
                            print "The Computer put down: %s" % i
                            print "-*-"
                            prev_card = i
                            if color_card == com_card_color:
                                if num_card == com_card_num:
                                    com_deck.remove(i)
                                    break
                                else:
                                    com_deck.remove(i)
                                    break
                            elif num_card == com_card_num:
                                if color_card == com_card_color:
                                    com_deck.remove(i)
                                    break
                                else:
                                    com_deck.remove(i)
                                    break
                            else:
                                random_com_card()
                                break
                else:
                    print " "
                    print "You have to put down a card that has either a matching color or number."
            else:
                print " "
                print "The card you specified is not in either deck."
            count += 1
    elif ask.lower() == choices[1]:
        print " "
        print "-*-"
        print "Your Deck:"
        for i in user_deck:
            i[1] = str(i[1])
            print "[" + i[0] + " : " + i[1] + "]"
            i[1] = int(i[1])
        print " "
        print "You have %d cards in your deck." % len(user_deck)
        print "The Computer has %d in their deck." % len(com_deck)
        print "You are currently in Round #%s." % count
        print "-*-"
    elif ask.lower() == choices[2]:
        if count > 1:
            random_user_card()
        else:
            print "You can't draw on the first round!"
    elif ask.lower() == choices[3]:
        if count > 1:
            com_deck.remove(random.choice(com_deck))
        else:
            print " "
            print "You can't pass on the first round!"
    elif ask.lower() == choices[4]:
        print "Exiting the Program..."
        sys.exit()
    elif ask.lower() == choices[5]:
        print " "
        print "-*-"
        print "Computer's Deck:"
        for i in user_deck:
            i[1] = str(i[1])
            print "[" + i[0] + " : " + i[1] + "]"
            i[1] = int(i[1])
        print " "
        print "The Computer has %d cards in their deck." % len(com_deck)
        print "You have %d in your deck." % len(user_deck)
        print "You are currently in Round #%s." % count
        print "-*-"
    elif ask.lower() == choices[6]:
        print " "
        print "You can't call UNO! yet."
    elif ask.lower() == choices[7]:
        print " "
        print "-*-"
        print "Your Deck:"
        for i in user_deck:
            i[1] = str(i[1])
            print "[" + i[0] + " : " + i[1] + "]"
            i[1] = int(i[1])
        print " "
        print "You have %d cards in your deck." % len(user_deck)
        print "The Computer has %d in their deck." % len(com_deck)
        print "You are currently in Round #%s." % count
        print "------------------------------------------------------------"
        print "Computer's Deck:"
        for i in user_deck:
            i[1] = str(i[1])
            print "[" + i[0] + " : " + i[1] + "]"
            i[1] = int(i[1])
        print " "
        print "The Computer has %d cards in their deck." % len(com_deck)
        print "You have %d in your deck." % len(user_deck)
        print "You are currently in Round #%s." % count
        print "-*-"
while len(user_deck) == 1 or len(com_deck) == 1:
    ask = "foo"
    while ask.lower() not in choices:
        print " "
        print "Press [Enter] if you would like to continue."
        print "Type [Deck] if you would like to see your deck and statistics."
        print "Type [Draw] if you believe it is necessary to draw a card."
        print "Type [Pass] if you would like to skip a turn."
        print "Type [Exit] to exit the program if needed."
        ask = raw_input("")
    if len(user_deck) == 1:
        if ask.lower() == "uno":
            print "-*-"
            print "You Win!"
            print "-*-"
            break
        else:
            print "Don't you have something to say?"
    elif len(com_deck) == 1:
        print "You Lose! The Computer was first to win UNO."
        break