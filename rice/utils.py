import os
from glob import glob
from jinja2 import Template


def deglob(paths):
    """Resolve unix globs

    Args:
        paths: A list of file paths to deglob

    Returns:
        Yields all the possible file paths
    """
    for path in paths:
        for file in glob(path):
            yield file


def template(paths):
    """Render given template files

    Note: This will rewrite the file with the rendered version.

    Args:
        paths: An array of file paths to render
    """
    for path in deglob(paths):
        with open(path, "r+") as fp:
            print(path)
            template = Template(fp.read())
            fp.seek(0)
            fp.write(template.render(os.environ))
            fp.truncate()
