>>> #Secuencia aritmetica
... inicio = int(input("Primer número: "))
... diferencia = int(input("Diferencia: "))
... limite = int(input("Límite máximo: "))
... num = inicio
... while True:
...     print(num, end=" ")
...     num += diferencia
...     if num > limite:
...         break
... print("\nSecuencia aritmética desde", inicio, "hasta", limite)
...
Primer número: 2
Diferencia: 3
Límite máximo: 20
2 5 8 11 14 17 20
Secuencia aritmética desde 2 hasta 20
