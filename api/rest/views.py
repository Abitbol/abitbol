# -*- coding: utf-8 -*-
"""
Global API views.

"""

from api.rest.urls import urls
import web

__author__ = "Jérémy Subtil"
__email__ = "jeremy.subtil@smile.fr"


api_app = web.application(urls, locals())
