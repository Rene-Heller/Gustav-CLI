import os
import click
import subprocess


@click.command()
@click.argument("name")
def init_project(name: str):

    os.makedirs(name, exist_ok=True)

    index_html = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>My App</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>

            <h1>Hello World</h1>

            <script src="script.js"></script>
        </body>
    </html>
    """

    style_css = """
    *{
        margin:0;
        box-sizing:border-box;
    }
    """

    script_js = """
    console.log("Hello from JS!");
    """

    with open(os.path.join(name, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    with open(os.path.join(name, "style.css"), "w", encoding="utf-8") as f:
        f.write(style_css)

    with open(os.path.join(name, "script.js"), "w", encoding="utf-8") as f:
        f.write(script_js)

    try:
        click.echo(name)
        subprocess.run("code .", cwd=name, shell=True, check=True)
    except FileNotFoundError:
        click.echo("VS Code CLI 'code' nicht gefunden. Bitte öffne den Ordner manuell.")
