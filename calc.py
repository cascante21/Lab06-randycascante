def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input
    try:
        result = callback(num1, num2)
        print("Resultado:", result)
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except Exception as e:
        print(f"Error: {e}")

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

operations = {
    '+': lambda x, y: suma(x, y),
    '-': lambda x, y: resta(x, y),
    '*': lambda x, y: multiplicacion(x, y),
    '/': lambda x, y: division(x, y)
}

def main():
    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")

        if user_input[2] in operations:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o escriba 'exit' para salir.")

if __name__ == "__main__":
    main()
