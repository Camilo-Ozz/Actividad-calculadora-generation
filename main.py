def addmultiplenumbers(numbers):
    """Suma todos los números de la lista."""
    return sum(numbers)


def multiplymultiplenumbers(numbers):
    """Multiplica todos los números de la lista en orden."""
    result = 1
    for num in numbers:
        result *= num
    return result


def isiteven(num):
    """Devuelve True si el número es par, False en caso contrario."""
    return isinstance(num, int) and num % 2 == 0


def isitaninteger(num):
    """Devuelve True si el número es un entero, False en caso contrario."""
    return isinstance(num, int)


def main():
    print("Hello learners!")
    print("Bienvenido a la calculadora 👩‍💻")

    cantidad = int(input("¿Cuántos números quieres ingresar? "))

    numeros = []
    for i in range(cantidad):
        num = float(input(f"Digita el número {i+1}: "))
        if num.is_integer():
            num = int(num)
        numeros.append(num)

    print("\n--- Resultados ---")
    print("Suma:", addmultiplenumbers(numeros))
    print("Multiplicación:", multiplymultiplenumbers(numeros))

    probar = float(input("\nDigita un número para probar si es par y si es entero: "))
    if probar.is_integer():
        probar = int(probar)

    print("¿Es par?:", isiteven(probar))
    print("¿Es entero?:", isitaninteger(probar))


if __name__ == "__main__":
    main()
