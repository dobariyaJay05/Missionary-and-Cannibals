# Unicode representations for emojis
missionary = '\U0001f482'  # 💂
cannibal = '\U0001f479'     # 👹
river = '\U0001f30a'        # 🌊
boat = '\U0001f6A2'         # 🚢

# Initial game state
num_missionaries_right = 3
num_cannibals_right = 3
num_missionaries_left = 0
num_cannibals_left = 0
boat_side = 'Right'


def print_game_state():
    # Construct the riverbank and boat representation using emojis
    right_bank = f"{missionary *
                    num_missionaries_right}{cannibal * num_cannibals_right}"
    left_bank = f"{missionary *
                   num_missionaries_left}{cannibal * num_cannibals_left}"
    river_with_boat = f"{river * 5}{boat}{river * 5}"

    # Print the game state
    print(f"|{right_bank}{river_with_boat}{left_bank}|")


# Display initial game state
print_game_state()

# Game loop
while True:
    # Prompt user for input (move)
    move_missionaries = int(
        input('Enter number of missionaries to move (or enter 10 to quit): '))
    if move_missionaries == 10:
        print('You Quit. Game Over!')
        break

    move_cannibals = int(input('Enter number of cannibals to move: '))

    # Validate move
    if (move_missionaries + move_cannibals) != 1 and (move_missionaries + move_cannibals) != 2:
        print('Invalid Move: You can only move 1 or 2 individuals at a time.')
        continue

    if boat_side == 'Right':
        if num_missionaries_right < move_missionaries or num_cannibals_right < move_cannibals:
            print('Invalid Move: Not enough individuals on the right bank.')
            continue

        # Update game state
        num_missionaries_right -= move_missionaries
        num_cannibals_right -= move_cannibals
        num_missionaries_left += move_missionaries
        num_cannibals_left += move_cannibals
        boat_side = 'Left'
    else:
        if num_missionaries_left < move_missionaries or num_cannibals_left < move_cannibals:
            print('Invalid Move: Not enough individuals on the left bank.')
            continue

        # Update game state
        num_missionaries_left -= move_missionaries
        num_cannibals_left -= move_cannibals
        num_missionaries_right += move_missionaries
        num_cannibals_right += move_cannibals
        boat_side = 'Right'

    # Display updated game state after move
    print_game_state()

    # Check win/lose conditions
    if (num_missionaries_right < num_cannibals_right and num_missionaries_right > 0) or (num_missionaries_left < num_cannibals_left and num_missionaries_left > 0):
        print('You Lose. Cannibals ate the missionaries!')
        break

    if num_missionaries_left == 3 and num_cannibals_left == 3:
        print('Congratulations! You Win!')
        break
