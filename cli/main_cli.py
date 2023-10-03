import click
from .mutation_code_cli import mutation_code_cli
from .mutate_fasta_cli import mutate_fasta_cli
# from .other_tool2_cli import other_tool2_cli

@click.group()
def main():
    """vritools: A collection of tools for VR."""
    pass

main.add_command(mutation_code_cli, name="mutation_code")
main.add_command(mutate_fasta_cli, name="mutate_fasta")
# main.add_command(other_tool2_cli, name="other_tool2")

if __name__ == "__main__":
    main()
