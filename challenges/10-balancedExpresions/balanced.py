"""
/*
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""

def is_balanced(expression: str) -> bool:
    """Check if the expression is balanced.
    """
    symbols = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = []
    for char in expression:
        if char in symbols or char in symbols.values():
            if char in symbols:
                stack.append(char)
            else:
                if not stack or symbols[stack.pop()] != char:
                    return False
    return not stack

if __name__ == "__main__":
    tests = [
        (is_balanced("{a + b [c] * (2x2)}}}}"), False),
        (is_balanced("{ [ a * ( c + d ) ] - 5 }"), True),
        (is_balanced("{ a * ( c + d ) ] - 5 }"), False),
        (is_balanced("{a^4 + (((ax4)}"), False),
        (is_balanced("{ [] a * ( c + d ) + ( 2 - 3 )[ - 5 ]}"), True),
        (is_balanced("{{{{{{(}}}}}}"), False),
        (is_balanced("(a"), False),
    ]
    for test, expected in tests:
        assert test == expected, f"Expected {expected} but got {test}"