"""
Business logic linking JIRA & GLPI.

"""

from common.connectors.glpi.models import Ticket as GlpiTicket
from common.connectors.jira.models import Ticket as JiraTicket
from connectors.glpi.actions.jira import link_jira
from core.server import server

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


def link_to_jira(glpi_id, jira_id):
	"""
	Links a GLPI ticket to a JIRA one.

	"""
	glpi_ticket = GlpiTicket(glpi_id)
	jira_ticket = JiraTicket(jira_id)

	remote_action = {'ns': 'glpi', 'action': 'link_glpi', 'kwargs': {
		'jira_id': jira_id,
		'glpi_ticket': glpi_ticket}}
	server.transport.send('jira', remote_action)

	link_jira(glpi_ticket, jira_ticket)
