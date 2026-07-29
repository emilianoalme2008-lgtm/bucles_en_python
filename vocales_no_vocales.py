>>> #Vocales / No Vocales
... while True:
...     letra = input("Ingrese letra (espacio termina): ")
...     if letra == " ":
...         break
...     letra = letra.lower()
...     if letra in "aeiou":
...         print("Vocal")
...     else:
...         print("Consonante")
... print("Programa finalizado")
...
Ingrese letra (espacio termina): a
Vocal
Ingrese letra (espacio termina): h
Consonante
Ingrese letra (espacio termina):
Programa finalizado
