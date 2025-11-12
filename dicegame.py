import random

# sends a random number.


def roll():
    min_value = 1
    max_value = 6
    # random.randit function or the creation of our random number.
    roll = random.randint(min_value, max_value)

    return roll


# this is where we get our number of players.
while True:
    players = input("Enter number of players (1-4): ")
    if players.isdigit():  # checks if the number is a digit/integer.
        players = int(players)  # changes the string into an integer.
        if 1 <= players <= 4:
            print("Welcome to our", players, "players")
            break
        else:
            print("Must be between 1-4 players")
    else:
        print("Invalid Format please try again")

# print(players) no ned for this it seems.

# for player scores.
max_scores = 50
player_scores = [0 for i in range(players)]

# Simulation of player turns.
while max(player_scores) < max_scores:

    # looping all our players turns, so they all get one.
    for player_index in range(players):
        # so they know their turn has started.(\n for line break)
        print("\nPlayer number", player_index + 1, "turn just started!\n")
        print("Your score is: ", player_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y/n): ")
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("Oh no! You rolled a 1!, Its someone elses turn now.")
                print("Your score has been reset to 0")
                current_score = 0  # Setting the score to 0 for when the player hits a 1
                player_scores[player_index] = 0  # resets the total score to 0
                break  # stops looping after player got a 1
            else:
                current_score += value  # adds their score t their overall current score
                print("You rolled a: ", value)

            print("Your current score is: ", current_score)

            # Calculating total scores
        player_scores[player_index] += current_score
        print("Your total score is: ", player_scores[player_index])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player number", player_index,"is the winner with a score of: ", max_score)


# dice = roll()
# print(dice)


