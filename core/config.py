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
	
	def loadFromArgs(self, options):
		pass

	def get(self, key):
		return self.storage[key]
