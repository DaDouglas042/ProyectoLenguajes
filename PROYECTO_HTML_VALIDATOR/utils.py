def read_html_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no fue encontrado.")
        return ""
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return ""
