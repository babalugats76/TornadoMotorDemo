from tornado import escape, httpclient
from tornado.web import RequestHandler


class TodoHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    async def get(self, todo_id):
        http = httpclient.AsyncHTTPClient()
        response = await http.fetch("https://jsonplaceholder.typicode.com/todos/" + todo_id)
        json = escape.json_decode(response.body)
        self.set_status(200)
        self.set_header('Content-Type', 'application/json')
        self.write(json)
