from flask import Flask
#from shellshocker_server.saferproxyfix import SaferProxyFix
from raven.contrib.flask import Sentry
from flask.ext.analytics import Analytics

import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
try:
  if os.environ['SECRET_KEY'] is not None:
    app.config['USE_SENTRY'] = True
    app.config['SENTRY_DSN'] = os.environ['SENTRY_DSN']
except KeyError:
  app.config['USE_SENTRY'] = False

try:
  app.config['GOOGLE_ANALYTICS_ID'] = os.environ['GOOGLE_ANALYTICS_ID']
except KeyError:
  pass

sentry = Sentry(app)
analytics = Analytics(app)

import shellshocker_server.views
