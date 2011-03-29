"""
Common transport stuff.

"""

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


class Transport(object):
	"""
	Abstract class to access a transport.

	"""
	def connect(self):
		raise NotImplementedError()

	def send(self, destination, action):
		raise NotImplementedError()
