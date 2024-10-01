def obtener_numero_natural():
    while True:
        try:
            # Solicitar al usuario un número
            numero = int(input("Ingrese un número natural: "))

            # Validar si el número es positivo
            if numero <= 0:
                raise ValueError("Debe ser un número natural positivo.")

            return numero

        except ValueError as e:
            # Manejar las excepciones si el valor no es un número natural
            print(f"Entrada inválida: {e}. Por favor, intente de nuevo.")


def calcular_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores


def main():
    numero = obtener_numero_natural()  # Obtener el número validado
    divisores = calcular_divisores(numero)  # Calcular los divisores
    print(f"Los divisores de {numero} son: {divisores}")


if __name__ == "__main__":
    main()