import random

#--------------------КЛАСС ИГРОКА--------------------

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.inventory = []
        self.has_key = False

    def move(self, dx, dy, maze_width, maze_height):
        """Перемещение игрока по полю."""
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < maze_width and 0 <= new_y < maze_height:
            self.x = new_x
            self.y = new_y
            return True
        else:
            print("Вы уперлись в границу лабиринта.")
            return False

    def add_item(self, item):
        """Добавление предмета в инвентарь."""
        self.inventory.append(item)
        print(f"Добавлен предмет: {item}")
        if item == "волшебный ключ":
            self.has_key = True

    def add_items(self, items):
        """Добавление нескольких предметов."""
        self.inventory.extend(items)
        print(f"Добавлены предметы: {items}")
        if "волшебный ключ" in items:
            self.has_key = True

    def remove_item(self, item):
        """Удаляет указанный предмет из инвентаря."""
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"Удален предмет: {item}")
            if item == "волшебный ключ":
                self.has_key = False
            return True
        return False

    def use_last_item(self):
        """Использовать последний предмет в инвентаре."""
        if self.inventory:
            item = self.inventory.pop()
            print(f"Использован последний предмет: {item}")
            if item == "волшебный ключ":
                self.has_key = False
            return item
        return None

    def sort_inventory(self):
        """Сортировка инвентаря по длине названия предмета."""
        self.inventory.sort(key=lambda x: len(x))
        print("Инвентарь отсортирован по длине названия.")

    def reverse_inventory(self):
        """Сортировка предметов инвентаря в обратном порядке."""
        self.inventory.reverse()
        print("Инвентарь перевернут.")

    def find_item_index(self, item):
        """Ищет предмет в инвентаре и возвращает его индекс или -1."""
        try:
            idx = self.inventory.index(item)
            print(f"Предмет '{item}' найден в позиции {idx}")
            return idx
        except ValueError:
            print(f"Предмет '{item}' не найден в инвентаре.")
            return -1

    def has_item(self, item):
        """Проверяет, есть ли предмет в инвентаре."""
        found = item in self.inventory
        status = "есть" if found else "нет"
        print(f"У вас {status}: {item}")
        return found

    def take_damage(self, amount):
        """Получить урон."""
        self.health = max(0, self.health - amount)
        print(f"Получено урона: {amount}. Здоровье: {self.health}")
        return self.health > 0



#--------------------КЛАСС ЛАБИРИНТА--------------------


class Maze:

    ROOM_TYPES = {
        'empty': '.',
        'chest': 'C',
        'trap': 'T',
        'monster': 'M',
        'key': 'K',
        'portal': 'P'
    }

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        self.visited = []
        self.key_room = None
        self.portal_room = None
        self.generate_maze()

    def generate_maze(self):
        """Создание матрицы и размешение комнат лабиринта."""
        self.grid = [['empty' for _ in range(self.width)]
                     for _ in range(self.height)]
        self.visited = [[False for _ in range(self.width)]
                        for _ in range(self.height)]

        rooms_to_place = [
            ('chest', 3),
            ('trap', 2),
            ('monster', 2),
        ]

        for room_type, count in rooms_to_place:
            for _ in range(count):
                x, y = self.get_random_empty_position()
                self.grid[y][x] = room_type

        # Размещаем ключ
        key_x, key_y = self.get_random_empty_position()
        self.grid[key_y][key_x] = 'key'
        self.key_room = (key_x, key_y)

        # Размещаем портал
        portal_x, portal_y = self.get_random_empty_position()
        self.grid[portal_y][portal_x] = 'portal'
        self.portal_room = (portal_x, portal_y)

        # Начальная комната
        self.visited[0][0] = True

    def get_random_empty_position(self):
        """Находит случайную пустую клетку (не стартовая)."""
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.grid[y][x] == 'empty' and (x, y) != (0, 0):
                return x, y

    def mark_visited(self, x, y):
        self.visited[y][x] = True

    def is_visited(self, x, y):
        return self.visited[y][x]

    def get_room_type(self, x, y):
        return self.grid[y][x]

    def display(self, player_x, player_y, quiet=True):
        """Отображение поля."""
        print("\n" + "=" * (4 * self.width))
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if x == player_x and y == player_y:
                    row.append("!")
                elif quiet and not self.is_visited(x, y):
                    row.append("?")
                else:
                    room_type = self.get_room_type(x, y)
                    row.append(self.ROOM_TYPES[room_type])
            print(" ".join(row))
        print("=" * (4 * self.width))



#--------------------КЛАСС ИГРЫ--------------------

class Game:

    def __init__(self, width=5, height=5):
        self.maze = Maze(width, height)
        self.player = Player(0, 0)
        self.game_over = False
        self.win = False

    def handle_room_event(self):
        self.maze.mark_visited(self.player.x, self.player.y)
        room = self.maze.get_room_type(self.player.x, self.player.y)

        if room == 'empty':
            print("Пустая комната. Ничего не происходит.")

        elif room == 'chest':
            treasures = [
                ["золотая монета"],
                ["магический кристалл"],
                ["древний свиток"],
                ["серебряный кулон"],
                ["монета", "камень удачи"],
                ["свиток огня", "зелье лечения"]
            ]
            found_items = random.choice(treasures)
            print(f"Вы нашли сундук! Получены предметы: {found_items}")
            if len(found_items) == 1:
                self.player.add_item(found_items[0])
            else:
                self.player.add_items(found_items)
            self.maze.grid[self.player.y][self.player.x] = 'empty'

        elif room == 'trap':
            print("Вы наступили на ловушку. Минус 20 очков здоровья.")
            if not self.player.take_damage(20):
                print("Вы погибли на ловушке.")
                self.game_over = True

        elif room == 'monster':
            print("На вас напал монстр. Минус 30 очков здоровья.")
            if not self.player.take_damage(30):
                print("Монстр сразил вас.")
                self.game_over = True

        elif room == 'key':
            print("Вы нашли волшебный ключ. Можно активировать портал - Ура.")
            self.player.add_item("волшебный ключ")
            self.maze.grid[self.player.y][self.player.x] = 'empty'

        elif room == 'portal':
            if self.player.has_key:
                print("Вы используете ключ и активируете портал. Победа!")
                self.win = True
                self.game_over = True
            else:
                print("Это портал, но у вас к сожалению нет ключа.")

    def show_status(self):
        """Состояние игрока."""
        print(f"\nПозиция: ({self.player.x}, {self.player.y})")
        print(f"Здоровье: {self.player.health}")
        print(f"Инвентарь ({len(self.player.inventory)}): {self.player.inventory}")
        print(f"Ключ: {'есть' if self.player.has_key else 'нет'}")

    def player_actions(self):
        """Обработка действий игрока."""
        print("\nДоступные действия:")
        print("W / A / S / D - Двигаться")
        print("2. Показать инвентарь")
        print("3. Отсортировать инвентарь")
        print("4. Перевернуть инвентарь")
        print("5. Найти предмет в инвентаре")
        print("6. Проверить наличие предмета")
        print("7. Выбросить предмет")
        print("8. Использовать последний предмет")
        print("9. Показать карту")
        print("0. Выйти из игры")

        choice = input("Выберите действие (или WASD): ").strip().lower()

        if choice in ['w', 'a', 's', 'd']:
            moves = {
                'w': (0, -1),
                'a': (-1, 0),
                's': (0, 1),
                'd': (1, 0)
            }
            dx, dy = moves[choice]
            if self.player.move(dx, dy, self.maze.width, self.maze.height):
                self.handle_room_event()

        elif choice == '2':
            print(f"\nИнвентарь: {self.player.inventory}")

        elif choice == '3':
            self.player.sort_inventory()

        elif choice == '4':
            self.player.reverse_inventory()

        elif choice == '5':
            item = input("Введите название предмета для поиска: ")
            self.player.find_item_index(item)

        elif choice == '6':
            item = input("Введите название предмета для проверки: ")
            self.player.has_item(item)

        elif choice == '7':
            item = input("Введите название предмета для удаления: ")
            if self.player.remove_item(item):
                print("Предмет удален.")
            else:
                print("Такой предмет не найден.")

        elif choice == '8':
            used_item = self.player.use_last_item()
            if used_item:
                print(f"Вы использовали: {used_item}")
            else:
                print("Инвентарь пуст.")

        elif choice == '9':
            self.maze.display(self.player.x, self.player.y, quiet=True)

        elif choice == '0':
            self.game_over = True

        else:
            print("Неверный выбор.")

    def start(self):
        """Запускает основной игровой цикл."""
        print("Добро пожаловать в лабиринт!")
        print("Найдите ключ и доберитесь до портала.")
        print("Обозначения: ! - игрок, . - пусто, C - сундук, T - ловушка, M - монстр, K - ключ, P - портал")
        print("Непосещённые клетки отображаются как '?'.\n")

        while not self.game_over:
            self.show_status()
            self.maze.display(self.player.x, self.player.y, quiet=True)
            self.player_actions()

            if self.player.health <= 0:
                self.game_over = True
                print("Смерть")

        if self.win:
            print("Поздравляю! Вы прошли лабиринт!")

        print("\nСпасибо за игру!")


#--------------------ЗАПУСК ИГРЫ--------------------

if __name__ == "__main__":
    game = Game(5, 5)
    game.start()
