from flask import render_template, flash, redirect, session, url_for, request, g
from shellshocker_server import app

@app.route('/', methods=['GET'])
def index():
  return  render_template('index.html')

@app.route('/shockit/', methods=['POST'])
def shockit():
  websiteUrl = request.form.get('websiteUrl')
  if request.form.get('commonVulnerableRoutes') is None:
    commonVulnerableRoutes = False
  elif request.form.get('commonVulnerableRoutes') == "on":
    commonVulnerableRoutes = True
  return 'URL is: ' + websiteUrl + ' commonVulnerableRoutes is: ' + str(commonVulnerableRoutes)
