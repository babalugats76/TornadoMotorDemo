import os
from dotenv import load_dotenv
from src import server

env = os.getenv("TORNADO_ENV", "production")

if env == "development":
    load_dotenv()  # take environment variables from .env

if __name__ == '__main__':
    server().start()
