from src.controllers import *


class Router:
    """Application routing helper"""
    # Dictionary to map routes to Tornado RequestHandler subclasses
    ROUTES = {
        '/http/todos/?(?P<todo_id>[^/]+)?': HttpClientHandler,
    }

    @classmethod
    def routes(cls):
        """Get routes with their respective controllers"""
        return [(k, v) for k, v in cls.ROUTES.items()]
