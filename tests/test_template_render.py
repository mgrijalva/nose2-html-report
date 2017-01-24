import unittest
from jinja2 import Template

from nose2_html_report.render import render_template


class TemplateRenderingTests(unittest.TestCase):
    def test_template_render(self):
        template = Template('<p>This is a really {{ simple }} template.</p> {{ stamp }}')
        context = {
            'simple': 'woot',
            'stamp': '2016-01-01'
        }
        rendered_template = render_template(template, context)
        self.assertEqual(rendered_template, '<p>This is a really woot template.</p> 2016-01-01')
