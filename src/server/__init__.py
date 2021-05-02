from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from src.server.router import *
from src.server.mongo import *
from src.server.application import *


class Server:
    """Custom Tornado web application server"""
    @classmethod
    def start(cls):
        # create context and application
        ctx, app = get_app()

        # create HTTP server
        server = HTTPServer(app)

        # bind to port
        server.bind(ctx.port)

        # number of processes (fork not supported on Windows!)
        server.start(1 if os.name == 'nt' else ctx.processes)

        # initialize the mongo database
        Mongo.init(ctx.mongoUri)

        # application.settings is available to all subclasses of RequestHandler, i.e., RequestHandler.settings
        app.settings['db'] = Mongo.get()

        # start the "main" IOLoop
        IOLoop.current().start()
