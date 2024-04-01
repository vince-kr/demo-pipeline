import eggs
import datetime
import unittest


class TestEggSale(unittest.TestCase):
    """Ensure that the EggSale class behaves as expected"""

    def setUp(self) -> None:
        self.egg_sale = eggs.EggSale(6, 200)

    def test_sanity(self) -> None:
        """Ensure that self reference and unittest pkg exist"""
        self.assertTrue(True)

    def test_buyerAndDateMatchDefaultArguments(self) -> None:
        """When creating an EggSale object without a buyer or sale date
        Then buyer and sale date are assigned default values"""
        expected_buyer = "Unnamed"
        expected_saledate = datetime.date.today()
        actual_buyer = self.egg_sale.buyer
        actual_saledate = self.egg_sale.sale_date
        self.assertEqual(expected_buyer, actual_buyer)
        self.assertEqual(expected_saledate, actual_saledate)

    def test_valuePerEggIsCalculated(self) -> None:
        """When creating an EggSale object
        Then the per_egg method returns the correct value"""
        expected = 1/3
        actual = self.egg_sale.per_egg()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
