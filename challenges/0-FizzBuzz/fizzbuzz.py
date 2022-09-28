"""
 * Reto #0
 * EL FAMOSO "FIZZ BUZZ"
 * Fecha publicación enunciado: 27/12/21
 * Fecha publicación resolución: 03/01/22
 * Dificultad: FÁCIL
 * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a N (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *
"""
def fizzbuzz(N):
    for idx in range(1, N+1):
        if idx % 3 == 0 and idx % 5 == 0:
            print("fizzbuzz")
        elif idx % 3 == 0:
            print("fizz")
        elif idx % 5 == 0:
            print("buzz")
        else:
            print(idx)

if __name__ == "__main__":
    fizzbuzz(100)