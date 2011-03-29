"""
Transport layer utils.

"""
from core.transport.local import LocalTransport

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


def TransportFactory(type):
	"""
	Returns a Transport instance.

	"""
	transport_class = {
		'local': LocalTransport}
	
	return transport_class[type]()
