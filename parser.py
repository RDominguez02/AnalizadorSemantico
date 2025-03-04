import ply.yacc as yacc
from lexer import tokens

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# Reglas gramaticales
def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    if p[3] == 0:
        print("Error semántico: División por cero")
        p[0] = 0
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

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Manejo de errores
def p_error(p):
    print("Error de sintaxis")

# Construir el parser
parser = yacc.yacc()