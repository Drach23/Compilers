import ply.lex as lex

# Lista de tokens
tokens = (
    'INT',      # Palabra clave 'int'
    'RETURN',   # Palabra clave 'return'
    'ID',       # Identificadores
    'NUMBER',   # Números enteros
    'STRING'    # Cadenas de texto
)

# Palabras clave reservadas
reserved = {
    'int': 'INT',
    'return': 'RETURN'
}

# Reglas para los tokens
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica si es palabra clave
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"([^\n"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remover las comillas
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Comentarios de una línea
def t_COMMENT_SINGLELINE(t):
    r'//.*'
    pass  # Ignorar el comentario

# Comentarios de múltiples líneas
def t_COMMENT_MULTILINE(t):
    r'/\*[\s\S]*?\*/'
    pass  # Ignorar el comentario

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la linea {t.lineno}")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

# Función para probar el lexer
def test_lexer(data):
    lexer.input(data)
    for tok in lexer:
        print(tok)

if __name__ == "__main__":
    data = """
    int x = 10;
    return x;
    // Esto es un comentario de una linea
    /* Esto es un
    comentario de múltiples lineas */
    "Esto es una cadena de texto"
    """
    test_lexer(data)
