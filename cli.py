import click
from sqlalchemy import create_engine,inspect

engine = create_engine('mysql+pymysql://root:rootpass@127.0.0.1:3306/clitool')
print(engine.table_names())
#connection = engine.connect()
    
@click.group()
@click.option('--pre',default='',help="pre loading option")
def cli(pre):
    pass


@cli.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--name', '-n', multiple=True, default='', help='Who are you?')
@click.argument('country')
def greet(verbose,name,country):
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello {0}".format(country))
    for n in name:
        click.echo('Bye {0}'.format(n))


@cli.command()
@click.option('--name',type=click.STRING,required=True)
def create(name):
    if name != '':
        click.echo("user created!!")
