from flask import render_template, flash, jsonify, redirect, session, url_for, request, g
from shellshocker_server import app
from shellshocker.exploits import ShellShocker

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/shockit/', methods=['GET', 'POST'])
def shockit():
  websiteUrl = request.form.get('websiteUrl')
  urlsToCheck = [websiteUrl]
  if request.form.get('commonVulnerableRoutes') is None:
    commonVulnerableRoutes = False
  elif request.form.get('commonVulnerableRoutes') == "on":
    commonVulnerableRoutes = True
  if commonVulnerableRoutes == True:
    for r in ShellShocker.commonVulnerableRoutes:
      urlsToCheck.append(websiteUrl + r)
  return render_template('shockit.html',
    websiteUrl = websiteUrl,
    commonVulnerableRoutes = commonVulnerableRoutes,
    urlsToCheck = urlsToCheck
    )

@app.route('/exploitable', methods=['POST'])
def exploitable():
  websiteUrl = request.form.get('websiteUrl')
  shocker = ShellShocker({'url': websiteUrl})
  exploitable = shocker.exploitable()
  return jsonify(exploitable=exploitable)
