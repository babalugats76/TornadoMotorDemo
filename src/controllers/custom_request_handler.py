from typing import Optional, Awaitable

from tornado.web import RequestHandler

from src.server.database import Mongo


class CustomRequestHandler(RequestHandler):

    @classmethod
    def initialize(cls, **args):
        print('initializing...')
        print(args)

    def data_received(self, chunk):
        pass

    def prepare(self):
        """Called at the beginning of GET/POST requests, etc."""
        print('preparing...')
        # This is needed so that every request can access globally to the database or lock server
        Mongo.set(self.settings['db'])

    def on_finish(self):
        """Called at the end of each request (for cleanup, logging, etc.)"""
        print('finishing...')
