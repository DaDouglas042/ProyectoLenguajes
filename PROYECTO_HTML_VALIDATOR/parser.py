import ply.yacc as yacc
from lex import tokens

# Gramática
def p_structure(p):
    '''structure : header paragraphs structure
                 | header paragraphs
                 | header structure
                 | header
    '''

def p_header(p):
    '''header : H1
              | H2
              | H3
              | H4
              | H5
              | H6
    '''
    print(f"Encabezado encontrado: {p[1]}")

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
