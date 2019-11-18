from jinja2 import Environment, PackageLoader, select_autoescape

def get_template():
    """\
    Returns the default narator template from the package.
    """
    env = Environment(
        loader=PackageLoader('narator', 'templates'),
        autoescape=select_autoescape(['txt'])
    )

    return env.get_template('template.txt')
