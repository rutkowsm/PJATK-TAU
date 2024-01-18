import os
import msvcrt
import random


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def random_positions_on_edge(board_size, taken_edges):
    edges = ["N", "S", "W", "E"]
    for edge in taken_edges:
        edges.remove(edge)

    selected_edge = random.choice(edges)
    if selected_edge in ["N", "S"]:
        x = random.randint(0, board_size - 1)
        y = 0 if selected_edge == "N" else board_size - 1
    else:
        x = 0 if selected_edge == "W" else board_size - 1
        y = random.randint(0, board_size - 1)
    return x, y


def generate_obstacles(board_size, obstacles_number, start_pos, end_pos):
    obstacles = set()
    while len(obstacles) < obstacles_number:
        obstacle_x = random.randint(0, board_size - 1)
        obstacle_y = random.randint(0, board_size - 1)
        if (obstacle_x, obstacle_y) != start_pos and (obstacle_x, obstacle_y) != end_pos:
            obstacles.add((obstacle_x, obstacle_y))
    return obstacles


def move_player(current_x, current_y, key, board_size, obstacles):
    new_x, new_y = current_x, current_y
    if key == b'H' and current_x > 0:  # Strzałka w górę
        new_x -= 1
    elif key == b'P' and current_x < board_size - 1:  # Strzałka w dół
        new_x += 1
    elif key == b'K' and current_y > 0:  # Strzałka w lewo
        new_y -= 1
    elif key == b'M' and current_y < board_size - 1:  # Strzałka w prawo
        new_y += 1

    if 0 <= new_x < board_size and 0 <= new_y < board_size and (new_x, new_y) not in obstacles:
        return new_x, new_y
    return current_x, current_y


def is_game_over(player_pos, end_pos):
    return player_pos == end_pos


def main():
    board_size = 10
    x, y = random_positions_on_edge(board_size, [])
    taken_edge = ["N", "E", "W"] if y == 0 else ["S", "E", "W"] if y == board_size - 1 else ["W", "N", "S"] if x == 0 else ["E", "N", "S"]
    end_x, end_y = random_positions_on_edge(board_size, taken_edge)
    obstacles = generate_obstacles(board_size, 20, (x, y), (end_x, end_y))

    while True:
        clear_screen()
        for i in range(board_size):
            for j in range(board_size):
                print("X " if (i, j) == (x, y) else "O " if (i, j) in obstacles else "* " if (i, j) == (end_x, end_y) else ". ", end="")
            print()

        key = msvcrt.getch()
        if key in [b'\x00', b'\xe0']:
            key = msvcrt.getch()
            x, y = move_player(x, y, key, board_size, obstacles)

        if is_game_over((x, y), (end_x, end_y)):
            print("Gratulacje! Dotarłeś do mety!")
            break

        if key == b'r':
            return True
        if key == b'q':
            return False

while main():
    pass
