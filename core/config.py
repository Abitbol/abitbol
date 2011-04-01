"""
Configuration management.

"""

from ConfigParser import SafeConfigParser

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


class Settings(object):
	"""
	Stores the application settings.

	"""
	storage = dict()

	def loadFromFile(self, filename):
		config = SafeConfigParser()
		config.read(filename)

		self.storage['transport_type'] = config.get('General', 'transport')
		self.storage['xmpp_domain'] = config.get('XMPP', 'domain')
		self.storage['xmpp_host'] = config.get('XMPP', 'host')
		self.storage['xmpp_port'] = config.get('XMPP', 'port')
		self.storage['xmpp_user'] = config.get('XMPP', 'user')
		self.storage['xmpp_password'] = config.get('XMPP', 'password')
		self.storage['xmpp_presence'] = config.get('XMPP', 'presence')
	
	def loadFromArgs(self, options):
		pass

	def get(self, key):
		return self.storage[key]
