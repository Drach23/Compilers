import ply.lex as lex

# Lista de tokens
tokens = (
    'INT',        # Palabra clave 'int'
    'RETURN',     # Palabra clave 'return'
    'ID',         # Identificadores
    'NUMBER',     # Números enteros
    'STRING',     # Cadenas de texto
    'PLUS',       # Operador +
    'MINUS',      # Operador -
    'TIMES',      # Operador *
    'DIVIDE',     # Operador /
    'EQUALS',     # Operador =
    'LPAREN',     # Delimitador (
    'RPAREN',     # Delimitador )
    'LBRACE',     # Delimitador {
    'RBRACE',     # Delimitador }
    'SEMICOLON'   # Delimitador ;
)

# Reglas para los tokens
reserved = {
    'int': 'INT',
    'return': 'RETURN'
}

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

# Operadores
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='

# Delimitadores
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

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
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

# Función para analizar un archivo y contar elementos
def analyze_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    
    lexer.input(data)
    counts = {'keywords': 0, 'identifiers': 0, 'numbers': 0, 'operators': 0, 'delimiters': 0}
    
    for tok in lexer:
        if tok.type in ['INT', 'RETURN']:
            counts['keywords'] += 1
        elif tok.type == 'ID':
            counts['identifiers'] += 1
        elif tok.type == 'NUMBER':
            counts['numbers'] += 1
        elif tok.type in ['PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS']:
            counts['operators'] += 1
        elif tok.type in ['LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON']:
            counts['delimiters'] += 1
    
    print("Resultados del análisis léxico:")
    for key, value in counts.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    filename = r"C:\Users\Diego Aquino\Documents\Code\Uni\Compiladores\hands_on_2\CodigoPrueba.c"
    analyze_file(filename)

