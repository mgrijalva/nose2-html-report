"""
    Functions to generate the HTML output
"""
from jinja2 import Template

def generate_report(out_filename, template_file, context):
    """
    Generate an HTML test report.

    Args:
        out_filename (str): where the generated file should be output to
        template_file (str): path to the Jinja2 template file
        context (dict): the context to pass to the template
    """
    template = Template(open(template_file).read())
    rendered_template = template.render(context)
    with open(out_filename, 'w') as f:
        f.write(rendered_template)
