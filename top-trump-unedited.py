import random
import time


print(" ______________________________ ")
print("|                              |")
print("|      Pokemon Top Trumps      |")
print("|______________________________|")
print("")

# start of the game
# Start the game
score = 0
print("~~ Welcome to the Pokemon Top Trumps Game.~~ \n The rules are simple, the player with the highest stat/number wins each round \n")
player1name = input("Player 1, please enter your name: ")
print("Hello " + player1name + ", get ready to enter the world of Pokemon!\n")
computername = "Computer"
print("You are playing against " + computername +  ", get ready...\n")
print("Your current score is, {}".format(score))

# creating an object, in this case a Top Trump card that has multiple properties: moves, power etc
class Card:
    def __init__(self, name, speed, power, accuracy, defence):
        self.name = name
        self.speed = speed
        self.power = power
        self.accuracy = accuracy
        self.defence = defence


# different cards showing the properties of the class above in order
cards = []
cards.append(Card("Acid", 35, 40, 100, 30))
cards.append(Card("Zubat", 55, 45, 100, 40))
cards.append(Card("Squirtle", 40, 30, 56, 47))
cards.append(Card("Pikachu", 65, 48, 100, 46))

random.shuffle(cards)

playerDeck = []
computerDeck = []

# Deal the cards
# return the "cards", start the while loop
while len(cards) > 0:
    playerDeck.append(cards.pop(0))
    computerDeck.append(cards.pop(0))

playerTurn = True
allowedResponses = ["a", "b", "c", "d"]

# add lists to start a loop
while len(playerDeck) > 0 and len(computerDeck) > 0:
    # suspends execution for a few seconds/mins
    time.sleep(1)

    playerCard = playerDeck.pop(0)
    computerCard = computerDeck.pop(0)
    # displays card on console and class properties
    print("YOUR CARD")
    print("Name:", playerCard.name)
    print("a. Power:", playerCard.power)
    print("b. Accuracy:", playerCard.accuracy)
    print("c. Speed:", playerCard.speed)
    print("d. Defence:", playerCard.defence)

    time.sleep(1)

# can only choose from the options displayed
#     .count returns a value already mentioned in the function, if its not mentioned the return will give error input
    if playerTurn == True:
        answer = input("Choose the following options: a, b, c, or d? ")
        while allowedResponses.count(answer) == 0:
            answer = input("That isn't a valid answer, please try again: ")
    else:
        answer = random.choice(allowedResponses)
        print("Computer chooses", answer)

    print("COMPUTER CARD")
    print("Name:", computerCard.name)

    playerWins = False

    if answer == "a":
        print("Power:", computerCard.power)
        isDraw = (playerCard.power == computerCard.power)
        playerWins = (playerCard.power > computerCard.power)
    elif answer == "b":
        print("Accuracy:", computerCard.accuracy)
        isDraw = (playerCard.accuracy == computerCard.accuracy)
        playerWins = (playerCard.accuracy > computerCard.accuracy)
    elif answer == "c":
        print("Speed::", computerCard.speed)
        isDraw = (playerCard.speed == computerCard.speed)
        playerWins = (playerCard.speed > computerCard.speed)
    elif answer == "d":
        print("Defence:", computerCard.defence)
        isDraw = (playerCard.defence == computerCard.defence)
        playerWins = (playerCard.defence > computerCard.defence)


    time.sleep(1)

    if isDraw:
        print("It's a tie!")
        playerDeck.append(playerCard)
        computerDeck.append(computerCard)
    elif playerWins:
        print("You win this hand!")
        score = score +1
        print("Your current score is, {}".format(score))
        playerDeck.append(playerCard)
        playerDeck.append(computerCard)
        playerTurn = True
    else:
        print("You lose this hand!")
        computerDeck.append(computerCard)
        computerDeck.append(playerCard)
        playerTurn = False

time.sleep(2)

if len(playerDeck) == 0:
    print("YOU LOSE!")
else:
    print("YOU WIN!")
    print("You scored {} points altogether!".format(score))
