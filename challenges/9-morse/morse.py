"""
/*
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""
import re

NATURAL_TO_MORSE = {
    "A": ".—",    "N": "—.",     "0": "—————",
    "B": "—...",  "Ñ": "——.——",  "1": ".————",
    "C": "—.—.",  "O": "———",    "2": "..———",
    "CH": "————", "P": ".——.",   "3": "...——",
    "D": "—..",   "Q": "——.—",   "4": "....—",
    "E": ".",     "R": ".—.",    "5": ".....",
    "F": "..—.",  "S": "...",    "6": "—....",
    "G": "——.",   "T": "—",      "7": "——...",
    "H": "....",  "U": "..—",    "8": "———..",
    "I": "..",    "V": "...—",   "9": "————.",
    "J": ".———",  "W": ".——",    ".": ".—.—.—",
    "K": "—.—",   "X": "—..—",   ",": "——..——",
    "L": ".—..",  "Y": "—.——",   "?": "..——..",
    "M": "——",    "Z": "——..",   "\"": ".—..—.", "/": "—..—."
}

MORSE_TO_NATURAL = {v: k for k, v in NATURAL_TO_MORSE.items()}

def encode(text: str) -> str:
    """Encode a text to morse code."""
    encoded = ""
    for word in text.split(" "):
        for letter in word:
            encoded += NATURAL_TO_MORSE[letter.upper()] + " "
        encoded += " "
    print(encoded)
    return encoded

def decode(morse: str) -> str:
    """Decode a morse code to text.
    """
    decoded = ""
    for word in morse.split("  "):
        for symbol in word.split(" "):
            if symbol:
                decoded += MORSE_TO_NATURAL[symbol]
        decoded += " "
    # Remove last space
    print(decoded)
    return decoded.strip()

def morse(text: str) -> str:
    """Encode or decode a text to morse code.
    """
    # Regex a-zA-Z in text
    if re.search(r"[a-zA-Z0-9]", text):
        return encode(text)
    else:
        return decode(text)

if __name__ == "__main__":
    phrase = "Hello world, this is a test."
    assert phrase.upper() == morse(morse(phrase))
