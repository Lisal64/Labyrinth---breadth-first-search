from collections import deque


class Labyrinth:
    def __init__(self, lab: list[str]):
        self.lab = lab

    def print(self):
        num_row = len(self.lab)
        num_column = len(self.lab[0])

        print(" ", end="")
        for column in range(num_column):
            print(f"{column}", end=" ")  # end in a space to have room for the numbers
        print()
        for row in range(num_row):
            print(f'{row}', end=' ')  # printing the left side enumeration
            for column in range(num_column):
                print(self.lab[row][column], end=' ')  # printing the other contents of the labyrinth
            print(f'{row}')  # right side enumeration
        print('  ', end='')
        for column in range(num_column):
            print(f'{column}', end=' ')
        print('\n')

    @staticmethod
    def prompt_integer(message: str) -> int:
        while True:  # creating infinite loop
            user_i = input(f'{message}')
            if user_i.isdigit():
                value = int(user_i)
                break  # breaking it after valid input is given
            else:
                print('The input you provided was not an integer. Please enter an integer.')
        return value

    def prompt_user_for_location(self, name: str) -> tuple[int, int]:
        if name == 'start':
            row_start = self.prompt_integer('Please enter the row you want to start in: ')
            column_start = self.prompt_integer('Please enter the column you want to start in: ')
            st_location = (row_start, column_start)
            return st_location
        elif name == 'end':
            row_end = self.prompt_integer('Please enter the row you want to end in: ')
            column_end = self.prompt_integer('Please enter the column you want to end in: ')
            en_location = (row_end, column_end)
            return en_location
        else:
            raise Exception('Please provide a valid argument. Either "start" or "end".')

    def bfs(self, start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
        queue = deque([[start]])
        visited = set()
        if not self.is_traversable(end):
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
                    if self.is_traversable(next_t):
                        queue.append(path + [next_t])

    def is_traversable(self, location: tuple[int, int]) -> bool:
        row, column = location
        if 0 <= row < len(self.lab) and 0 <= column < len(self.lab[0]):
            return self.lab[row][column] == ' '
        return False


labyrinth = [
    "███████",
    "█     █",
    "█   ███",
    "█ ███ █",
    "█     █",
    "███████"
]

labyrinth = Labyrinth(labyrinth)
start_location = labyrinth.prompt_user_for_location('start')
end_location = labyrinth.prompt_user_for_location('end')

print(f'Row of start: {start_location[0]}')
print(f'Column of start: {start_location[1]}')
print(f'Row of end: {end_location[0]}')
print(f'Column of end: {end_location[1]}')

o_path = Labyrinth.bfs(labyrinth, start_location, end_location)
print(Labyrinth.print(labyrinth))
