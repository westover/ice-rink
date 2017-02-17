from __future__ import unicode_literals, print_function
import sys
import os

from tornado.web import Application, StaticFileHandler, RequestHandler, url
import tornado.wsgi
from tornado.httpserver import HTTPServer
from tornado.options import parse_command_line, define, options

sys.path.insert(0, os.path.abspath('..'))

define("port", default=8888)
define("debug", default=False)


class Health(RequestHandler):

    def get(self):
        self.write("OK")


if __name__ == '__main__':
    parse_command_line()

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static/build"),
        "cookie_secret": "ZAMBONI",
        "xsrf_cookies": True,
        "debug": options.debug
    }

    static_file_handler_settings = {
        "path": settings["static_path"],
        "default_filename": "index.html",
    }

    application = Application([
        ("/health", Health),
        (r"/(.*)", StaticFileHandler, static_file_handler_settings),
    ], **settings)

    server = HTTPServer(application)
    server.bind(options.port)

    if options.debug:
        server.start()  # simple single-process
    else:
        server.start(0)  # forks one process per cpu

    tornado.ioloop.IOLoop.current().start()
