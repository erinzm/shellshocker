ShellShocker
============
[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/ArchimedesPi/shellshocker?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Stories in Ready](https://badge.waffle.io/ArchimedesPi/shellshocker.png?label=ready&title=Ready)](https://waffle.io/ArchimedesPi/shellshocker)
![Time to close issues](http://issuestats.com/github/ArchimedesPi/shellshocker/badge/issue?style=flat) ![Time to merge PRs](http://issuestats.com/github/ArchimedesPi/shellshocker/badge/pr?style=flat)

<img src="https://raw.githubusercontent.com/ArchimedesPi/shellshocker/master/shellshocker_server/static/images/shellshock-logo.png" alt="ShellShocker" align="right" />

If you don't know what the ShellShock Bash exploit is, you should probably Google it.
Now that you know...

### What is this for?
ShellShocker tests a website for vulnerability to the ShellShock bug.
There's a command-line tool for doing testing, and a deployable Flask-powered
ShellShock testing website (punch in the URL of your server, we'll tell you
what's vulnerable)
It can act as a testing toolkit for ShellShock for researchers as well!

### How do I use it?
ShellShocker has two different ways of being run:
* a command line utility, and
* a web interface, which ~~is~~ was deployed to Heroku

#### Usage of the CLI:
<pre>
Usage: shellshocker.py [OPTIONS] URL

  Test the URL `URL` for ShellShock vulnerability.

Options:
  -v, --verbose                   Make the tester more verbose for debugging
  -c, --command TEXT              Command to inject into the payload
  -p, --payload [traditional|new]
                                  Choose between the original bug and the new
                                  one
  --help                          Show this message and exit.
</pre>

### Hacking on the code
`vagrant up`.
In your Vagrant enviroment, everything'll be set up. If it somehow isn't...
`vagrant provision`.

If you're not in the virtualenv, activate it: `. env/bin/activate`.

**SEND ME PRs!** *Please!* I can't add every feature people want ;)

### Authors
* Liam (ArchimedesPi)
