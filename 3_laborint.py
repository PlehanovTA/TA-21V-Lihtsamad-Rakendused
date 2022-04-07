import random
map = [
    [12, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 24]
]

def get_start_pos():
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] == 12:
                return y, x

start_pos_y = get_start_pos()
start_pos_x = get_start_pos()

x_columns = len(map[0])
y_rows = len(map)

def get_next_free_pos(current_pos_y, current_pos_x):
    possible_moves = []
    if current_pos_x+1 < x_columns and map[current_pos_y][current_pos_x + 1] in [1, 24]:
        print("You can go right")
        possible_moves.append((current_pos_y, current_pos_x + 1))
    
    if current_pos_y+1 < y_rows and map[current_pos_y + 1][current_pos_x] in [1, 24]:
        print("You can go bottom")
        possible_moves.append((current_pos_y + 1, current_pos_x))

    if current_pos_y-1 >= 0 and map[current_pos_y - 1][current_pos_x] in [1, 24]:
        print("You can go top")
        possible_moves.append((current_pos_y - 1, current_pos_x))

    if current_pos_x-1 >= 0 and map[current_pos_y][current_pos_x - 1] in [1, 24]:
        print("You can go left")
        possible_moves.append((current_pos_y, current_pos_x - 1))
        
    if map[current_pos_y][current_pos_x] == 24:
        print("The End")
        return False
    
    random_move = random.choice(possible_moves)
    print(random_move)
    return random_move

next_free_pos = get_next_free_pos(start_pos_y, start_pos_x)
print("Next free position is: ", next_free_pos)

while next_free_pos:
    next_free_pos = get_next_free_pos(next_free_pos[0], next_free_pos[1])
    print("Next free position is: ", next_free_pos)