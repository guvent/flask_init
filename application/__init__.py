from flask import Flask, Response, request, render_template

from application.error_handler import DefaultErrorHandler
from controllers import Controller


app = Flask(__name__, template_folder="../templates", static_folder="../statics")

controller = Controller()

DefaultErrorHandler(app, Response)

allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


@app.route('/', defaults={'__path': ''}, methods=allowed_methods)
@app.route('/<path:__path>', methods=allowed_methods)
def routing(__path):
    return controller.route(
        path=__path,
        request=request,
        response=Response,
        render_template=render_template
    )
