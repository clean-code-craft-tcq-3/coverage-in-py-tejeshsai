import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
        self.assertTrue(typewise_alert.infer_breach(30, 20, 50) == 'NORMAL')
        self.assertTrue(typewise_alert.infer_breach(
            120, 70, 100) == 'TOO_HIGH')
        self.assertTrue(typewise_alert.infer_breach(10, 15, 30) == 'TOO_LOW')
        self.assertTrue(typewise_alert.infer_breach(60, 50, 55) == 'TOO_HIGH')
        self.assertTrue(typewise_alert.infer_breach(40, 35, 55) == 'NORMAL')

    def test_classify_temperature_breach(self):
        self.assertTrue(typewise_alert.classify_temperature_breach(
            'MED_ACTIVE_COOLING', 35) == 'NORMAL')
        self.assertTrue(typewise_alert.classify_temperature_breach(
            'MED_ACTIVE_COOLING', 45) == 'TOO_HIGH')
        self.assertTrue(typewise_alert.classify_temperature_breach(
            'MED_ACTIVE_COOLING', -1) == 'TOO_LOW')
        self.assertTrue(typewise_alert.classify_temperature_breach(
            'PASSIVE_COOLING', 35) == 'NORMAL')
        self.assertTrue(typewise_alert.classify_temperature_breach(
            'PASSIVE_COOLING', 45) == 'TOO_HIGH')
        self.assertTrue(typewise_alert.classify_temperature_breach(
            'PASSIVE_COOLING', -5) == 'TOO_LOW')
        self.assertTrue(typewise_alert.classify_temperature_breach(
            'HI_ACTIVE_COOLING', 42) == 'NORMAL')
        self.assertTrue(typewise_alert.classify_temperature_breach(
            'HI_ACTIVE_COOLING', 48) == 'TOO_HIGH')
        self.assertTrue(typewise_alert.classify_temperature_breach(
            'HI_ACTIVE_COOLING', -1) == 'TOO_LOW')


if __name__ == '__main__':
    # unittest.main()
    typewise_alert.check_and_alert('TO_EMAIL', 'MED_ACTIVE_COOLING', 40)
