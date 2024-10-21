﻿# Описание

В скрипте реализуются игровые поля и расстановка кораблей классической игры "Морской бой".

## Описание структуры классов

### class Warship

Содержит три свойства, с соответствующими геттерами и сеттерами:
- __position - список кортежей с координатами, занятыми кораблем.
- __category - класс корабля: подводная лодка, эсминец, крейсер, линкор, авианосец.
- __size - сколько клеток должен занимать на поле.

#### class Aircraft_carrier(Warship)

Наследует классу Warship. Содержит значения для кораблей категории "авианосец".

#### class Battleship(Warship)

Наследует классу Warship. Содержит значения для кораблей категории "линкор".

#### class Cruiser(Warship)

Наследует классу Warship. Содержит значения для кораблей категории "крейсер".

#### class Destroyer(Warship)

Наследует классу Warship. Содержит значения для кораблей категории "эсминец".

#### class Submarine(Warship)

Наследует классу Warship. Содержит значения для кораблей категории "подводная лодка".

### class Player

Содержит два метода:
- name - имя игрока.
- ships - список кораблей-объектов класса "Warship".

### class MicroAI(Player)

Наследует классу Player. Предназначен для игрока-за-компьютер.
Дополнительно описан метод:
- make_a_move - определяет выбор координат для атаки.

### class GameBoard

Класс игрового поля. Реализует поле заданной размерности и методы автоматического распределения кораблей.
Определены методы:
- __size - определяет размер квадратного поля. Значение задается параметром конструктора.
- __board - список списков, реализующий игровое поле, где пробел (" ") - свободное поле, а число - часть корабля соответствующего класса-размера.
- def show - метод для вывода поля на экран.
- def is_avialable_cell - метод определяет, свободно ли поле с заданными координатами для размещения корабля.
- def auto_build_warship - метод, размещающий корабль заданного класса на игровом поле.
- def auto_building - метод, автоматически заполняющий игровое поле всеми классами кораблей. Количесвто кораблей разного класса определяется размером игрового поля.

## Описание тестового скрипта

В скрипте определяются два игровых поля - объекты класса GameBoard, и два игрока: User - объект класса Player и opponent - объект класса MicroAI.
Для объектов user и opponent тестируем заполнение имени по умолчанию, и проверяем размер поля по-умолчанию.
Затем для этих же объектов заполняем метод ships, присваивая им результат методов:
- user_board.auto_building() для объекта user;
- opponent_board.auto_building() для объекта opponent.
Проверяем количество созданных кораблей для user и выводим на экран игровое поле user_board.
Затем также проверяем количество кораблей, созданных для opponent, выводим на экран игровое поле opponent_board.