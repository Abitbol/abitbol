"""
JIRA models.

"""

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


class Ticket:
	"""
	A JIRA ticket.
	
	"""
	def __init__(self, id):
		self.id = id
