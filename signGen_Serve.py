import tornado.ioloop
import tornado.web
import sign_builder

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")
    def post(self):
        text = self.get_body_argument("text")
        name = sign_builder.imbuild(text)
        self.render("static/imageShow.html", name = name)
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ims/(.*)", tornado.web.StaticFileHandler, {'path': "ims"}),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': "static"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(19347)
    tornado.ioloop.IOLoop.current().start()