import ply.lex as lex

# Lista de tokens
tokens = (
    'HEADER',
    'P',
    'TEXT',
)

# Definiciones de tokens
t_HEADER = r'<h[1-9][0-9]*>'
t_P = r'<p>'
t_TEXT = r'[^<>\n]+'

# Ignorar espacios, tabuladores y nuevas líneas
t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
