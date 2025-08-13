import typer

# 1. On crée une instance de l'application Typer.
#    C'est cet objet 'app' qui va gérer toutes nos commandes.
app = typer.Typer(help="MyDevCompanion : Un outil CLI pour le codage agentique.")

# 2. On utilise le décorateur @app.command() pour définir une commande.
@app.command()
def version():
    """
    Affiche la version de l'outil.
    """
    typer.echo("my-dev-companion version 0.1.0 (avec Typer)")

@app.command()
def hello(name: str):
    """
    Dit bonjour à quelqu'un.
    """
    typer.echo(f"Bonjour, {name} !")

# 3. Le point d'entrée pour l'exécution directe du script
if __name__ == '__main__':
    app()
