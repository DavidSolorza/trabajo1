def calculadora_completa():
    while True:
        print("Bienvenido a la calculadora mini")
        print("\nCalculadora 100% funcional")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("Saliendo...")
            break

        if opcion in ("1", "2", "3", "4"):
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == "1":
                resultado = num1 + num2
            elif opcion == "2":
                resultado = num1 - num2
            elif opcion == "3":
                resultado = num1 * num2
            elif opcion == "4":
                if num2 == 0:
                    print("No se puede dividir por cero.")
                    continue
                resultado = num1 / num2

            print(f"El resultado es: {resultado}")
        else:
            print("Opción no válida")

calculadora_completa()


print ("Cuadrado")

lado = 5
for _ in range(lado):
    print("* " * lado)

print("Triangulo")
for i in range(1, lado + 1):
    print(" " * (lado - i) + "*" * (2 * i - 1))

print("Rectangulo")
lado2 = 10
for _ in range(lado):
    print("* " * lado2)

print("Triangulo rectangulo")
for i in range(1, lado + 1):
    print("* " * i)