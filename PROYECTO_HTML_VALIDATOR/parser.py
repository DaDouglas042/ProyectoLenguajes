import ply.yacc as yacc
from lex import tokens

# Variable global para rastrear el nivel del último encabezado
last_header_level = 0

# Gramática
def p_structure(p):
    '''structure : header paragraphs structure
                 | header structure
                 | header paragraphs
                 | header
    '''

def p_header(p):
    'header : HEADER'
    global last_header_level
    current_level = int(p[1][2:-1])  # Extrae el número del encabezado
    if current_level != last_header_level + 1:
        print(f"Error: Encabezado fuera de secuencia en {p[1]}")
    else:
        print(f"Encabezado correcto: {p[1]}")
    last_header_level = current_level

def p_paragraphs(p):
    '''paragraphs : P paragraphs
                  | P
    '''
    print("Párrafo encontrado")

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis en EOF")

# Construir el parser
parser = yacc.yacc()
