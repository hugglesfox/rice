import os
from jinja2 import Template


def template(files):
    """Render a given template files

    Args:
        files: An array of file paths to render
    """
    for file in files:
        with open(file, "r+") as fp:
            template = Template(fp.read())
            fp.seek(0)
            fp.write(template.render(os.environ))
            fp.truncate()
