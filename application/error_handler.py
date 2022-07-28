from flask import json
from werkzeug.exceptions import MethodNotAllowed, NotFound


class DefaultErrorHandler:
    response = None

    def __init__(self, app, response):
        app.register_error_handler(Exception, self.handle_exception)
        app.register_error_handler(MethodNotAllowed, self.handle_method_not_allowed)
        app.register_error_handler(NotFound, self.handle_not_found)

        self.response = response

    def handle_exception(self, err):
        return self.response(json.dumps({
            "code": 500,
            "error": "Internal Server Error!",
            "message": str(err),
        }), status=500, mimetype="application/json", content_type="application/json")

    def handle_method_not_allowed(self, err):
        return self.response(json.dumps({
            "code": err.code,
            "error": err.name,
            "message": err.description,
        }), status=err.code, mimetype="application/json", content_type="application/json")

    def handle_not_found(self, err):
        return self.response(json.dumps({
            "code": err.code,
            "error": err.name,
            "message": err.description,
        }), status=err.code, mimetype="application/json", content_type="application/json")

