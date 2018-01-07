color_favorito = "amarillo"
color_encontrado = False

colores_disponibles = ('azul', 'verde', 'amarillo', 'morado', 'celeste')

for color in colores_disponibles:
    if color == color_favorito:
        color_encontrado = True

if color_encontrado:
    print("tu color favorito SÍ está disponible, puedes pedir tu camiseta")
else:
    print("tu color favorito no está disponible, lo siento")