from src.handlers.todo_handler import TodoHandler


class Router:
    # Dictionary to map routes to Tornado RequestHandler subclasses
    ROUTES = {
        '/todo/?(?P<todo_id>[^/]+)?': TodoHandler,
    }

    @classmethod
    def routes(cls):
        """ Get routes with their respective handlers"""
        return [(k, v) for k, v in cls.ROUTES.items()]
