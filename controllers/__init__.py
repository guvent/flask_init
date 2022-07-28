import importlib
import os

from werkzeug.exceptions import NotFound

from utils import RequestParams


class Controller:
    modules = {}

    def __init__(self):
        controller_files = os.listdir("controllers")

        for controller_file in controller_files:
            module_name = str(controller_file).split(".py")[0]
            if module_name != "__init__":
                module = importlib.import_module("controllers." + str(module_name))
                self.modules[module_name] = module

    def route(self, path, request, response, render_template, home_page="index"):
        params = RequestParams(request)
        params.set_response(response)
        params.set_render_template(render_template)

        c_path = str(path).split("/")[0]
        if str(c_path).strip() in self.modules:
            if self.modules.get(c_path).__dict__.__contains__(str(request.method).lower()):
                return self.modules.get(c_path).__getattribute__(str(request.method).lower())(params)
            else:
                raise NotFound(
                    description="Method Not Implemented!",
                    response=response("Method Not Implemented!", status=405)
                )

        elif str(c_path).strip() == "":
            try:
                return self.modules.get(home_page).__getattribute__(str(request.method).lower())(params)
            except AttributeError:
                raise NotFound(
                    description="Home Page Method Not Implemented!",
                    response=response("Home Page Method Not Implemented!", status=405)
                )

        raise NotFound(
            description="Route Not Found!",
            response=response("Route Not Found!", status=404)
        )
