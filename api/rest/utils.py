# -*- coding: utf-8 -*-
"""
REST API utils.

"""

import json

import web

__author__ = "Jérémy Subtil"
__email__ = "jeremy.subtil@smile.fr"


class Response(object):
	"""
	Response renderer.

	"""
	def render(self, msg):
		raise NotImplementedError()

class JsonResponse(Response):
	"""
	Renders the response in JSON format.

	"""
	def render(self, msg):
		return json.dumps(msg)

response_renderer = JsonResponse()

def render_success():
	"""
	Renders a success response.

	"""
	response = {'success': True}
	return response_renderer.render(response)

def render_error(msg):
	"""
	Renders an error response.

	"""
	web.BadRequest()
	response = {'error': True, 'msg': msg}
	return response_renderer.render(response)


def check_required_args(required_args, args):
	"""
	Checks whether the required args are defined.

	"""
	required_args = frozenset(required_args)
	args = frozenset(args)
	if not required_args <= args:
		missing_args = required_args - args
		missing_args_str = reduce(lambda a, b: "%s, %s" % (a, b), missing_args)
		raise RuntimeError("Missing parameters: %s" % missing_args_str)
