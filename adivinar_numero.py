>>> #Adivinar numero
... import random
... secreto = random.randint(1, 100)
... while True:
...     intento = int(input("Adivina (1-100): "))
...     if intento < secreto:
...         print("Demasiado bajo")
...     elif intento > secreto:
...         print("Demasiado alto")
...     else:
...         print("¡Correcto! Era", secreto)
...         break
... print("Juego terminado. El número era", secreto)
...
Adivina (1-100): 8
Demasiado bajo
Adivina (1-100): 67
Demasiado alto
Adivina (1-100): 45
Demasiado alto
Adivina (1-100): 25
Demasiado bajo
Adivina (1-100): 30
Demasiado alto
Adivina (1-100): 27
Demasiado bajo
Adivina (1-100): 28
¡Correcto! Era 28
Juego terminado. El número era 28
