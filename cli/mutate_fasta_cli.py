import click
from vritools import mutate_fasta

@click.command()
@click.argument('fasta_file', type=click.Path(exists=True))
@click.argument('mutation_code')
@click.argument('output_folder', type=click.Path())
def mutate_fasta_cli(fasta_file, mutation_code, output_folder):
    """Create a mutated version of a FASTA file."""
    try:
        mutate_fasta(fasta_file, mutation_code, output_folder)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)

if __name__ == "__main__":
    mutate_fasta_cli()
