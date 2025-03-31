import ply.lex as lex

# Definimos los tokens
tokens = (
    'KEYWORD',  # Palabras clave como int, return
    'IDENTIFIER',  # Identificadores
    'NUMBER',  # Números
)

# Palabras clave reservadas
reserved = {
    'int': 'KEYWORD',
    'return': 'KEYWORD'
}

# Expresiones regulares para los tokens
def t_KEYWORD(t):
    r'int|return'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Si no es palabra clave, es identificador
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convertimos a entero
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

#Creación del analizador léxico (lexer)
lexer = lex.lex()

#Prueba con código de entrada
code = "int x = 55; return x;"
lexer.input(code)

#Imprimir los tokens reconocidos
for tok in lexer:
    print(tok)
