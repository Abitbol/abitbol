"""
Global API URLs.

"""

from connectors.glpi.api.rest.views import app_glpi

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


urls = (
		"/glpi", app_glpi
		)
