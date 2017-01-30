import sys
import unittest
from nose2 import events, result
from nose2.session import Session

from nose2_html_report.html_report import HTMLReporter


def _test_func():
    """
    A dummy test function.
    Bug 1234
    """
    pass


def _test_func_fail():
    """
    Test case that fails.
    """
    assert 1 == 2


for func in [_test_func, _test_func_fail]:
    setattr(func, '_testMethodDoc', func.__doc__)
setattr(_test_func, 'id', lambda: _test_func.__name__)
setattr(_test_func_fail, 'id', lambda: _test_func_fail.__name__)


def create_plugin_instance():
    return HTMLReporter(session=Session())


class NosePluginTests(unittest.TestCase):
    def test_outcome_processing_successful_test(self):
        test_function = _test_func
        ev = events.TestOutcomeEvent(test_function, None, result.PASS)

        reporter = create_plugin_instance()
        reporter.testOutcome(ev)

        self.assertEqual(len(reporter.test_results), 1, 'Actual contents: %s' % reporter.test_results)
        test_result = reporter.test_results[0]
        self.assertEqual(test_result['result'], result.PASS)
        self.assertEqual(test_result['name'], test_function.__name__)
        self.assertEqual(test_result['description'], test_function.__doc__)
        self.assertIsNone(test_result['traceback'])

    def test_outcome_with_failed_test(self):
        test_function = _test_func_fail
        try:
            test_function()
        except:
            exc_info = sys.exc_info()
        ev = events.TestOutcomeEvent(test_function, None, result.FAIL, exc_info=exc_info)

        reporter = create_plugin_instance()
        reporter.testOutcome(ev)

        self.assertEqual(len(reporter.test_results), 1, 'Actual contents: %s' % reporter.test_results)
        test_result = reporter.test_results[0]
        self.assertEqual(test_result['result'], result.FAIL)
        self.assertEqual(test_result['name'], test_function.__name__)
        self.assertEqual(test_result['description'], test_function.__doc__)
        self.assertIsNotNone(test_result['traceback'])
        self.assertIn('assert 1 == 2', test_result['traceback'])

    def test_summary_stats_new_test(self):
        ev = events.TestOutcomeEvent(_test_func, None, result.PASS)
        reporter = create_plugin_instance()
        reporter.testOutcome(ev)

        self.assertIn('passed', reporter.summary_stats)
        self.assertEqual(reporter.summary_stats['passed'], 1)

    def test_summary_stats_increment(self):
        ev = events.TestOutcomeEvent(_test_func, None, result.PASS)
        reporter = create_plugin_instance()
        reporter.summary_stats['passed'] = 10
        reporter.testOutcome(ev)

        self.assertIn('passed', reporter.summary_stats)
        self.assertEqual(reporter.summary_stats['passed'], 11)

    def test_summary_stats_total(self):
        ev = events.TestOutcomeEvent(_test_func, None, result.PASS)
        reporter = create_plugin_instance()
        for i in range(0, 20):
            reporter.testOutcome(ev)

        self.assertIn('passed', reporter.summary_stats)
        self.assertEqual(reporter.summary_stats['total'], 20)
