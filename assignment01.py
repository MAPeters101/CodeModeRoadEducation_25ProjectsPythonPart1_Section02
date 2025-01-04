print("Welcome to 1v1 battle\n")
choice = ""
player1Health = 1000
player2Health = 1000

player1 = input("Player 1, please enter your nickname: ") # add the input code needed to ask what player 1's nickname is
player2 = input("Player 2, please enter your nickname: ") # add the input code needed to ask what player 2's nickname is

# don't worry about what this while loop does yet
while choice.lower() != "no":
    # ask player 1 how much damage they want to do to player 2
    damageToPlayer2 = int(input(f"{player1}, How much damage do you want to do to {player2}? "))

    # decrease player 1's health by that amount (hint: decrement player2Health by damageToPlayer2)
    player2Health -= damageToPlayer2

    # ask player 2 how much damage they want to do to player 1
    damageToPlayer1 = int(input(f"{player2}, How much damage do you want to do to {player1}? "))

    # decrease player 1's health by that amount (hint: decrement player1Health by damageToPlayer1)
    player1Health -= damageToPlayer1

    # don't worry about the part of the program below this
    choice = input("Would you like to play again? ")

totalDamageToPlayer1 = 1000 - player1Health
totalDamageToPlayer2 = 1000 - player2Health

print(f"In total, {player1} did {totalDamageToPlayer2} to {player2}")
print(f"In total, {player2} did {totalDamageToPlayer1} to {player1}")

"""Instructor's code is wrong here:
if totalDamageToPlayer1 > totalDamageToPlayer2:
    print(f"{player1} wins!")

elif totalDamageToPlayer2 > totalDamageToPlayer1:
    print(f"{player2} wins!")
"""

if totalDamageToPlayer1 < totalDamageToPlayer2:
    print(f"{player1} wins!")

elif totalDamageToPlayer2 < totalDamageToPlayer1:
    print(f"{player2} wins!")

else:
    print("draw")

