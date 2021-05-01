from dataclasses import dataclass
from argparse import ArgumentParser
from tornado.web import Application
from src.server.router import Router


@dataclass
class ApplicationContext:
    """POPO Class for web application configuration."""
    port: int
    processes: int


def parse_arguments() -> ApplicationContext:
    """Defines and parses command-line args, returning populated instance of ApplicationContext."""
    parser = ArgumentParser()
    parser.add_argument('--port', default=5000, type=int, help='Port where application will listen')
    parser.add_argument('--processes', default=1, type=int, help='Number of processes. 0 is one per CPU')
    args = parser.parse_args()
    return ApplicationContext(
        port=args.port,
        processes=args.processes
    )


def get_app() -> (ApplicationContext, Application):
    context: ApplicationContext = parse_arguments()
    return context, Application(Router.routes())
