#CompareNumbers: That receives three numbers and return the max of them

''' primer opción: convierte los numeros ingresados a un array y realiza la comparación con la función "max" '''

print("Opcion 1:")
num1= int(input("Ingrese un numero:"))
num2= int(input("Ingrese otro numero:"))
num3= int(input("Ingrese un  último numero:"))
lista_Num= [num1, num2, num3]
mayor = max(lista_Num)

print("El máximo de los tres numeros ingresados es el:" ,mayor)

''' segunda opción: compara los numeros ingresados a través de la función maximo y condicional if y else'''
def maximo(n1, n2, n3):
    mayor=0
    if n1 > n2 and n1 > n3:
        mayor = n1
    elif n2 > n1 and n2 > n3:
        mayor = n2
    else:
        mayor = n3
    return mayor

print("Opcion 2:")
num1= int(input("Ingrese un numero:"))
num2= int(input("Ingrese otro numero:"))
num3= int(input("Ingrese un  último numero:"))
mayor= maximo(num1, num2, num3)

print("El mayor de los tres numeros es:" ,mayor)


