import unittest

import basket_pricer


class TestShoppingBasketPrice(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_basket_empty_true(self):
        basket = {}
        response = basket_pricer.is_basket_empty(basket)
        self.assertTrue(response)

    def test_is_basket_empty_false(self):
        basket = {
            'Baked Beans': 2,
            'Biscuits': 1,
            'Sardines': 2
        }
        response = basket_pricer.is_basket_empty(basket)
        self.assertFalse(response)

    def test_is_catalogue_empty_true(self):
        catalogue = {}
        response = basket_pricer.is_catalogue_empty(catalogue)
        self.assertTrue(response)

    def test_is_catalogue_empty_false(self):
        catalogue = {
            'Baked Beans': 2,
            'Biscuits': 1,
            'Sardines': 2
        }
        response = basket_pricer.is_catalogue_empty(catalogue)
        self.assertFalse(response)
