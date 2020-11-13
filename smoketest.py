from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionTest
from searchtest import SearchTest

assertion_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([search_test, assertion_test])

kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)