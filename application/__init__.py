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
