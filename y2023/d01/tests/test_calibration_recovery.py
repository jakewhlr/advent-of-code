import unittest
from calibration_recovery import recover_calibration_value, recover_total_calibration

class TestCalibrationRecoveryInts(unittest.TestCase):
    def test_recover_calibration_value(self):
        self.assertEqual(recover_calibration_value("1abc2"), 12)
        self.assertEqual(recover_calibration_value("pqr3stu8vwx"), 38)
        self.assertEqual(recover_calibration_value("a1b2c3d4e5f"), 15)
        self.assertEqual(recover_calibration_value("treb7uchet"), 77)
        self.assertEqual(recover_calibration_value("123456789"), 19)
        self.assertEqual(recover_calibration_value("abcdefg"), 0)

    def test_recover_total_calibration(self):
        test_input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        self.assertEqual(recover_total_calibration(test_input), 142)

class TestCalibrationRecoveryStrs(unittest.TestCase):
    def test_recover_calibration_value(self):
        self.assertEqual(recover_calibration_value("two1nine"), 29)
        self.assertEqual(recover_calibration_value("eightwothree"), 83)
        self.assertEqual(recover_calibration_value("abcone2threexyz"), 13)
        self.assertEqual(recover_calibration_value("xtwone3four"), 24)
        self.assertEqual(recover_calibration_value("4nineeightseven2"), 42)
        self.assertEqual(recover_calibration_value("zoneight234"), 14)
        self.assertEqual(recover_calibration_value("7pqrstsixteen"), 76)

    def test_recover_total_calibration(self):
        test_input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        self.assertEqual(recover_total_calibration(test_input), 142)


if __name__ == '__main__':
    unittest.main()






