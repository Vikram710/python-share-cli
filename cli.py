import click
import pymongo
import json,bson
client = pymongo.MongoClient("mongodb://nsi319:babaji_123@sharecli-shard-00-00.csdat.gcp.mongodb.net:27017,sharecli-shard-00-01.csdat.gcp.mongodb.net:27017,sharecli-shard-00-02.csdat.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-nsb81p-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client["share_database"]
# print(client.list_database_names())
# print(db.list_collection_names())
user_collection = db["user"]
message_collection = db["message"]

    
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
@click.argument('name')
def create(name):
    """Create User"""
    if name != '':
        if user_collection.find_one({"name" : name})!=None:
            click.echo("Username already taken.. Try with a different name")
        else:
            insert = user_collection.insert_one({"name": name})
            click.echo("Your _id is: {0} ".format(str(insert.inserted_id)))
            click.echo("User creation successful")
    else:
        click.echo("Name attribute cannot be empty")

@cli.command()
def users():
    """Get all Users"""
    if user_collection.find()!=None:
        for user in user_collection.find():
            # check online 
            click.echo("{0}".format(user["name"]))
    else:
        click.echo("No active users :(")


