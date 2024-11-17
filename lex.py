import ply.lex as lex

# Lista de tokens
tokens = (
    'H1', 'H2', 'H3', 'H4', 'H5', 'H6',
    'P', 'OPEN_TAG', 'CLOSE_TAG', 'TEXT'
)

# Definiciones de tokens
t_H1 = r'<h1>'
t_H2 = r'<h2>'
t_H3 = r'<h3>'
t_H4 = r'<h4>'
t_H5 = r'<h5>'
t_H6 = r'<h6>'
t_P = r'<p>'
t_OPEN_TAG = r'</?[a-zA-Z0-9]+>'
t_CLOSE_TAG = r'</[a-zA-Z0-9]+>'
t_TEXT = r'[^<>\n]+'

# Ignorar espacios, tabuladores y nuevas líneas
t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
