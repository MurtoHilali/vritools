# vritools.py
import re
import argparse
from .convert_amino_acids import convert

class MutationCode:
    def __init__(self, code):
        # Regular expression to match the mutation code
        pattern = r"(?:p\.)?([A-Za-z]{1,3})(\d+)([A-Za-z]{1,3})"
        match = re.match(pattern, code)
        if not match:
            raise ValueError("Invalid mutation code format")

        self.wtres = match.group(1)
        self.pos = int(match.group(2))
        self.msres = match.group(3)

    def get_wtres(self):
        return self.wtres

    def get_pos(self):
        return self.pos

    def get_msres(self):
        return self.msres

    def as_tuple(self):
        return self.wtres, self.pos, self.msres

    def concise_format(self, as_tuple=False):
        wtres_concise = convert(self.wtres)
        msres_concise = convert(self.msres)
        if wtres_concise == "Invalid code" or msres_concise == "Invalid code":
            return "Invalid code"
        if as_tuple:
            return wtres_concise, self.pos, msres_concise
        return f"{wtres_concise}{self.pos}{msres_concise}"

def parse_mutation_code(code):
    return MutationCode(code)

def main():
    parser = argparse.ArgumentParser(description="Parse protein mutation codes.")
    parser.add_argument("-c", "--code", required=True, help="Mutation code to parse.")
    parser.add_argument("-w", "--wildtype_residue", action="store_true", help="Return wildtype residue.")
    parser.add_argument("-p", "--position", action="store_true", help="Return position.")
    parser.add_argument("-m", "--missense_residue", action="store_true", help="Return missense residue.")
    parser.add_argument("-f", "--concise_format", action="store_true", help="Return code in concise format.")
    parser.add_argument("-t", "--as_tuple", action="store_true", help="Return concise format as a tuple.")

    args = parser.parse_args()

    mutation = parse_mutation_code(args.code)

    if args.wildtype_residue:
        print(mutation.wtres)
    if args.position:
        print(mutation.pos)
    if args.missense_residue:
        print(mutation.msres)
    if args.concise_format:
        print(mutation.concise_format(as_tuple=args.as_tuple))

if __name__ == "__main__":
    main()