def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

def main():
    print("Bienvenido a la calculadora básica")
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    try:
        opcion = int(input("Ingrese el número de la operación (1-4): "))
        if opcion not in [1, 2, 3, 4]:
            print("Opción no válida.")
            return

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == 2:
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == 3:
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == 4:
            print(f"Resultado: {division(num1, num2)}")
        
        input("Presione una tecla para finalizar...")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese números.")

if __name__ == "__main__":
    main()