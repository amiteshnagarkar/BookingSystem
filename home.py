import tornado.web
import tornado.ioloop


class Handler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")

application = tornado.web.Application([
(r"/",Handler),
(r"/(logo.png)", tornado.web.StaticFileHandler, {'path':'./'}) <--Add!
])


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", mainRequestHandler),
        (r"/dates", listRequestHandler)
    ])

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()