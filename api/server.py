"""
REST API server.

"""
import web

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


class RestServer(object):
	"""
	Serves REST requests to the API.

	"""
	def run(self):
		from api.urls import urls
		self.app = web.application(urls, {})
		self.app.run()
