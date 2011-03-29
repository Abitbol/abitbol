# -*- coding: utf-8 -*-
"""
Abitbol's main module.

"""
from api.rest.server import RestServer
from core.transport.utils import TransportFactory
from xmpp import Client
from xmpp import Message

__author__ = "Jérémy Subtil"
__email__ = "jeremy.subtil@smile.fr"


def test():

	client = Client('localhost')

	def message_handler(conn, mess_node):
		client.send(Message('tim@localhost', 'reponse!'))

	if not client.connect(server=('127.0.0.1', 5222)):
		raise IOError('Can not connect to server.')

	if not client.auth('abitbol', 'abitbol', 'abitbol'):
		raise IOError('Can not auth with server.')

	client.RegisterHandler('message', message_handler)

	client.sendInitPresence()

	client.send(Message('tim@localhost', 'Test message'))

	while 1:
		client.Process(1)

#	client.sendPresence(typ='unavailable')
#	client.disconnect()


class AbitbolServer(object):
	"""
	The Abitbol server.

	"""
	settings = None

	def configure(self, settings):
		"""
		Configures the server before it can be run.

		"""
		self.settings = settings

	def run(self):
		"""
		Starts the server instance.

		"""
		if not self.settings:
			raise RuntimeError("The server is not configured.")

		self.transport = TransportFactory(self.settings.get('transport_type'))
		self.restServer = RestServer()

		self.transport.connect()
		self.restServer.run()


server = AbitbolServer()
