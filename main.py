from lexer import lexer
from parser import parser

def main():
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            print("Saliendo...")
            break
        if not s:
            continue

        try:
            lexer.input(s)
            for token in lexer:
                print(token)
            result = parser.parse(s)
            print(f"Resultado: {result}")
        except SyntaxError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()