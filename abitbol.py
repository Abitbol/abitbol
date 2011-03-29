#!/usr/bin/env python

from core.config import Settings
from core.server import server
from optparse import OptionParser

__author__ = "Jeremy Subtil"
__email__ = "jeremy.subtil@smile.fr"


parser = OptionParser()

parser.add_option("-c", "--config", action="store", type="string",
				  dest="config_filename", default="config.cfg",
				  help="the configuration file to use")

(options, args) = parser.parse_args()

settings = Settings()
settings.loadFromFile(options.config_filename)
settings.loadFromArgs(options)

server.configure(settings)
server.run()
