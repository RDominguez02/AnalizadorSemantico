from lexer import lexer
from parser import parser

def main():
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        lexer.input(s)
        for token in lexer:
            print(token)
        result = parser.parse(s)
        print(result)

if __name__ == '__main__':
    main()