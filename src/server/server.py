from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.web import Application
from src.server.router import Router;


class Server:

    @classmethod
    def start(cls):
        application = Application(Router.routes())
        server = HTTPServer(application)
        server.bind(8888)
        server.start(1, 10)
        IOLoop.current().start()
