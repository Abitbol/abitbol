# -*- coding: utf-8 -*-
"""
GLPI API views.

"""

from api.rest.utils import *
from connectors.glpi.api.rest.urls import urls
import web

__author__ = "Jérémy Subtil"
__email__ = "jeremy.subtil@smile.fr"


class LinkJira:
	"""
	Links GLPI tickets to JIRA ones.

	"""
	def POST(self):
		"""
		Asks JIRA to link the given GLPI ticket to the JIRA one.

		Arguments:
		  * glpi_ticket_id		the GLPI ticket ID
		  * jira_ticket_id		the JIRA ticket ID

		"""
		data = web.input()
		required_args = ['glpi_ticket_id', 'jira_ticket_id']

		try:
			check_required_args(required_args, data)
		except RuntimeError as e:
			return render_error(str(e))

		return render_success()


app_glpi = web.application(urls, locals())
