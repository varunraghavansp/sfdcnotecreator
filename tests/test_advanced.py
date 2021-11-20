# -*- coding: utf-8 -*-

from .context import sfdcnotecreator

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_positive(self):
        self.assertEqual(sfdcnotecreator.core.processnotes,0)


if __name__ == '__main__':
    unittest.main()
