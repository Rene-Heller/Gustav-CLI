import click
import webbrowser
import re

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("\nHello dear Master Kevin!")
    
    
@cli.command()
@click.option("--verbose", "-v", is_flag=True, help="detailed answer")
def status(verbose:bool):
    if verbose:
        click.echo("\nSystem Status")
        click.echo("- CPU   OK")
        click.echo("- Memory   OK")
        click.echo("- Disk   OK")
    else:
        click.echo("\nStatus: Everything is OK!")
    
    
@cli.command()
@click.argument("name")
def greet(name:str):
    click.echo(f'\nHello {name}! Nice to have you here :)')
    
    
@cli.command()
@click.argument('message', type=str)
@click.option("--times", "-t", type=int, default=2, help="repititions")
def repeat(message:str, times:int):
    click.echo("\n")
    for _x in range(times):
        click.echo(f'{_x + 1}: {message}')
        
        
@cli.command()
@click.argument("a", type=int)
@click.argument("b",type=int)
def sum(a:int,b:int):
    result = a + b
    click.echo(result)        
    
    
@cli.command()
def subcommand():
    click.echo("\nMy commands behave like any other commands. But they are part of me: Gustav!")
    
    
@click.command()    
def form_answer():
    data = click.get_text_stream("stdin").read().strip()
    click.echo(f"The result is: {data}")
        
@click.command()
def command():
    click.echo("\nI'm a command. I just need to be written to do something.")
    
@click.command()
def flag():
    click.echo("\nI'm a flag. You may see me like this: '--flag', or '-f' in short.\nJust write me once to enable a feature :D")
    
@click.command()
def option():
    click.echo("\nI'm an option. Similiar to flags but i need additional values, like: '--times 5', to be used.")
    
@click.command()
def pipe():
    click.echo("\n\n|\n\nYou see that stroke? That is a pipe. You can use the pipe to give a value to something else.\nFor example: 'sum 3 8 | form-answer' could result in 'The result of the calculation is 11!'")
    
@click.command()
def quote():
    click.echo("\nZu den Risiken und Nebenwirkungen zählen: trockener Mund, Übelkeit, Erbrechen, Harnstau, schmerzhafter rektaler Juckreiz, Halluzinationen, Demenz, Koma, Tod.\n\nMagie eignet sich nicht für jeden.")
    
@click.command()
def open_da():
    webbrowser.open("https://www.developer-akademie.com")
    
@click.command()
@click.argument("url", type=str)
def start_browser(url:str):
    regex = re.compile(r"^https?://")
    if not regex.match(url):
        url = "https://" + url
    webbrowser.open(url)