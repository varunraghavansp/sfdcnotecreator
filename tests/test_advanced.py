# -*- coding: utf-8 -*-

from .context import sfdcnotecreator

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_positive(self):
        sfdcnotecreator.core.processnotes


if __name__ == '__main__':
    unittest.main()
