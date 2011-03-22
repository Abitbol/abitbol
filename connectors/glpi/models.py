# -*- coding: utf-8 -*-
"""
GLPI models.

"""

__author__ = "Jérémy Subtil"
__email__ = "jeremy.subtil@smile.fr"


class Ticket:
	"""
	A GLPI ticket.
	
	"""
	def __init__(self, id):
		self.id = id
