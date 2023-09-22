import click
from vritools.mutation_code import MutationCode

@click.command()
@click.option('-c', '--code', required=True, help="Mutation code to parse.")
@click.option('-w', '--wildtype_residue', is_flag=True, help="Return wildtype residue.")
@click.option('-p', '--position', is_flag=True, help="Return position.")
@click.option('-m', '--missense_residue', is_flag=True, help="Return missense residue.")
def mutation_code_cli(code, wildtype_residue, position, missense_residue):
    """Parse protein mutation codes."""
    mutation = MutationCode(code)

    if wildtype_residue:
        click.echo(mutation.wtres)
    if position:
        click.echo(mutation.pos)
    if missense_residue:
        click.echo(mutation.msres)

if __name__ == "__main__":
    mutation_code_cli()
