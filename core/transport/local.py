"""
Local transport.

"""
from core.transport.common import Transport

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


class LocalTransport(Transport):
	"""
	Implements the local transport.

	"""
	def connect(self):
		pass

	def send(self, destination, action):
		receptor.handle(destination, action)

	@classmethod
	def isIdentifiedBy(cls, type):
		return type == 'local'


class ReceptionHandler(object):
	"""
	Handles local message reception.

	"""
	def handle(self, destination, action):
		module_name = "connectors.%s.actions.%s" % (destination, action['ns'])
		exec "import %s" % module_name
		callback_name = "%s.%s" % (module_name, action['action'])
		eval(callback_name)( ** action['kwargs'])
		
receptor = ReceptionHandler()
