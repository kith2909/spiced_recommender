import uuid


class SetCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        cookie_value = str(uuid.uuid4())
        response.set_cookie('chat_to_grow', cookie_value)
        return response
