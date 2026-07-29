>>> #Contador de digitos
... num = int(input("Número entero: "))
... if num == 0:
...     digitos = 1
... else:
...     digitos = 0
...     if num < 0:
...         num = abs(num)
...     while num > 0:
...         num //= 10
...         digitos += 1
... print("El número tiene", digitos, "dígitos")
...
Número entero: 12345
El número tiene 5 dígitos
>>> 0
0
>>> -7
-7
>>> #Contador de digitos
... num = int(input("Número entero: "))
... if num == 0:
...     digitos = 1
... else:
...     digitos = 0
...     if num < 0:
...         num = abs(num)
...     while num > 0:
...         num //= 10
...         digitos += 1
... print("El número tiene", digitos, "dígitos")
...
Número entero: 0
El número tiene 1 dígitos
>>>
>>> #Contador de digitos
... num = int(input("Número entero: "))
... if num == 0:
...     digitos = 1
... else:
...     digitos = 0
...     if num < 0:
...         num = abs(num)
...     while num > 0:
...         num //= 10
...         digitos += 1
... print("El número tiene", digitos, "dígitos")
...
Número entero: -7
El número tiene 1 dígitos
