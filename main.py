def calculadora():
    print("Calculadora 50% funcional")
    print("1. Sumar")
    print("2. Restar")

    opcion = input("Elige una opción (1/2): ")

    if opcion in ("1", "2"):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
        else:
            resultado = num1 - num2

        print(f"El resultado es: {resultado}")
    else:
        print("Opción no válida")

calculadora()

print ("Cuadrado")

lado = 5
for _ in range(lado):
    print("* " * lado)

print("Triangulo")
for i in range(1, lado + 1):
    print(" " * (lado - i) + "*" * (2 * i - 1))