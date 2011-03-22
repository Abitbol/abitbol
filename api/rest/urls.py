# -*- coding: utf-8 -*-
"""
Global API URLs.

"""

from api.rest.glpi.views import app_glpi

__author__ = "Jérémy Subtil"
__email__ = "jeremy.subtil@smile.fr"


urls = (
		"/glpi", app_glpi
		)
