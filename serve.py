import tornado.ioloop
import tornado.web
from ngrams import *

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		text = self.get_argument("q", "", True)
		if not text: raise tornado.web.HTTPError(404)

		segmented = segment2(text.lower())

		self.write(' '.join(segmented[1]))


application = tornado.web.Application([(r"/", MainHandler)])
if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
