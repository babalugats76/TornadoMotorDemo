from tornado import escape, httpclient
from tornado.web import RequestHandler


class ExampleHttpClientHandler(RequestHandler):
    """Example of async handler that interacts with external api"""
    __BASE_URL = "https://jsonplaceholder.typicode.com/todos/"

    @classmethod
    def get_base_url(cls):
        return cls.__BASE_URL

    def data_received(self, chunk):
        pass

    async def get(self, todo_id):
        """Example async GET handler with non-blocking operation"""
        http = httpclient.AsyncHTTPClient()
        response = await http.fetch(self.get_base_url() + todo_id)
        json = escape.json_decode(response.body)
        self.set_status(200)
        self.set_header('Content-Type', 'application/json')
        self.write(json)
