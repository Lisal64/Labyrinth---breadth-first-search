from collections import deque


def replace_at_index(s: str, r: str, idx: int) -> str:
    return s[:idx] + r + s[idx + len(r):]


def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    num_row = len(lab)  # gathering the amount of indices
    num_column = len(lab[0])  # gathering the length of index 0 since all of them are the same length

    for row, line in enumerate(lab):
        if path:
            for element in path:
                if element[0] == row:
                    column = element[1]
                    lab[row] = replace_at_index(lab[row], 'X', column)

    print('  ', end='')  # creating a line to print the numbers on top
    for column in range(num_column):
        print(f'{column}', end=' ')
    print()
    for row in range(num_row):
        print(f'{row}', end=' ')  # printing the left side enumeration
        for column in range(num_column):
            print(lab[row][column], end=' ')  # printing the other contents of the labyrinth
        print(f'{row}')  # right side enumeration
    print('  ', end='')
    for column in range(num_column):
        print(f'{column}', end=' ')
    print('\n')


labyrinth = [
 "███████",
 "█     █",
 "█   ███",
 "█ ███ █",
 "█     █",
 "███████"
]


# maybe add constraint for size of labyrinth
def prompt_integer(message: str) -> int:
    while True:  # creating infinite loop
        user_i = input(f'{message}')
        if user_i.isdigit():
            value = int(user_i)
            break  # breaking it after valid input is given
        else:
            print('The input you provided was not an integer. Please enter an integer.')
    return value


def prompt_user_for_location(name: str) -> tuple[int, int]:
    if name == 'start':
        row_start = prompt_integer('Please enter the row you want to start in: ')
        column_start = prompt_integer('Please enter the column you want to start in: ')
        st_location = (row_start, column_start)
        return st_location
    elif name == 'end':
        row_end = prompt_integer('Please enter the row you want to end in: ')
        column_end = prompt_integer('Please enter the column you want to end in: ')
        en_location = (row_end, column_end)
        return en_location
    else:
        raise Exception('Please provide a valid argument. Either "start" or "end".')


def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    row, column = location
    if 0 <= row < len(lab) and 0 <= column < len(lab[0]):
        return lab[row][column] == ' '
    return False


def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    queue = deque([[start]])
    visited = set()
    if not is_traversable(lab, end):
        raise Exception('Please provide a valid location (on an empty space)')
    while len(queue) != 0:
        path = queue.popleft()
        last = path[-1]
        if last == end:
            return path
        if last not in visited:
            visited.add(last)
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for move in moves:
                next_t = (last[0] + move[0], last[1] + move[1])
                if is_traversable(lab, next_t):
                    queue.append(path + [next_t])


print(print_labyrinth(labyrinth))

start_location = prompt_user_for_location('start')
end_location = prompt_user_for_location('end')

print(f'Row of start: {start_location[0]}')
print(f'Column of start: {start_location[1]}')
print(f'Row of end: {end_location[0]}')
print(f'Column of end: {end_location[1]}')

o_path = bfs(labyrinth, start_location, end_location)
print(print_labyrinth(labyrinth, o_path))
