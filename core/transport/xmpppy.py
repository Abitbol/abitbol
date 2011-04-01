"""
XMPP transport through xmpppy.

"""
import core.server
from xmpp import Client
from xmpp import Message
from core.transport.common import Transport

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


def message_handler(conn, mess_node):
	conn.send(Message('tim@localhost', 'reponse!'))


class XmpppyTransport(Transport):
	"""
	Implements the XMPP transport (xmpppy).

	"""
	def __init__(self):
		settings = core.server.server.settings

		self.domain = settings.get('xmpp_domain')
		self.host = settings.get('xmpp_host')
		self.port = settings.get('xmpp_port')
		self.user = settings.get('xmpp_user')
		self.password = settings.get('xmpp_password')
		self.presence = settings.get('xmpp_presence')
		
		self.connected = False

	@classmethod
	def isIdentifiedBy(cls, type):
		return type == 'xmpp'

	def connect(self):
		"""
		Connects to an XMPP server.

		"""
		self.client = Client(self.domain)

		if not self.client.connect(server=(self.host, self.port)):
			raise IOError('Cannot connect to server.')

		if not self.client.auth(self.user, self.password, self.presence):
			raise IOError('Cannot auth with server.')

		self.client.RegisterHandler('message', message_handler)

		self.client.sendInitPresence()

		self.connected = True

		while True:
			self.client.Process(1)

	def disconnect(self):
		"""
		Disconnects from the current XMPP server.

		"""
		if connected:
			self.client.sendPresence(typ='unavailable')
			self.client.disconnect()

		self.client = None
		self.connected = False

	def send(self, destination, action):
		self.client.send(Message('tim@localhost', str(action)))
