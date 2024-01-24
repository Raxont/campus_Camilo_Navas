palabra=str(input("Ingrese la palabra: "))
palabra_m=palabra.lower()
if palabra==palabra[::-1]:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")