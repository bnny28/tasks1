from enum import Enum
import random

# Размерность поля игры
FIELD_DIMENSION = 10


# Возможные состояния игры
class GameStatus(Enum):
    IMPOSSIBLE = 1
    O_LOSES = 2
    X_LOSES = 3
    DRAW = 4
    GAME_NOT_FINISHED = 5


# Возможные значения ячеек игры
class PositionVal(Enum):
    X = 'X'
    O = 'O'
    U = '_'


class TicTacToeState:
    """
    Клас отвечающий за состояния игры
    """
    game_state: GameStatus

    def __init__(self, game_field: list[list[chr]]):
        self.set(game_field)

    def set(self, game_field: list[list[chr]]):
        """
        Set state game
        :param game_field: Game model
        :return: None
        """
        # Проверка на "невозможные" состояния (большое превышение X над O и наоборот)
        is_impossible_proportion = self._is_impossible_proportion(game_field)
        # Проверка на наличие доступных ходов
        is_has_empty_position = self._is_has_empty_position(game_field)
        # Проиграл ли компьютер
        is_loses_o = self._is_loses(game_field, PositionVal.O.value)
        # Проиграл ли человек
        is_loses_x = self._is_loses(game_field, PositionVal.X.value)
        # Сохраняем состояния
        if (is_loses_x and is_loses_o) or is_impossible_proportion:
            self.game_state = GameStatus.IMPOSSIBLE.value
        elif is_loses_o:
            self.game_state = GameStatus.O_LOSES.value
        elif is_loses_x:
            self.game_state = GameStatus.X_LOSES.value
        elif is_has_empty_position:
            self.game_state = GameStatus.GAME_NOT_FINISHED.value
        else:
            self.game_state = GameStatus.DRAW.value

    def get(self) -> GameStatus:
        """
        Get state game
        :return: None
        """
        return self.game_state

    @staticmethod
    def _is_impossible_proportion(game_field: list[list[chr]]):
        game_fields_list = list(i for j in game_field for i in j)
        return abs(game_fields_list.count(PositionVal.X.value) - game_fields_list.count(PositionVal.O.value)) > 1

    @staticmethod
    def _is_has_empty_position(game_field: list[list[chr]]):
        game_fields_list = list(i for j in game_field for i in j)
        return game_fields_list.count(PositionVal.U.value) > 0

    def _is_loses(self, game_field: list[list[chr]], c: chr):
        # Проверка на заполненность строки 5 символами подряд
        # Проверка на заполненность диагонали 5 символами подряд
        # Проверка на заполненность строки 5 символами подряд для развернутого на 90 градусов поля
        # Проверка на заполненность диагонали 5 символами подряд для развернутого на 90 градусов поля
        return self._is_row_filled(game_field, c) or \
               self._is_diagonal_filled(game_field, c) or \
               self._is_row_filled(self._turn_to_left(game_field), c) or \
               self._is_diagonal_filled(self._turn_to_left(game_field), c)

    @staticmethod
    def _is_row_filled(game_field: list[list[chr]], c: chr):
        for n in range(6):
            for m in range(6):
                sub_field = list()
                for y in range(5):
                    sub_field.append(game_field[y + m][n:n + 5])
                for row in sub_field:
                    if row == [c for _ in range(5)]:
                        return True
        return False

    @staticmethod
    def _is_diagonal_filled(game_field: list[list[chr]], c: chr):
        for n in range(6):
            for m in range(6):
                sub_field = list()
                for y in range(5):
                    sub_field.append(game_field[y + m][n:n + 5])
                diagonal_filled = True
                for row, val in enumerate(sub_field):
                    if val[row] != c:
                        diagonal_filled = False
                if diagonal_filled:
                    return diagonal_filled
        return False

    @staticmethod
    def _turn_to_left(game_field: list[list[chr]]):
        turn_field = []
        i = 0
        for _ in game_field:
            list_to_add = [item[i] for item in game_field]
            turn_field.append(list_to_add)
            i += 1
        return turn_field[::-1]


class TicTacToeDisplay:
    """
    Клас отвечающий за прорисовку поля игры
    """
    # Шаблон для заполнения
    game_template_matrix: list[str] = [
        "    0 1 2 3 4 5 6 7 8 9  ",
        "  -----------------------",
        "0 | 00 01 02 03 04 05 06 07 08 09 |",
        "1 | 10 11 12 13 14 15 16 17 18 19 |",
        "2 | 20 21 22 23 24 25 26 27 28 29 |",
        "3 | 30 31 32 33 34 35 36 37 38 39 |",
        "4 | 40 41 42 43 44 45 46 47 48 49 |",
        "5 | 50 51 52 53 54 55 56 57 58 59 |",
        "6 | 60 61 62 63 64 65 66 67 68 69 |",
        "7 | 70 71 72 73 74 75 76 77 78 79 |",
        "8 | 80 81 82 83 84 85 86 87 88 89 |",
        "9 | 90 91 92 93 94 95 96 97 98 99 |",
        "  -----------------------"
    ]

    # Заполненный шаблон на основании модели игры
    current_field_matrix: list[str]

    def __init__(self, game_field: list[list[chr]]):
        self.set(game_field)

    def set(self, game_field: list[list[chr]]):
        """
        Set game field
        :param game_field: Game model
        :return: None
        """
        self.current_field_matrix = self.game_template_matrix[:]
        for i in range(FIELD_DIMENSION):
            for j in range(FIELD_DIMENSION):
                self.current_field_matrix[i + 2] = self.current_field_matrix[i + 2].replace(f'{i}{j}',
                                                                                            game_field[i][j])

    def render(self):
        """
        Render field game
        :return: None
        """
        print()
        for i in self.current_field_matrix:
            print(i)


class AIGamer:
    """
    Клас отвечающий за игру компьютера
    """
    # Набор возможных ходов
    possible_steps = [i for i in range(100)]

    def __init__(self, game_field: list[list[chr]]):
        self._remove_impossible_steps(game_field)

    def _remove_impossible_steps(self, game_field: list[list[chr]]):
        """
        Remove impossible steps
        :param game_field: Game model
        :return: None
        """
        for i, row in enumerate(game_field):
            for j, val in enumerate(row):
                if val != PositionVal.U.value and int(f'{i}{j}') in self.possible_steps:
                    self.possible_steps.remove(int(f'{i}{j}'))

    def go_step(self, game_field: list[list[chr]], c: chr, tic_tac_state: TicTacToeState) -> list[list[chr]]:
        """
        :param game_field:  Game model
        :param c: Current symbol for step
        :param tic_tac_state: Game state
        :return: Correct Game model
        """
        self._remove_impossible_steps(game_field)
        # Цикл подбора хода, не ведущего к проигрышу
        while len(self.possible_steps) > 0:
            # Случайным образом выбираем ход из доступных
            random_index = random.randint(0, len(self.possible_steps) - 1)
            random_step = self.possible_steps[random_index]
            if random_step > 9:
                int_x, int_y = int(str(random_step)[0]), int(str(random_step)[1])
            else:
                int_x, int_y = 0, random_step
            # Устанавливаем состояние модели для выбранного хода
            game_field[int_x][int_y] = c
            tic_tac_state.set(game_field)
            # Проверка, что ход ведет к проигрышу компьютера
            if tic_tac_state.get() == GameStatus.O_LOSES.value:
                # Если остался единственный ход, то проиграли (ничего не поделать)
                if len(self.possible_steps) == 1:
                    self.possible_steps.remove(random_step)
                    print('Компьютер ходит:', int_x, int_y, sep=' ')
                    return game_field
                # Отменяем выбор проигрышного хода, удаляем его из возможных и выберем другой
                game_field[int_x][int_y] = PositionVal.U.value
                tic_tac_state.set(game_field)
                self.possible_steps.remove(random_step)
            else:
                # Ходим, если ход не проигрышный
                print('Компьютер ходит:', int_x, int_y, sep=' ')
                return game_field
        return game_field


class TicTacToe:
    """
    Клас отвечающий за игру (главный)
    """
    # Модель игры
    game_field: list[list[chr]] = []
    # Текущий символ для хода (O или X)
    current_symbol: PositionVal

    def __init__(self):
        # Закоментирована возможность внести первоначальное состояние модели игры при старте
        # input_string = list(input('> ').strip()[:FIELD_DIMENSION * FIELD_DIMENSION])
        input_string = list(['_'] * FIELD_DIMENSION * FIELD_DIMENSION)
        self.set_game_field(input_string)
        self.current_symbol = PositionVal.X

    def set_game_field(self, input_string: list[chr]):
        """
        Set game model
        :param input_string: Input list of char
        :return: None
        """
        for i in range(FIELD_DIMENSION):
            fields_row = []
            for j in range(FIELD_DIMENSION):
                idx = i * FIELD_DIMENSION + j
                if input_string[idx] in [PositionVal.O.value, PositionVal.X.value, PositionVal.U.value]:
                    fields_row.append(input_string[idx])
                else:
                    raise IOError('Ошибка ввода')
            self.game_field.append(fields_row)

    def go_game_step(self):
        """
        User input for step and test legal input
        :return: None
        """
        while True:
            input_line = input('Ваш ход: ')
            if self.is_legal_input(input_line):
                break

    def is_legal_input(self, input_line: str) -> bool:
        """
        Test legal user input
        :param input_line: Input string
        :return: isLegal
        """
        if len(input_line.split()) > 1:
            x, y = input_line.split()
            if x.strip().isdigit() and y.strip().isdigit():
                int_x = int(x.strip())
                int_y = int(y.strip())
                if int_x in [i for i in range(FIELD_DIMENSION)] and int_y in [i for i in range(FIELD_DIMENSION)]:
                    if self.game_field[int_x][int_y] == PositionVal.U.value:
                        self.game_field[int_x][int_y] = self.current_symbol.value
                        return True
                    else:
                        print("Эта ячейка занята! Выберите другую!")
                        return False
                else:
                    print(f"Каждая из координат должна быть между 0 и {FIELD_DIMENSION - 1}!")
                    return False
            else:
                print("Нужно вводить только числа!")
                return False
        else:
            print("Введите 2 координаты через пробел!")
            return False

    def main(self):
        """
        Запуск основного цикла игры
        :return: None
        """
        tic_tac_display = TicTacToeDisplay(self.game_field)
        tic_tac_display.render()
        tic_tac_state = TicTacToeState(self.game_field)
        ai_gamer = AIGamer(self.game_field)

        # Играем пока есть доступные ходы
        while tic_tac_state.get() == GameStatus.GAME_NOT_FINISHED.value:
            if self.current_symbol == PositionVal.X:
                # Если ход игрока
                self.go_game_step()
                tic_tac_state.set(self.game_field)
            else:
                # Если ход компьютера
                self.game_field = ai_gamer.go_step(self.game_field, PositionVal.O.value, tic_tac_state)
            # Рисуем экран игры
            tic_tac_display.set(self.game_field)
            tic_tac_display.render()
            # Меняем следующий символ (X или O)
            self.current_symbol = PositionVal.O if self.current_symbol == PositionVal.X else PositionVal.X

        # Вывод результата игры
        if tic_tac_state.get() == GameStatus.IMPOSSIBLE.value:
            print('Невозможная комбинация')
        elif tic_tac_state.get() == GameStatus.X_LOSES.value:
            print('Вы проиграли :(')
        elif tic_tac_state.get() == GameStatus.O_LOSES.value:
            print('Вы выиграли :)')
        elif tic_tac_state.get() == GameStatus.GAME_NOT_FINISHED.value:
            print('Игра может продолжаться')
        else:
            print('Ходов больше нет')


if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.main()
