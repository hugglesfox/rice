"""Rice.

Rice aids automating configuration files by combinding environment variables
with jinja2.

Usage:
    rice [-hv] FILE ...

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""

from docopt import docopt
from .template import template
from . import __version__

def main():
    """Required for application entrypoint"""
    arguments = docopt(__doc__, version=__version__)
    template(arguments["FILE"])

if __name__ == "__main__":
    main()
