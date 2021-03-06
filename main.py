import tornado.web
import tornado.ioloop
import json



class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")


class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("dates.txt", "r")
        dates = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(dates))

    #def post(self):
        #fruit = self.get_argument("fruit")
        #fh = open("list.txt", "a")
        #fh.write(f"{fruit}\n")
        #fh.close()
        #self.write(json.dumps({"message": "Fruit added successfully."}))


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/assets/(.*)", tornado.web.StaticFileHandler, {"path": "./assets"},),
        (r"/", mainRequestHandler),
        (r"/dates", listRequestHandler),

    ])

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()