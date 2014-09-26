#!/usr/bin/env python

"""
ShellShocker CLI
================
The CLI for ShellShocker.
Interfaces to **shellshocker.exploits.ShellShocker**, a ShellShock exploiter
"""

from shellshocker.exploits import ShellShocker # Import a shellshock payload generator
# and delivery device.
import click # Click is Armin Ronacher's new CLI framework. It's awesomesauce.

@click.command()
@click.argument('url')
@click.option('--verbose', is_flag=True)
# I'll add payload, etc here later.
def test_site(url, verbose):
  """
  Command to test the site
  """
  click.echo("Testing {url} with a standard payload using ShellShocker".format(url=url))

  if verbose:
    click.echo("Creating instance of exploit on {url}".format(url=url))
  # Create a instance of the exploiter
  shocker = ShellShocker({'url': url})

  if verbose:
    click.echo("Sending exploit to {url}".format(url=url))

  # Is it exploitable?
  exploitable = shocker.exploitable()

  click.echo("{url} is exploitable".format(url=url) if exploitable else "{url} is not exploitable".format(url=url))

if __name__ == '__main__':
  """
  If this is being run as a script
  """
  test_site()
