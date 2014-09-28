from __future__ import print_function
import sys
from flask import render_template, flash, jsonify, redirect, Response,session, url_for, request, g
from shellshocker_server import app, sentry
from shellshocker.exploits import ShellShocker
from shellshocker.url import verify_url
from raven.contrib.flask import Sentry
import logging


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/shockit/', methods=['GET', 'POST'])
def shockit():
  websiteUrl = request.form.get('websiteUrl', type=str)
  if verify_url(websiteUrl):
    urlsToCheck = [websiteUrl]
    if request.form.get('commonVulnerableRoutes') is None:
      commonVulnerableRoutes = False
    elif request.form.get('commonVulnerableRoutes') == "on":
      commonVulnerableRoutes = True
    if commonVulnerableRoutes == True:
      for r in ShellShocker.commonVulnerableRoutes:
        urlsToCheck.append(websiteUrl + r)

    #if app.config['USE_SENTRY']:
    #  sentry.captureMessage('IP {ip} requested exploit of {url} with commonVulnerableRoutes: {cvr}'.format(ip='removed',
    #    url=websiteUrl,
    #    cvr=commonVulnerableRoutes),
    #    level=logging.INFO
    #    )

    print('IP {ip} requested exploit of {url} with commonVulnerableRoutes: {cvr}'.format(ip='removed',
        url=websiteUrl,
        cvr=commonVulnerableRoutes),
        file=sys.stderr)

    return render_template('shockit.html',
      websiteUrl = websiteUrl,
      commonVulnerableRoutes = commonVulnerableRoutes,
      urlsToCheck = urlsToCheck,
      headersToCheck = ShellShocker.commonVulnerableHeaders,
      )
  flash('Baaaad URL. Check it and fix it :\'(')
  return redirect(url_for('index'))

@app.route('/exploitable', methods=['POST'])
def exploitable():
  websiteUrl = request.form.get('websiteUrl')
  header = request.form.get('header')
  # print websiteUrl + ' :: ' + header
  shocker = ShellShocker({'url': websiteUrl, 'payload_headers': [header]})
  exploitable = shocker.exploitable()
  return jsonify(exploitable=exploitable)
