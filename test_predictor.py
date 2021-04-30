import unittest
from predictor import predictor, plate_validation, date_validation, time_validation

class TestPredictor(unittest.TestCase):
    def test_car_can_transit(self):
        # monday tests
        self.assertTrue(predictor("abc1231", "26/04/2021", "19:40"))
        self.assertTrue(predictor("abc1232", "26/04/2021", "19:40"))

        # tuesday tests
        self.assertTrue(predictor("abc1233", "27/04/2021", "19:40"))
        self.assertTrue(predictor("abc1234", "27/04/2021", "19:40"))

        # wednesday tests
        self.assertTrue(predictor("abc1235", "28/04/2021", "19:40"))
        self.assertTrue(predictor("abc1236", "28/04/2021", "19:40"))

        # thursday tests
        self.assertTrue(predictor("abc1237", "29/04/2021", "19:40"))
        self.assertTrue(predictor("abc1238", "29/04/2021", "19:40"))

        # friday tests
        self.assertTrue(predictor("abc1239", "30/04/2021", "19:40"))
        self.assertTrue(predictor("abc1230", "30/04/2021", "19:40"))

        # saturday tests
        self.assertTrue(predictor("abc1231", "01/05/2021", "9:00"))
        self.assertTrue(predictor("abc1230", "01/05/2021", "19:00"))

        # sunday tests
        self.assertTrue(predictor("abc1231", "02/05/2021", "9:00"))
        self.assertTrue(predictor("abc1230", "02/05/2021", "19:00"))

    def test_car_cannot_transit(self):
        # monday tests
        self.assertFalse(predictor("abc1231", "26/04/2021", "19:00"))
        self.assertFalse(predictor("abc1232", "26/04/2021", "19:00"))

        # tuesday tests
        self.assertFalse(predictor("abc1233", "27/04/2021", "19:00"))
        self.assertFalse(predictor("abc1234", "27/04/2021", "19:00"))

        # wednesday tests
        self.assertFalse(predictor("abc1235", "28/04/2021", "19:00"))
        self.assertFalse(predictor("abc1236", "28/04/2021", "19:00"))

        # thursday tests
        self.assertFalse(predictor("abc1237", "29/04/2021", "19:00"))
        self.assertFalse(predictor("abc1238", "29/04/2021", "19:00"))

        # friday tests
        self.assertFalse(predictor("abc1239", "30/04/2021", "19:00"))
        self.assertFalse(predictor("abc1230", "30/04/2021", "19:00"))

    def test_correct_plate(self):
        self.assertTrue(plate_validation("abc123"))
        self.assertTrue(plate_validation("abc1234"))
        self.assertTrue(plate_validation("ABC123"))
        self.assertTrue(plate_validation("ABC1234"))

    def test_incorrect_plate(self):
        # plate length is incorrect
        self.assertFalse(plate_validation("abcde123456"))

        # plate first three characters contain numbers
        self.assertFalse(plate_validation("ab1234"))
        self.assertFalse(plate_validation("ab12345"))

        # plate last digits contain letters
        self.assertFalse(plate_validation("abcd12"))
        self.assertFalse(plate_validation("abcd123"))

    def test_correct_date(self):
        self.assertTrue(date_validation("29/04/2021"))

    def test_incorrect_date(self):
        self.assertFalse(date_validation("29-04-2021"))

    def test_correct_time(self):
        self.assertTrue(time_validation("09:30"))
        self.assertTrue(time_validation("9:30"))

    def test_incorrect_time(self):
        self.assertFalse(time_validation("19h30"))