"""
/*
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""
from collections import defaultdict

def word_count(text: str) -> None:
    """Count the nuber of words and its repetitions in a text.
    """
    words: dict[str, int] = defaultdict(lambda: 0, {})
    # replace any non alphanumeric character with a space
    text = "".join([char if char.isalnum() else " " for char in text]).lower()
    word_count = 0
    for word in text.split():
        words[word] += 1
        word_count += 1
    print("Word count:", word_count)
    print("\n".join([f"{word}: {count}" for word, count in words.items()]))


if __name__ == "__main__":
    word_count("This is a test string. (Count) how many words are in this string?")