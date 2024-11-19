from lex import lexer
from parser import parser
import utils

def main():
    file_path = input("Ingresa la ruta del archivo HTML a validar (ej., valid.html): ")
    content = utils.read_html_file(file_path)
    
    if not content:
        return

    print("\n--- Análisis Léxico ---\n")
    
    # Análisis léxico
    lexer.input(content)
    for token in lexer:
        print(token)
    
    print("\n--- Análisis Sintáctico ---\n")
    # Reiniciar el nivel del último encabezado antes del análisis sintáctico
    global last_header_level
    last_header_level = 0
    # Análisis sintáctico
    parser.parse(content)
    
if __name__ == "__main__":
    main()
