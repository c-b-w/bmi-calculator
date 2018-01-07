# gonzalo [26/12/17-09:46]
#=========================
#
# Programa que sirve para calcular el índice de masa corporal (IMC).
# Este programa de ejemplo contiene:
#   variables, funciones, iteraciones, condicionales, entrada/salida
#   tipos de datos, estructuras y manejo de errores.
#
# **************************************************************************

# gonzalo [26/12/17-09:48] == definimos un par de variables globales que controlarán las iteraciones 'while'
peso_correcto = False
altura_correcta = False


# gonzalo [26/12/17-10:47] == definimos una función que usaremos más adelante
def calcular_imc(el_peso, la_altura):

    # la fórmula para calcular el imc es dividir el peso (kg) por el cuadrado de la altura (m)
    resultado = el_peso / pow(la_altura,2)

    return resultado


# gonzalo [26/12/17-10:51] == definimos la función para mostrar el imc
def mostrar_resultado(resultado):

    referencia = [((-100,15.99),"<- extr. delgado ->"),
                  ((16,18.49),"<---- delgado ---->"),
                  ((18.5,24.99),"<---- adecuado --->"),
                  ((25,29.99),"<--- sobrepeso --->"),
                  ((30,100),"<----- obeso ----->")]

    posiciones = {"<- extr. delgado ->":0,
                  "<---- delgado ---->":1,
                  "<---- adecuado --->":2,
                  "<--- sobrepeso --->":3,
                  "<----- obeso ----->":4}

    cabecera = ""

    for elemento in referencia:
        cabecera += elemento[1]

    print(cabecera)

    for elemento in referencia:
        if elemento[0][0] <= resultado <= elemento[0][1]:
            posicion = posiciones[elemento[1]]
            espacios = " " * 19 * posicion
        else:
            pass

    print (espacios + ' tu imc es   ' + '%.2f' % resultado)


# gonzalo [26/12/17-10:06] == damos la bienvenida y mostramos las instrucciones
print('\n')
print('Bienvenido a la calculadora de índice de masa corporal (IMC).')
print('Con esta herramienta podrás calcular tu IMC de forma rápida y sencilla.')
print('Sólo necesitas introducir tu peso en kg (valores mayores que cero y menores que 350)')
print('y tu altura en metros (valores mayores que cero y menores que 2.50).')
print('\n')

# gonzalo [26/12/17-10:18] == una iteración 'while' para recoger el peso por parte del usuario
while not peso_correcto:
    entrada = input('Por favor, introduce tu peso en kg (por ejemplo 78.5 ó 61): ')

    try:
        peso = float(entrada)

        if peso >=0 and peso <350:
            peso_correcto = True
        else:
            pass

    except ValueError:
        print('Por favor introduce el peso como número, no hace falta indicar que son kilos ("kg").')

# gonzalo [26/12/17-10:24] == una iteración 'while' para recoger la altura por parte del usuario
while not altura_correcta:
    entrada = input('Por favor, introduce tu altura en metros (por ejemplo 1.76 ó 1.87): ')

    try:
        altura = float(entrada)

        if altura >= 0 and altura < 2.5:
            altura_correcta = True
        else:
            pass

    except ValueError:
        print('Por favor introduce tu altura como número, no hace falta indicar que son metros ("m").')

# gonzalo [26/12/17-10:47] == calculamos el imc
imc = calcular_imc(peso,altura)

# gonzalo [26/12/17-10:43] == mostramos los resultados
print('\n')
mostrar_resultado(imc)