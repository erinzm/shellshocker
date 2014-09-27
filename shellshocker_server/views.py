from flask import render_template, flash, jsonify, redirect, Response,session, url_for, request, g
from shellshocker_server import app
from shellshocker.exploits import ShellShocker
from shellshocker.url import verify_url

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/shockit/', methods=['GET', 'POST'])
def shockit():
  websiteUrl = request.form.get('websiteUrl', type=str)
  print websiteUrl
  if verify_url(websiteUrl):
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
  flash('Baaaad URL. Check it and fix it :\'(')
  return redirect(url_for('index'))

@app.route('/exploitable', methods=['POST'])
def exploitable():
  websiteUrl = request.form.get('websiteUrl')
  shocker = ShellShocker({'url': websiteUrl})
  exploitable = shocker.exploitable()
  return jsonify(exploitable=exploitable)
