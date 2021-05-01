from src.controllers import *


class Router:
    # Dictionary to map routes to Tornado RequestHandler subclasses
    ROUTES = {
        '/todos/?(?P<todo_id>[^/]+)?': TodoHandler,
    }

    @classmethod
    def routes(cls):
        """ Get routes with their respective controllers"""
        return [(k, v) for k, v in cls.ROUTES.items()]
