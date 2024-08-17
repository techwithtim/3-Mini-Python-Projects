import random

def roll():
    min_val = 1
    max_val = 6
    return random.randint(min_val, max_val)

def print_scores(players_scores):
    print("\nCurrent Scores:")
    for idx, score in enumerate(players_scores):
        print(f"Player {idx + 1}: {score}")
    print("-" * 20)

# Get the number of players
while True:
    players = input("Enter number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players must be between 2-4.")
    else:
        print("Invalid input, try again.")

# Initialize the scores for each player
max_score = 50
players_scores = [0 for _ in range(players)]
previous_rolls = [-1 for _ in range(players)]  # To track previous rolls for penalties

# Game loop
while max(players_scores) < max_score:
    for player_idx in range(players):
        print(f"\n🎲 Player {player_idx + 1}'s turn! 🎲")
        print(f"Your total score so far is: {players_scores[player_idx]}")
        
        current_score = 0
        bonus_turn = False
        penalty_applied = False
        
        while True:
            should_roll = input("Would you like to roll the die? (y/n): ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("😢 You rolled a 1! Turn over, no points added this round.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"🎉 You rolled a {value}. Current score for this turn: {current_score}")
                
                # Bonus Roll for rolling a 6
                if value == 6:
                    print("✨ Lucky! You rolled a 6. You get a bonus roll!")
                    bonus_turn = True

                # Penalty for rolling two 1s in a row
                if previous_rolls[player_idx] == 1 and value == 1:
                    print("🚨 Uh-oh! Two 1s in a row! You lose 5 points!")
                    players_scores[player_idx] -= 5
                    penalty_applied = True

            previous_rolls[player_idx] = value  # Track the roll
            
            if not bonus_turn or penalty_applied:
                break

        # Update player's total score
        players_scores[player_idx] += current_score
        print(f"Player {player_idx + 1}'s total score is now: {players_scores[player_idx]}")

        # Special event: Bonus points for score multiple of 10
        if players_scores[player_idx] % 10 == 0 and players_scores[player_idx] != 0:
            print("🎁 Wow! Your score is a multiple of 10! You get a bonus of 5 points!")
            players_scores[player_idx] += 5

        # Check if the player has won
        if players_scores[player_idx] >= max_score:
            print(f"\n🎉🎉 Player {player_idx + 1} has won with a total score of {players_scores[player_idx]}! 🎉🎉")
            break

    print_scores(players_scores)

    # Continue the game if no winner
    if max(players_scores) < max_score:
        print("\nNext round starting!")
        continue
    else:
        # Break the outer loop if a player has won
        break
