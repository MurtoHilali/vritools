import click
from vritools.convert_amino_acids import convert

@click.command()
@click.argument('code')
def convert_cli(code):
    """Convert between three-letter and one-letter amino acid codes."""
    result = convert(code)
    if result == "Invalid code":
        click.echo(f"Error: {result}", err=True)
    else:
        click.echo(result)

if __name__ == "__main__":
    convert_cli()
