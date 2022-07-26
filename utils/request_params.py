class RequestParams:
    request = None
    response = None
    render_template = None

    def __init__(self, request):
        self.request = request

    def get_request(self):
        return self.request

    def get_response(self):
        return self.response

    def set_response(self, response):
        self.response = response

    def set_render_template(self, render_template):
        self.render_template = render_template

    def get_render_template(self):
        return self.render_template
