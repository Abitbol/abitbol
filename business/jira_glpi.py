# -*- coding: utf-8 -*-
"""
Business logic linking JIRA & GLPI.

"""

from common.connectors.glpi.models import Ticket as GlpiTicket
from common.connectors.jira.models import Ticket as JiraTicket
from connectors.glpi.actions import jira as glpi_actions
from connectors.jira.actions import glpi as jira_actions

__author__ = "Jérémy Subtil"
__email__ = "jeremy.subtil@smile.fr"


def link_tickets(glpi_id, jira_id):
	"""
	Links a GLPI ticket and a JIRA one.

	"""
	glpi_ticket = GlpiTicket(glpi_id)
	jira_ticket = JiraTicket(jira_id)

	jira_actions.link_glpi(jira_ticket, glpi_ticket)
	glpi_actions.link_jira(glpi_ticket, jira_ticket)
