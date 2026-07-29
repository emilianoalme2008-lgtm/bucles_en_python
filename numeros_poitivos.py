>>> #Media de numeros positivos
... suma = 0
... contador = 0
... while True:
...     num = float(input("Número positivo (negativo sale): "))
...     if num < 0:
...         break
...     if num > 0:
...         suma += num
...         contador += 1
... if contador > 0:
...     media = suma / contador
...     print("Media:", media)
... else:
...     print("No se ingresaron positivos")
...
Número positivo (negativo sale): 10
Número positivo (negativo sale): 20
Número positivo (negativo sale): 30
Número positivo (negativo sale): -1
Media: 20.0
>>>
>>> #Media de numeros positivos
... suma = 0
... contador = 0
... while True:
...     num = float(input("Número positivo (negativo sale): "))
...     if num < 0:
...         break
...     if num > 0:
...         suma += num
...         contador += 1
... if contador > 0:
...     media = suma / contador
...     print("Media:", media)
... else:
...     print("No se ingresaron positivos")
...
Número positivo (negativo sale): -5
No se ingresaron positivos
