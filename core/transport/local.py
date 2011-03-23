# -*- coding: utf-8 -*-
"""
Local transport.

"""

__author__ = "Jérémy Subtil"
__email__ = "jeremy.subtil@smile.fr"


class LocalTransport(object):
	"""
	Implements the local transport.

	"""
	def send(self, destination, action):
		receptor.handle(destination, action)

class ReceptionHandler(object):
	"""
	Handles local message reception.

	"""
	def handle(self, destination, action):
		module_name = "connectors.%s.actions.%s" % (destination, action['ns'])
		exec "import %s" % module_name
		callback_name = "%s.%s" % (module_name, action['action'])
		eval(callback_name)(**action['kwargs'])
		
receptor = ReceptionHandler()
