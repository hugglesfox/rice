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
from rice import template


if __name__ == "__main__":
    arguments = docopt(__doc__, version="0.1.0")
    template(arguments["FILE"])
