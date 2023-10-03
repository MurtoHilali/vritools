import argparse
from .amino_acids import AMINO_ACIDS, REVERSE_AMINO_ACIDS

def convert(code):
    if len(code) == 1:
        return REVERSE_AMINO_ACIDS.get(code.upper(), "Invalid code")
    elif len(code) == 3:
        return AMINO_ACIDS.get(code.upper(), "Invalid code")
    else:
        return "Invalid code"

def main():
    parser = argparse.ArgumentParser(description="Convert between three-letter and one-letter amino acid codes.")
    parser.add_argument("code", help="Amino acid code to convert.")
    
    args = parser.parse_args()
    
    print(convert(args.code))

if __name__ == "__main__":
    main()
