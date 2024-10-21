from battleship_classes import *

user_board = GameBoard()
opponent_board = GameBoard()

user = Player()
opponent = MicroAI()

print("Тест классов")
print(f"{user.name} VS. {opponent.name} на поле {user_board.size} X {opponent_board.size}")
print("-" * 30)
user.ships = user_board.auto_building()
opponent.ships = opponent_board.auto_building()

print(f"Кораблей у {user.name} = {len(user.ships)}")
user_board.show()

print("-" * 30)

print(f"Кораблей у {opponent.name} = {len(opponent.ships)}")
opponent_board.show()

input("Нажмите Enter для завершения программы...")
