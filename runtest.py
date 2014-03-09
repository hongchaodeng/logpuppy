#!/usr/bin/env python

import unittest

from test.alert_test import TestAlertingLogic

suite = unittest.TestLoader().loadTestsFromTestCase(TestAlertingLogic)
unittest.TextTestRunner(verbosity=2).run(suite)
