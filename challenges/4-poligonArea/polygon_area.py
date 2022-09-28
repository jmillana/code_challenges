"""
/*
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculates the area of the polygon

        Returns:
            float: Polygon's area
        """
        pass

    def print_area(self) -> None:
        """Prints the area of the polygon
        """
        print(f"Area of the {self.__class__.__name__.lower()}: {self.area()}")

class Triangle(Polygon):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return (self.base * self.height) / 2

class Square(Polygon):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2

class Rectangle(Polygon):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return self.base * self.height

def polygon_area(polygon: Polygon) -> float:
    polygon.print_area()
    return polygon.area()

if __name__ == "__main__":
    polygon_area(Triangle(3, 4))
    polygon_area(Rectangle(3, 4))
    polygon_area(Square(3))