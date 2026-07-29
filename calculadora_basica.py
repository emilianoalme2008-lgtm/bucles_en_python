>>> #Calculadora Básica
... while True:
...     print("1.Suma 2.Resta 3.Multiplicación 4.División 5.Salir")
...     op = int(input("Opción: "))
...     if op == 5:
...         break
...     a = float(input("Primer número: "))
...     b = float(input("Segundo número: "))
...     match op:
...         case 1: print(a + b)
...         case 2: print(a - b)
...         case 3: print(a * b)
...         case 4:
...             if b != 0:
...                 print(a / b)
...             else:
...                 print("Error: división por cero")
...     resp = input("¿Desea continuar? (s/n): ").lower()
...     if resp == 'n':
...         break
...
1.Suma 2.Resta 3.Multiplicación 4.División 5.Salir
Opción: 1
Primer número: 5
Segundo número: 9
14.0
¿Desea continuar? (s/n): s
1.Suma 2.Resta 3.Multiplicación 4.División 5.Salir
Opción: 2
Primer número: 8
Segundo número: 3
5.0
¿Desea continuar? (s/n): s
1.Suma 2.Resta 3.Multiplicación 4.División 5.Salir
Opción: 3
Primer número: 9
Segundo número: 7
63.0
¿Desea continuar? (s/n): s
1.Suma 2.Resta 3.Multiplicación 4.División 5.Salir
Opción: 4
Primer número: 6
Segundo número: 3
2.0
¿Desea continuar? (s/n): n
>>>
