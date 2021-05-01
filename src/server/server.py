import os
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from src.server.app import get_app


class Server:

    @classmethod
    def start(cls):

        # create application and context
        context, app = get_app()

        # create HTTP server
        server = HTTPServer(app)

        # bind to port
        server.bind(context.port)

        # number of processes (fork not supported on Windows!)
        server.start(1 if os.name == 'nt' else context.processes)

        # start the "main" IOLoop
        IOLoop.current().start()
