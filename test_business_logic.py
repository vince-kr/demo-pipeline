import business_logic
import datetime
import unittest


class TestBusinessLogic(unittest.TestCase):
    def test_sanity(self) -> None:
        self.assertTrue(True)

    def test_givenDatetimeObject_logicReturnsDateString(self) -> None:
        expected = "Saturday 16 March 2024"
        actual = business_logic.long_date(datetime.date.fromisoformat("2024-03-16"))
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()