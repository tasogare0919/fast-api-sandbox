import falcon

class HelloWorldResouce:
    def on_get(self, request, response):

        response.media = ('Hello Wolrd')

app = falcon.API()
app.add_route('/',HelloWorldResouce())