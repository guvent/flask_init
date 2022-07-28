import json

from utils import Validation
from services import HomepageService


def get(params):
    return params.render_template("index.html", context={
        "title": "Hello!",
        "content": "Hello World!"
    })


def post(params):
    request_body = params.request.json

    validated, exception = Validation(request_body).validate_dict({
        "username": {"type": str, "min": 3, "max": 100, "required": True},
        "password": {"type": str, "min": 3, "max": 100, "required": True},
        "status": {"type": bool, "required": False},
    })

    if validated is not True:
        return params.response(
            json.dumps(exception),
            mimetype="application/json",
            status=400
        )

    home_service = HomepageService()
    home = home_service.get_home()

    return params.response(
        json.dumps({
            "method": params.request.method,
            "body": request_body,
            "data": home
        }),
        mimetype="application/json",
        status=201
    )


def put(params):
    return "Method: " + str(params.request.method)

