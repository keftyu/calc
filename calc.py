def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str (b) + " = " + str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str (b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str (b) + " = " + str(answer))

print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Sair")

choice = input("input your choice: ")

if int(choice) == 1:
    print("Adição")
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    add(a, b)
elif int(choice) == 2:
    print("Subtração")
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    sub(a, b)
elif int(choice) == 3:
    print("Multiplicação")
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    mul(a, b)
elif int(choice) == 4:
    print("Divisão")
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    div(a, b)
else: 
    print("Encerrado")
    quit()