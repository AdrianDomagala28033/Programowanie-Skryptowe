import random

def set_ships(num_ships, board_size):
    ships = set()
    while len(ships) < num_ships:
        ship_position = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
        ships.add(ship_position)
    return ships

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def game():
    board_size = 10
    num_ships = 5
    ships = set_ships(num_ships, board_size)
    board = [['.' for _ in range(board_size)] for _ in range(board_size)]
    moves = 0

    while ships:
        print_board(board)
        try:
            row, col = map(int, input("Podaj współrzędne (wiersz, kolumna): ").split(","))
            if (row < 0 or row >= board_size) or (col < 0 or col >= board_size):
                print("Współrzędne poza zakresem. Spróbuj ponownie.")
                continue
        except ValueError:
            print("Nieprawidłowy format. Użyj formatu: wiersz, kolumna.")
            continue

        moves += 1
        if (row, col) in ships:
            print("Trafiony!")
            board[row][col] = 'X'
            ships.remove((row, col))
        else:
            print("Nietrafiony.")
            board[row][col] = 'O'

    print_board(board)
    print(f"Gratulacje! Zatopiłeś wszystkie statki w {moves} ruchach.")

if __name__ == "__main__":
    game()
