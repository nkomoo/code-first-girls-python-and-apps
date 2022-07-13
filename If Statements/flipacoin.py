import random

def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side

choice = input('heads or tails: ')
result = flip_coin()
print('The coin landed on {}'.format(result))

if choice == result:
    print("You win!")
elif choice == "heads" or "tails":
    print("You lose")
    print(f"The coin landed on {result}")
else:
    print("Please pick either heads or tails")



"""
To finish the program you will need to add the following:
● If the random coin flip matches the choice input by the user then they win
● Otherwise if the random coin flip does not match the choice input by the user then they
lose
"""


"""
Extension: The program should show a message to 
the user if they enter a choice that isn't heads
or tails
"""