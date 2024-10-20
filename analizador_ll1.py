# Analizador sintáctico LL(1) que acepta mis iniciales "EMPR"

# Gramática:
# S -> E M P R S | ε

# Tabla LL(1):
# M[S, E] = 'E M P R S'
# M[S, $] = ε (vacío)

def ll1_parser(input_string):
    # Definición de la tabla LL(1)
    table = {
        ('S', 'E'): ['E', 'M', 'P', 'R', 'S'],
        ('S', '$'): ['ε'],  # ε representa la cadena vacía
    }

    stack = ['S']  # Pila de análisis
    index = 0  # Índice de la cadena de entrada
    input_string = list(input_string) + ['$']  # Cadena de entrada más símbolo $

    while stack:
        top = stack.pop()  # Cima de la pila

        if top == 'ε':
            continue  # Skip si es cadena vacía

        elif top == input_string[index]:
            # Coincide el símbolo en la pila y en la entrada
            index += 1
        elif (top, input_string[index]) in table:
            # Busca en la tabla LL(1)
            production = table[(top, input_string[index])]

            # (en orden inverso)
            stack.extend(production[::-1])
        else:
            print("Error de sintaxis")
            return False

    if input_string[index] == '$':
        print("Cadena aceptada")
        return True
    else:
        print("Error de sintaxis")
        return False


# Prueba con cadena válida
cadena = "EMPR"  
if ll1_parser(cadena):
    print("La cadena es válida según la gramática.")
else:
    print("La cadena no es válida.")
