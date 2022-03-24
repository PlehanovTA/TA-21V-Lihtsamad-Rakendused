game = [
    ".",".",".",
    ".",".",".",
    ".",".","."
]

print(game[0] + game[1] + game[2])
print(game[3] + game[4] + game[5])
print(game[6] + game[7] + game[8])

next_position = input("Please type what position: ")

if next_position == "1":
    game[0] = "X"

print(game[0] + game[1] + game[2])
print(game[3] + game[4] + game[5])
print(game[6] + game[7] + game[8])