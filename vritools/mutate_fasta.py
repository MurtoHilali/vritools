import os
import argparse
from .mutation_code import MutationCode

# Function to mutate a FASTA file
def mutate_fasta(fasta_file, mutation_code, output_folder):
    ref_aa, pos, alt_aa = MutationCode(mutation_code).concise_format(as_tuple=True)
    
    # Read the original FASTA file
    with open(fasta_file, 'r') as f:
        header = f.readline()
        sequence = f.read().replace('\n', '')
    
    # Check the reference amino acid
    if sequence[pos-1] != ref_aa:
        raise ValueError(f"Reference amino acid does not match at position {pos}")
    
    # Create the mutated sequence
    mutated_sequence = sequence[:pos-1] + alt_aa + sequence[pos:]
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Write the mutated sequence to a new FASTA file
    output_file = os.path.join(output_folder, os.path.basename(fasta_file).replace('.fasta', f'_{mutation_code}.fasta'))
    with open(output_file, 'w') as f:
        f.write(header)
        for i in range(0, len(mutated_sequence), 80):
            f.write(mutated_sequence[i:i+80] + '\n')
    
    print(f"Mutated FASTA file created: {output_file}")

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description="Create a mutated version of a FASTA file.")
    parser.add_argument("fasta_file", help="Path to the original FASTA file.")
    parser.add_argument("mutation_code", help="Mutation code.")
    parser.add_argument("output_folder", help="Path to the output folder.")
    
    args = parser.parse_args()
    mutate_fasta(args.fasta_file, args.mutation_code, args.output_folder)

if __name__ == "__main__":
    main()
