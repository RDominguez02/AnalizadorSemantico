import ply.yacc as yacc
from lexer import tokens

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POW'),
    ('right', 'UMINUS'),

)

# Reglas gramaticales
def p_expression_plus(p):
    '''expression : expression PLUS expression'''
    if isinstance(p[1], str) or isinstance(p[3], str):
        p[0] = str(p[1]) + str(p[3])  # Concatenación de cadenas
    else:
        p[0] = p[1] + p[3]  # S

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    if p[3] == 0:
        raise SyntaxError("Error: División por cero")
    else:
        p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMBER'
    if not isinstance(p[1], int):
        print("Error semántico: Se esperaba un número entero")
        p[0] = 0
    else:
        p[0] = p[1]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_pow(p):
    'expression : expression POW expression'
    p[0] = p[1] ** p[3]

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]  # El valor de la cadena ya está sin comillas



# Manejo de errores
def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en '{p.value}' en la posición {p.lexpos}")
    else:
        raise SyntaxError("Error de sintaxis: Entrada incompleta")

# Construir el parser
parser = yacc.yacc()