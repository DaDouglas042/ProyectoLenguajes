import ply.lex as lex

# Lista de tokens
tokens = (
    'HEADER',
    'P',
)

# Definiciones de tokens
def t_HEADER(t):
    r'<h[1-9][0-9]*>'
    return t

def t_P(t):
    r'<p>'
    return t

def t_ignore_TAG(t):
    r'</?[a-zA-Z][^>]*>'
    pass  # Ignorar otras etiquetas

def t_ignore_TEXT(t):
    r'[^<>\n]+'
    pass  # Ignorar texto

# Ignorar espacios, tabuladores y nuevas líneas
t_ignore = ' \t\n'

def t_error(t):
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
