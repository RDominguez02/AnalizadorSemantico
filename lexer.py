import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'POW',
    'STRING',
)

# Reglas para los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_POW = r'\^'

# Regla para números
def t_NUMBER(t):
    r'\d+\.\d+|\.\d+|\d+'  # Reconocer números decimales y enteros
    t.value = float(t.value) if '.' in t.value else int(t.value)  # Convertir a float o int
    return t

def t_STRING(t):
    r'"[^"]*"'  # Coincide con cualquier cosa entre comillas dobles
    t.value = t.value[1:-1]  # Elimina las comillas dobles
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    raise SyntaxError(f"Carácter ilegal '{t.value[0]}' en la posición {t.lexpos}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()