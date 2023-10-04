# VRITools

VRITools is a collection of Python tools designed as a remedy for the most common, small headaches encountered when studying variant residues at Protein-Protein Interactions (PPIs).

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Mutation Code Parser](#mutation-code-parser)
  - [Convert Amino Acids](#convert-amino-acids)
  - [Mutate FASTA](#mutate-fasta)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation
TODO: Instructions on how to install the package.

## Usage
### Mutation Code Parser
To use the mutation code parser from the command line:
```bash
$ vritools mutation_code -c "G123C" -w
```
### Convert Amino Acids
To convert between three-letter and one-letter amino acid codes:
```bash
$ vritools convert [CODE]
```
### Mutate FASTA
To create a mutated version of a FASTA file:
```bash
$ vritools mutate_fasta [FASTA_FILE] [MUTATION_CODE] [OUTPUT_FOLDER]
```

## Contributing
TODO: Guidelines for contributing to this project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
TODO: Any acknowledgements or credits.