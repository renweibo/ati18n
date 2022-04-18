"""Console script for ati18n."""
import sys
import typer


app = typer.Typer()


@app.command()
def main(args=None):
    """Console script for ati18n."""
    typer.echo("Replace this message by putting your code into ati18n.cli.main")
    return 0


if __name__ == "__main__":
    app()
