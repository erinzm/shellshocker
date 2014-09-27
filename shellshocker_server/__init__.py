from flask import Flask
#from shellshocker_server.saferproxyfix import SaferProxyFix
from raven.contrib.flask import Sentry

import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
try:
  if os.environ['SECRET_KEY'] is not None:
    app.config['USE_SENTRY'] = True
    app.config['SENTRY_DSN'] = os.environ['SENTRY_DSN']
except KeyError:
  app.config['USE_SENTRY'] = False

if app.config['USE_SENTRY']:
  sentry = Sentry(app)

import shellshocker_server.views
