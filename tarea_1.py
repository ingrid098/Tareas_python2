lista_libros = [
    {"id": 1, "libro": "EL PSICOANALISTA EN LA MIRA", "autor": "JOHN KATZENBACH",
        "ISBN": 9786287634275, "paginas": 422, "precio": 72.000, "categoria": "Literatura"},
    {"id": 2, "libro": "FISICA AVENTURAS EN EL ESPACIO Y EL TIEMPO", "autor": "ISAAC MCPHEE",
        "ISBN": 9788411540056, "paginas": 176, "precio": 69.000, "categoria": "Ciencias"},
    {"id": 3, "libro": "LOS ASESINOS DEL EMPERADOR", "autor": "SANTIAGO POSTEGUILLO",
        "ISBN": 9788408118329, "paginas": 1224, "precio": 99.000, "categoria": "Literatura"},
    {"id": 4, "libro": "UN MUNDO SIN FIN", "autor": "JOHN KATZENBACH",
        "ISBN": 9786287634275, "paginas": 422, "precio": 72.000, "categoria": "Literatura"},
    {"id": 5, "libro": "LA ISLA DE LAS TORMENTAS", "autor": "KEN FOLLETT",
        "ISBN": 9789585433557, "paginas": 319, "precio": 40.000, "categoria": "Literatura"},
    {"id": 6, "libro": "BIOLOGIA CELULAR CONCEPTOS ESENCIALES", "autor": "JOAQUIN DE JUAN HERRERO",
        "ISBN": 9788498357714, "paginas": 557, "precio": 368.000, "categoria": "Ciencias"}
]
## filtros usando filter y list comprehension

## Libros con precio mayor a $45.000

# usando filter
print("------Libros mayores a $45.000 usando filter------\n")


def precio_mayor(libro):
    return libro["precio"] > 45.000
  
lista_precio_mayor = filter(precio_mayor, lista_libros)

for libro in lista_precio_mayor:
    print(libro["libro"])

print()
# usando list comprehension

print("------Libros mayores a $45.000 usando list comprehension------\n")
filtro_precio_mayor = [
    libro for libro in lista_libros if libro["precio"] > 45.000]

for libro in filtro_precio_mayor:
    print(libro["libro"])
print()

## Libros de categoría "Literatura" con paginas > 500
# usando filter

print("------Libros de categoria Literatura con paginas > 500 usando filter------\n")

def categoria_mayor(libro):
    return libro["categoria"] == "Literatura" and libro["paginas"] > 500

categoria_mayor_500 = filter(categoria_mayor, lista_libros)

for libro in categoria_mayor_500:
    print(libro["libro"])

print()

# usando list comprehension

print("------Libros de categoria Literatura con paginas > 500 usando list comprehension------\n")
filtro_categoria_mayor = [libro for libro in lista_libros if libro["categoria"] == "Literatura" and libro["paginas"] > 500]

for libro in filtro_categoria_mayor:
    print(libro["libro"])

print()

# un filtro inventado por ud
# Libros de categoría con paginas > 500 y con el precio >70.000
# usando filter

print("------Libros con paginas > 500 y con el precio >70.000 usando filter------\n")

def paginas_precio_mayor(libro):
    return libro["paginas"] > 500 and libro["precio"] > 70.000

filtro_paginas = filter(paginas_precio_mayor, lista_libros)

for libro in filtro_paginas:
    print(libro["libro"])

print()

# Libros de categoría "Literatura" con paginas > 500 usando list comprehension

print("------Libros con paginas > 500 y con el precio >70.000 usando list comprehension------\n")

paginas_menores = [libro for libro in lista_libros if libro["paginas"]> 500 and libro["precio"] > 70.000]

for libro in paginas_menores:
    print(libro["libro"])

