import random


def Hello_game():
    print('=' * 40)
    print()
    print('*' * 5 + 'Добро пожаловать в игру крестики-нолики!' + '*' * 5)
    print()
    print('=' * 40)


def game_field_init():
    print('Поле создано.')
    return [[' ' for _ in range(3)] for _ in range(3)]


def persons_init():
    print('Введите по очереди имена игроков:')
    a = input()
    b = input()
    return a, b


def sign_init(a):
    s_per = input(
        f'Игрок {a} выберите знак, которым будете играть: (en) X or O\n>>:').upper()
    if s_per == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def board_change(board, x, y, sign):
    board[y][x] = sign
    return board


def first_move():
    return random.randint(0, 1)


def board_move_accept(board, x, y):
    return board[y][x] == ' '


def move_person(board, sign_person):
    while True:
        x, y = int(input('Введите от 0 до 2 положение по горизонтали(слева на право):\n>>:')), int(
            input('Введите от 0 до 2 положение по вертикали(сверху в низ):\n>>:'))
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Неверные координаты!\n')
            continue
        if not board_move_accept(board, x, y):
            print('Это место уже занято, выберете другое.\n')
            continue
        else:
            board = board_change(board, x, y, sign_person)
            break


def available_place(board):
    lst = list()
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                lst.append((i, j))
    return len(lst) > 0


def win(board, sign, person):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            print(f'Победил игрок {person}\n')
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            print(f'Победил игрок {person}\n')
            return True
    a, b, c = 0, 1, 2
    if board[a][a] == board[b][b] == board[c][c] == sign or board[a][c] == board[b][b] == board[c][a] == sign:
        print(f'Победил игрок {person}\n')
        return True
    if available_place(board):
        return False
    else:
        print('Ничья!\n')
        return True


def game_again():
    print('-+' * 20)
    print('Играть снова? (Y - yes, N - no)\n')
    query = input().upper()
    return query.startswith('Y')


def print_board(board):
    print('=' * 20)
    print(*[' ', 0, 1, 2], sep=' | ')
    print('- + ' * 3 + '-')
    j = 0
    for step in board:
        print(j, *step, sep=' | ', end='\n')
        print('- + ' * 3 + '-')
        j += 1
    print('=' * 20)


def main():
    Hello_game()
    person_1, person_2 = persons_init()
    print('=' * 40)
    while True:
        board = game_field_init()
        print_board(board)
        sign_per_1, sign_per_2 = sign_init(person_1)
        print('=' * 10)

        print(
            f'Игрок {person_1} играет за {sign_per_1}, игрок {person_2} играет за {sign_per_2}.')
        print('=' * 10)

        print('Определение кто будет ходит первым:')
        print('=' * 10)
        if first_move():
            print(f'Первым ходит игрок {person_1}')
            print('=' * 10)
            p = 1
        else:
            print(f'Первым ходит игрок {person_2}')
            print('=' * 10)
            p = 2

        while True:
            if p == 1:
                print_board(board)
                print(f'Ход игрока {person_1}')
                move_person(board, sign_per_1)
                p = 2
                print_board(board)
                if win(board, sign_per_1, person_1):
                    break
            else:
                print_board(board)
                print(f'Ход игрока {person_2}')
                move_person(board, sign_per_2)
                p = 1
                print_board(board)
                if win(board, sign_per_2, person_2):
                    break

        if not game_again():
            break


main()
