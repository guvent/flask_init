import json

print("index py.......")


def get(params):
    return params.render_template("index.html", context={
        "title": "Hello!",
        "content": "Hello World!"
    })


def post(params):
    return params.response(
        json.dumps({"method": params.request.method}),
        mimetype="application/json",
        status=201
    )


def put(params):
    return "Method: " + str(params.request.method)

