import random

MIN_BOARD_SIZE = 5
MAX_BOARD_SIZE = 16
DEFAULT_BOARD_SIZE = 10
DEFAULT_NAME = "Инкогнито"
DEFAULT_AI_NAME = "Супер мозг"
DEFAULT_NAME_SIZE = 32
AIRCRAFT_CARRIER = 5
BATTLESHIP = 4
CRUISER = 3
DESTROYER = 2
SUBMARINE = 1
WARSHIPS_LIST = [AIRCRAFT_CARRIER, BATTLESHIP, CRUISER, DESTROYER, SUBMARINE]
OCCUPANCY = 0.2

class Warship:
    def __init__(self):
        self.__is_destroyed = False
        self.__position = []
        self.__category = None
        self.__size = None

    @property
    def is_destroyed(self):
        return self.__is_destroyed
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, positions_list):
        self.__position = positions_list
        return
    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, new_category):
        if new_category in WARSHIPS_LIST:
            self.__category = new_category
            self.__size = new_category
        return
    @property
    def size(self):
        return self.__size

class Aircraft_carrier(Warship):
    def __init__(self):
        super().__init__()
        self.__size = AIRCRAFT_CARRIER
        self.__category = AIRCRAFT_CARRIER

class Battleship(Warship):
    def __init__(self):
        super().__init__()
        self.__size = BATTLESHIP
        self.__category = BATTLESHIP

class Cruiser(Warship):
    def __init__(self):
        super().__init__()
        self.__size = CRUISER
        self.__category = CRUISER

class Destroyer(Warship):
    def __init__(self):
        super().__init__()
        self.__size = Destroyer
        self.__category = Destroyer

class Submarine(Warship):
    def __init__(self):
        super().__init__()
        self.__size = Submarine
        self.__category = Submarine

class Player:
    def __init__(self, name=DEFAULT_NAME):
        if not name or not isinstance(name, str):
            name = DEFAULT_NAME
        if len(name) > DEFAULT_NAME_SIZE:
            name = name[:DEFAULT_NAME_SIZE]
        self.name = name
        self.ships = []

    def is_ready(self):
        if len(self.ships) == 0:
            return False
        return True

class MicroAI(Player):
    def __init__(self, name="") -> None:
        if not name or not isinstance(name, str):
            name = DEFAULT_AI_NAME
        super().__init__(name)

    def make_a_move(self, board):
        x = random.randint(0, board.size -1)
        y = random.randint(0, board.size -1)
        return (x, y)

class GameBoard:
    def __init__(self, size=DEFAULT_BOARD_SIZE) -> None:
        if not isinstance(size, int): size = 10
        if size < MIN_BOARD_SIZE: size = 5
        if size > MAX_BOARD_SIZE: size = 16
        # Прячем размер
        self.__size = size
        # Создаем квадратное поле из пробелов
        self.__board = [[' ' for _ in range(size)] for _ in range(size)]
        return

    @property
    def size(self):
        return self.__size

    def show(self):
        print("-" * 12)
        for y in range(self.__size -1, -1, -1):
            row = "".join([self.__board[x][y] for x in range(self.__size)])
            print(f"|{row}|")
        print("-" * 12)
        return

    def is_avialable_cell(self, x1, y1, x2, y2):
        '''
        Определяет свободно ли пространство вокруг клетки x1, y1. Исключая из диапазона координату x2, y2
        '''
        # Проверяем, попадают ли координаты-аргументы в игровое поле
        if not (0 <= x1 <= self.__size - 1 and 0 <= y1 <= self.__size - 1):
            return False
        cells_row = []
        # Проверить на данных 0 2 0 1
        for y in [y1 - 1, y1, y1 + 1]:
            if 0 <= y <= self.__size - 1:
                # cells_row = [self.__board[x][y] for x in [x1 - 1, x1, x1 + 1] if (0 <= x <= self.__size - 1) and (x != x2 and y != y2)]
                for x in [x1 - 1, x1, x1 + 1]:
                    if (0 <= x <= self.__size - 1) and (x != x2 and y != y2):
                        cells_row.append(self.__board[x][y])
            if not all([cell == " " for cell in cells_row]):
                return False
        return True

    def auto_build_warship(self, warship_catigory):
        '''
        Размещает заданный корабль на поле случайно.
        Аргумент: тип размещаемого корабля
        Возвращает объект класса warship с новыми координатами.
        Или None, если что-то пошло не так.
        '''
        if not isinstance(warship_catigory, int) or warship_catigory not in WARSHIPS_LIST:
            return None
        new_warship = Warship()
        new_warship.category = warship_catigory
        # Список уже проверенных координат
        verified_coords = []
        # Пока не проверим все координаты игрового поля
        while len(verified_coords) < self.__size ** 2:
            # Обнуляем список координат корабля
            points = []
            x, y = -1, -1
            # Определяем ориентацию корабля: по горизонтали или вертикали
            horizontal = random.choice([True, False])
            # Проверяем ориентацию, чтобы "отодвинуться" от края
            if horizontal:
                # Случайная стартовая точка - от 0 до размер поля минус размер корабля
                start_point_x = random.randint(0, (self.__size - 1) - new_warship.size)
                # А по вертикали от 0 до размера поля
                start_point_y = random.randint(0, self.__size - 1)
            else:
                # По горизонтали от 0 до размера поля
                start_point_x = random.randint(0, self.__size - 1)
                # А по вертикали от 0 до размера поля минус размер корабля
                start_point_y = random.randint(0, (self.__size - 1) - new_warship.size)
            # Цикл по всей длине корабля
            for c in range(new_warship.size):
                # если свободна область вокруг случайной координаты, исключая из проверки предыдущую координату
                if self.is_avialable_cell(start_point_x, start_point_y, x, y):
                    # Запоминаем координаты
                    x, y = start_point_x, start_point_y
                    # Сохраняем координату
                    points.append((x, y))
                else: # Если область вокруг координаты занята
                    # Вносим в список проверенных
                    verified_coords.append((x, y))
                    # И уходим в большой цикл
                    break
                if horizontal:
                    start_point_x += 1
                else:
                    start_point_y += 1
            # Проверяем, заполнились ли все координаты по размеру корабля
            if (len(points) == new_warship.size):
                # Записываем координаты в корабль
                new_warship.position = points
                # Занимаем клетку
                for point in points:
                    x, y = point
                    self.__board[x][y] = str(new_warship.category)
                # Возвращаем
                return new_warship
        return None

    def auto_building(self):
        # Вычисляем сколько полей взять под корабли
        # 20% от размера поля.
        empty_size = int(OCCUPANCY * (self.__size ** 2))
        # Определяем пропорцию кораблей разного класса
        # Определяем количество самых мелких кораблей, зависит от размера поля
        number = (self.__size // 4) + 2
        # Начинаем с подводных лодок
        ship_category = SUBMARINE
        # Список кораблей    
        warships = []
        # Пока хватает места под размер кораблей
        while empty_size > ship_category:
            # Заказываем корабль
            for c in range(number):
                warships.append(self.auto_build_warship(ship_category))
                # Место заняли
                empty_size -= ship_category
            # Повышаем ранг кораблей
            ship_category += 1
            # Уменьшаем количество кораблей этого типа
            number -= 1
        return warships
