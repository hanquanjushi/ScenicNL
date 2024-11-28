import scenic.syntax.parser
import sys

def check_scenic_syntax(fname):
    try:
        ast = scenic.syntax.parser.parse_file(fname)
        print(f'Syntax of {fname} is correct.')
    except Exception as e:
        print(f'Syntax error in {fname}: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_scenic_syntax.py <file.scenic>")
        sys.exit(1)
    check_scenic_syntax(sys.argv[1])