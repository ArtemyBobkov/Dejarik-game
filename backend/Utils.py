from typing import Tuple, List, Union, Callable

import numpy as np

from Figures.Fighter import Fighter
from Figures.Figure import Figure
from Figures.Guard import Guard
from Figures.Hunter import Hunter
from Figures.Pet import Pet

NUM_SECTORS = 11
FIGURE_SEPARATOR = ':'
FIGURE_X_NAME = {Hunter: "H", Guard: "G", Fighter: "F", Pet: "P"}
NAME_X_FIGURE = {value: key for key, value in FIGURE_X_NAME}


def find_possible_moves(cell: Point) -> List[Point]:
    """
    Поиск возможных ячеек для окончания движения
    :param cell: начало движения
    :return: список доступных ходов
    """
    if cell.radius == 0:
        return [*map(Point, *np.array(np.arange(0, NUM_SECTORS), np.zeros(NUM_SECTORS)).T),
                *map(Point, *np.array(np.arange(0, NUM_SECTORS), np.ones(NUM_SECTORS)).T)]

    possible_moves = [
        Point(0, 0),
        Point(3 - cell.radius, (cell.sector + NUM_SECTORS - 1) % NUM_SECTORS),
        Point(3 - cell.radius, (cell.sector + NUM_SECTORS + 1) % NUM_SECTORS)
    ]
    if cell.radius == 2:
        possible_moves.extend([(cell.radius, (cell.sector + NUM_SECTORS - 2) % NUM_SECTORS),
                               (cell.radius, (cell.sector + 2) % NUM_SECTORS)])
    else:
        # пройти можно с 1 на 1 в любую точку через центр
        possible_moves.extend(np.delete(np.arange(0, NUM_SECTORS), cell.sector))
    return possible_moves


def cells_between(cell1: Point, cell2: Point) -> List[Point]:
    """
    Промежуточные клетки, между которыми должна пройти фигура
    :param cell1: начало движения
    :param cell2: конец движения
    :return: все варианты промежуточных клеток
    """

    assert_correct(cell1, cells_between)
    assert_correct(cell2, cells_between)

    # проход только по орбите
    if cell1.radius == cell2.radius:
        if cell1.radius == 0:
            raise AttributeError("Невалидно переходить из дежарика в дежарик!")
        # если пройти можно только через центр поля
        if abs(cell1.sector - cell2.sector) == 1:
            return [Point(2, 0)]
        # если проход через нулевой сектор
        if abs(cell1.sector - cell2.sector) > 1:
            return [Point(cell1.radius, 0 if cell1.sector == 1 or cell2.sector == 1 else NUM_SECTORS - 1)]
        return [Point(cell1.radius, (cell1.sector + cell2.sector) // 2)]

    if cell1.radius > cell2.radius:
        cell1, cell2 = cell2, cell1

    # проход только по радиусу
    if cell2.radius - cell1.radius == 2:
        return [Point(1, cell2.sector)]
    # случай с центром и средней орбитой
    if cell1.radius == 0:
        return [
            Point(1, (cell2.sector + 1) % NUM_SECTORS),
            Point(1, (cell2.sector + NUM_SECTORS - 1) % NUM_SECTORS)
        ]
    # случай с обычным движением между орбитами
    return [
        Point(1, cell2.sector),
        Point(2, cell1.sector)
    ]


def assert_correct(cell: Point, fun: Callable):
    if cell.radius < 0 or cell.radius > 2:
        raise AssertionError(f"Invalid radius: {cell.radius} in function {fun}")
    if cell.radius == 0 and cell.sector != 0:
        raise AssertionError(f"Invalid sector {cell.sector} for radius 0 in function {fun}")
    if cell.sector < 0 or cell.sector >= NUM_SECTORS:
        raise AssertionError(f"Invalid sector {cell.sector} in function {fun}")


def near(cell1: Point, cell2: Point) -> bool:
    if cell1 == cell2:
        raise ValueError("Две ячейки в сравнении не должны быть одинаковыми!")
    if cell1.radius > cell2.radius:
        cell1, cell2 = cell2, cell1
    if cell1.radius == 0:
        return cell2.radius == 1
    return (abs(cell1.sector - cell2.sector) <= 1 or
            max(cell1.sector, cell2.sector) == NUM_SECTORS - 1 and
            min(cell1.sector, cell2.sector) == 0)


def is_winning_state(figs_1: list, figs_2: list) -> int:
    """
    Возвращает номер выигравшего игрока или 0, если никто не выигрывает
    :param figs_1: фигуры 1 игрока
    :param figs_2: фигуры 2 игрока
    :return: 0, 1 или 2
    """
    for i, figs in enumerate([figs_1, figs_2]):
        if len(figs) < 3:
            return 2 - i
        for figure in figs:
            if figure.position.radius != 1:
                break
            return i + 1
    return 0


def parse_state(state: str) -> List[List[Figure], List[Figure]]:
    figures = [[], []]
    for figure in state.split(FIGURE_SEPARATOR):
        fig_type = figure[0]
        player = int(figure[1])
        pos = int(figure[2]), int(figure[3])
        figures[player - 1].append(NAME_X_FIGURE[fig_type](pos))
    return figures
