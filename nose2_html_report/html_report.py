import json
import logging
import os
import traceback
from nose2.events import Plugin
from datetime import datetime

from .render import load_template, render_template

logger = logging.getLogger(__name__)


class HTMLReporter(Plugin):
    configSection = 'html-report'
    commandLineSwitch = (None, 'html-report', 'Generate an HTML report containing test results')

    def __init__(self, *args, **kwargs):
        super(HTMLReporter, self).__init__(*args, **kwargs)
        self.summary_stats = {'total': 0}
        self.test_results = []

        self._config = {
            'report_path': os.path.realpath(self.config.as_str('path', default='report.html')),
            'template': os.path.join(os.path.dirname(__file__), 'templates', 'report.html')
        }

    def _sort_test_results(self):
        return sorted(self.test_results, key=lambda x: x['name'])

    def _generate_search_terms(self):
        """
        Map search terms to what test case(s) they're related to

        Returns:
            dict: maps search terms to what test case(s) it's relevant to

        Example:
        {
            '12034': ['ui.tests.TestSomething.test_hello_world'],
            'buggy': ['ui.tests.TestSomething.test_hello_world', 'ui.tests.TestSomething.buggy_test_case'],
            'ui.tests.TestAnother.test_fail': ['ui.tests.TestAnother.test_fail']
        }
        """
        search_terms = {}

        for test_result in self.test_results:
            # search for the test name itself maps to the test case
            search_terms[test_result['name']] = test_result['name']

            if test_result['description']:
                for token in test_result['description'].split():
                    if token in search_terms:
                        search_terms[token].append(test_result['name'])
                    else:
                        search_terms[token] = [test_result['name']]

        return search_terms

    def testOutcome(self, event):
        """
        Reports the outcome of each test
        """
        test_case_import_path = event.test.id()
        test_case_doc = event.test._testMethodDoc

        formatted_traceback = None
        if event.outcome == 'failed':
            if event.exc_info:
                exception_type = event.exc_info[0]
                exception_message = event.exc_info[1]
                exception_traceback = event.exc_info[2]
                formatted_traceback = ''.join(traceback.format_exception(
                    exception_type, exception_message, exception_traceback))

        if event.outcome in self.summary_stats:
            self.summary_stats[event.outcome] += 1
        else:
            self.summary_stats[event.outcome] = 1
        self.summary_stats['total'] += 1

        self.test_results.append({
            'name': test_case_import_path,
            'description': test_case_doc,
            'result': event.outcome,
            'traceback': formatted_traceback
        })

    def afterSummaryReport(self, event):
        """
        After everything is done, generate the report
        """
        logger.info('Generating HTML report...')

        sorted_test_results = self._sort_test_results()

        context = {
            'test_report_title': 'Test Report',
            'test_summary': self.summary_stats,
            'test_results': sorted_test_results,
            'autocomplete_terms': json.dumps(self._generate_search_terms()),
            'timestamp': datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S UTC')
        }
        template = load_template(self._config['template'])
        rendered_template = render_template(template, context)
        with open(self._config['report_path'], 'w') as template_file:
            template_file.write(rendered_template)
