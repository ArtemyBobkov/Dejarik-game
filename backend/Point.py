from typing import Tuple, Union


class Point:
    """
    Точка на доске. Предполагается, что radius от 0 до 2, где
    0 - дежарик, центр поля
    1 - средняя орбита
    2 - внешняя орбита
    Круг разбит на сектора, номера sector - от 0 до NUM_SECTORS - 1.
    Фигура первого игрока расставляется на
    """

    def __init__(self, radius: Union[int, Tuple[int, int]], sector: int = None):
        """
        Конструктор по двум точкам
        :param radius: int либо Tuple из двух интов - радиус и сектор
        :param sector: сектор
        """
        if isinstance(radius, Tuple):
            self.radius = radius[0]
            self.sector = radius[1]
        else:
            self.radius = radius
            self.sector = sector

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.radius == other.radius and self.sector == other.sector
        return False

    def __ne__(self, other):
        if isinstance(other, Point):
            return not self == other
        return False
