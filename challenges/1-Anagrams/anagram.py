"""
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""
def is_anagram(word1: str, word2: str) -> bool:
    if word1.lower() == word2.lower():
        return False
    return sorted(word1.lower()) == sorted(word2.lower())

if __name__ == "__main__":
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("car", "car", False),
        ("car", "Arc", True),
    ]
    for word1, word2, result in tests:
        assert is_anagram(word1, word2) == result
    print("Tests OK")