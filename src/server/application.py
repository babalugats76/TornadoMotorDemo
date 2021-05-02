import os
from argparse import ArgumentParser
from dataclasses import dataclass

from tornado.web import Application

from src.server import Router
from src.server import Mongo


@dataclass
class ApplicationContext:
    """POPO for web application configuration"""
    port: int
    processes: int
    mongoUri: str


def get_context() -> ApplicationContext:
    """Creates application context"""

    # define and parse acceptable command-line args
    parser = ArgumentParser()
    parser.add_argument('--port', default=5000, type=int, help='Port where application will listen')
    parser.add_argument('--processes', default=1, type=int, help='Number of processes. 0 is one per CPU')
    args = parser.parse_args()

    # return context populating from args and environment variables
    return ApplicationContext(
        port=args.port,
        processes=args.processes,
        mongoUri=os.environ.get('MONGO_URI', None)
    )


def get_app() -> (ApplicationContext, Application):
    """Creates application"""
    ctx: ApplicationContext = get_context()
    return ctx, Application(Router.routes())
