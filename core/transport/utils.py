"""
Transport layer utils.

"""

from core.transport.common import Transport

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


def TransportFactory(type):
	"""
	Returns a Transport instance.

	"""
	for cls in Transport.__subclasses__():
		if cls.isIdentifiedBy(type):
			return cls()
	raise ValueError
