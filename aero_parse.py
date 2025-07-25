import argparse
import sys
import re

def main():
    
    args = parse_args()
    content = read_file(args.file)
    lexed_input = json_lexer(content)
    if json_parser(lexed_input):
        print("Valid JSON")
        sys.exit(0)
    else:
        print("Invalid JSON")
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser(
        prog = "Aero JSON Parser",
        description="Aero's Version of json_parser",
        epilog = "Have a nice day!"
    )

    parser.add_argument("file", type=str, nargs="?", help="File to Process")

    return parser.parse_args()

def read_file(file):
    if file is None:
        print("No file specified.")
        sys.exit(1)
    with open(file, "r") as f:
        return f.read()
    
def json_lexer(data):
    token_pattern = r'({|}|:|,|"[^"]*")'
    lexer = []
    data = "".join(data.split())
    tokens = re.findall(token_pattern, data)
    for token in tokens:
        if token == "{":
            lexer.append(("LEFT_BRACE", token))
        elif token == "}":
            lexer.append(("RIGHT_BRACE", token))
        elif token == ":":
            lexer.append(("COLON", token))
        elif token.startswith('"') and token.endswith('"'):
            lexer.append(("STRING", token[1:-1])) #Strip Quotes
        else:
            return []
    return lexer

def json_parser(lexed_json):
    pass
        
    


if __name__ == "__main__":
    main()