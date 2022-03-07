"""Rice.

Rice aids automating configuration files by combinding environment variables
with jinja2.

Usage:
    rice [-hvo] FILE ...

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""

from docopt import docopt
from .utils import template
from . import __version__

arguments = docopt(__doc__, version=__version__)
template(arguments["FILE"])
