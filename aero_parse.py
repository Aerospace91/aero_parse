import argparse

def main():
    
    args = parse_args()    


def parse_args():
    parser = argparse.ArgumentParser(
        prog = "Aero JSON Parser",
        description="Aero's Version of json_parser",
        epilog = "Have a nice day!"
    )

    parser.add_argument("file", type=str, nargs="?", help="File to Process")


    return parser.parse_args()


if __name__ == "__main__":
    main()