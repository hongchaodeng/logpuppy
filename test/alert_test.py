import unittest

from logmonitor.loganalyzer import LogAnalyzer

class TestAlertingLogic(unittest.TestCase):
    def setUp(self):
        pass

    #Not alerting receives Low traffic. Nothing happens.
    def test_notalerting_receive_low(self):
        analyzer = LogAnalyzer("1")
        msg = analyzer.analyze_alert([])

        self.assertEqual(msg, "")
        self.assertFalse(analyzer.alerting)

    #Not alerting receives High traffic. Become alerting and add alert message.
    def test_notalerting_receive_high(self):
        analyzer = LogAnalyzer("1")
        msg = analyzer.analyze_alert(["log1", "log2"])

        self.assertEqual(msg[:4], "High")
        self.assertTrue(analyzer.alerting)

    #Alerting receives High traffic. Nothing happens.
    def test_alerting_receive_high(self):
        analyzer = LogAnalyzer("1")
        analyzer.analyze_alert(["log1", "log2"])
        # now becomes alerting and average 2 with 1 count
        msg = analyzer.analyze_alert(["log1", "log2"])

        self.assertEqual(msg, "")
        self.assertTrue(analyzer.alerting)

    #Alerting receives Low traffic. Become not alerting and add a recovery message.
    def test_alerting_receive_low(self):
        analyzer = LogAnalyzer("1")
        analyzer.analyze_alert(["log1", "log2"])
        # now becomes alerting and average 2 with 1 count
        analyzer.analyze_alert([])
        msg = analyzer.analyze_alert([])
        # (2 / 3) < 1
        recover_msg_prefix = "Traffic recovered"

        self.assertEqual(msg[:len(recover_msg_prefix)], recover_msg_prefix )
        self.assertFalse(analyzer.alerting)
