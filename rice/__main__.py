"""Rice.

Rice aids automating configuration files by combinding environment variables
with jinja2.

Usage:
    rice [-hv] [-f VAR] FILE ...

Options:
  -h --help     Show this screen.
  -v --version  Show version.
  -f --file     Load envrionment variables from file
"""

import dotenv
from docopt import docopt
from .utils import template
from . import __version__

arguments = docopt(__doc__, version=__version__)
dotenv.load_dotenv()

if arguments["--file"]:
    dotenv.dotenv_values(arguments["VAR"])

template(arguments["FILE"])
