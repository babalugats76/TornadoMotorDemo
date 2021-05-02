from src.controllers import *


class Router:
    """Application routing helper"""
    # Dictionary to map routes to Tornado RequestHandler subclasses
    ROUTES = {
        '/examples/http/todos/?(?P<todo_id>[^/]+)?': ExampleHttpClientHandler,
    }

    @classmethod
    def routes(cls):
        """Get routes with their respective controllers"""
        return [(k, v) for k, v in cls.ROUTES.items()]
