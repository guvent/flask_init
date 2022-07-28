import click
from flask import Flask, Response, request, render_template
from controllers import Controller


app = Flask(__name__, template_folder="../templates", static_folder="../statics")

controller = Controller()


@app.route('/', defaults={'__path': ''})
@app.route('/<path:__path>', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def routing(__path):
    return controller.route(
        path=__path,
        request=request,
        response=Response,
        render_template=render_template
    )


@app.cli.command("my-cmd")
@click.option('--param', default="")
def mycmd(param):
    print(param)


@app.cli.command("my-pos")
@click.option('--pos', nargs=2, type=float)
def findme(pos):
    click.echo('%s / %s' % pos)


@app.cli.command("my-msg")
@click.option('--message', '-m', multiple=True)
def commit(message):
    click.echo('\n'.join(message))


@app.cli.command("my-verb")
@click.option('-v', '--verbose', count=True)
def log(verbose):
    click.echo('Verbosity: %s' % verbose)
