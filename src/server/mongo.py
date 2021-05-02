from motor.motor_tornado import MotorClient


class Mongo:
    """MongoDB helper"""

    __CLIENT = None
    DB = None

    @classmethod
    def init(cls, uri):
        """Create database with asynchronous connector"""
        # Create db client
        cls.__CLIENT = MotorClient(uri)
        cls.DB = cls.__CLIENT.get_default_database()

    @classmethod
    def set(cls, db):
        cls.DB = db

    @classmethod
    def get(cls):
        return cls.DB
