# Desafío 2, semana 3 Informatorio: Desarrollo web. Mario Luis Fretes,Comisión 2.
# Analizador de Texto.

# Pedimos al usuario que ingrese un texto y las letras que quiere buscar
texto = input("Ingrese un texto: ")
letras = input("Ingrese 3 letras a buscar separadas por espacios: ").lower().split()

# Inicializamos un diccionario para contar la cantidad de veces que aparece cada letra
contador_letras = {letra: texto.lower().count(letra) for letra in letras}

# Obtenemos la cantidad de palabras totales del texto utilizando el método .split() y len()
cant_palabras = len(texto.split())

# Obtenemos la primera y última letra utilizando indexación
primera_letra = texto[0]
ultima_letra = texto[-1]

# Invertimos el orden del texto utilizando el paso negativo en la indexación
texto_inverso = texto[::-1]

# Verificamos si la palabra "python" está en el texto asociando el string a un booleano
palabra_python = "python" in texto.lower()
resultado_python = {True: "Sí aparece la palabra 'python' en el texto", False: "No aparece la palabra 'python' en el texto"}

# Imprimimos los resultados
print("Cantidad de veces que aparecen cada una de las letras ingresadas en el texto:")
for letra, cantidad in contador_letras.items():
    print(f"{letra}: {cantidad}")

print(f"Cantidad total de palabras en el texto: {cant_palabras}")
print(f"Primera letra del texto: {primera_letra}")
print(f"Última letra del texto: {ultima_letra}")
print(f"Texto en orden inverso: {texto_inverso}")
print(resultado_python[palabra_python])
