# -*- coding: utf-8 -*-
"""
Abitbol's main module.
"""

from xmpp import Client
from xmpp import Message

__author__ = "Jérémy Subtil"
__email__ = "jeremy.subtil@smile.fr"


def test():

	client = Client('localhost')

	def message_handler(conn, mess_node):
		client.send(Message('tim@localhost', 'reponse!'))

	if not client.connect(server=('127.0.0.1', 5222)):
		raise IOError('Can not connect to server.')

	if not client.auth('abitbol', 'abitbol', 'abitbol'):
		raise IOError('Can not auth with server.')

	client.RegisterHandler('message', message_handler)

	client.sendInitPresence()
	
	client.send(Message('tim@localhost', 'Test message'))

	while 1:
		client.Process(1)

#	client.sendPresence(typ='unavailable')
#	client.disconnect()


def main():
	test
