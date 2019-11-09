import unittest

import basket_pricer


class TestShoppingBasketPrice(unittest.TestCase):

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
            'Baked Beans': 0.99,
            'Biscuits': 1.20,
            'Sardines': 1.89,
            'Shampoo(Small)': 2.00,
            'Shampoo(Medium)': 2.50,
            'Shampoo(Large)': 3.50
        }
        response = basket_pricer.is_catalogue_empty(catalogue)
        self.assertFalse(response)

    def test_are_basket_items_in_catalogue_false(self):
        catalogue = {}
        basket = {
            'Baked Beans': 2,
            'Biscuits': 1,
            'Sardines': 2
        }
        response = basket_pricer.are_basket_items_in_catalogue(
            basket, catalogue)
        self.assertFalse(response)

    def test_are_basket_items_in_catalogue_true(self):
        catalogue = {
            'Baked Beans': 0.99,
            'Biscuits': 1.20,
            'Sardines': 1.89,
            'Shampoo(Small)': 2.00,
            'Shampoo(Medium)': 2.50,
            'Shampoo(Large)': 3.50
        }
        basket = {
            'Baked Beans': 2,
            'Biscuits': 1,
            'Sardines': 2
        }
        response = basket_pricer.are_basket_items_in_catalogue(
            basket, catalogue)
        self.assertTrue(response)

    def test_get_sub_total_1(self):
        catalogue = {
            'Baked Beans': 0.99,
            'Biscuits': 1.20,
            'Sardines': 1.89,
            'Shampoo(Small)': 2.00,
            'Shampoo(Medium)': 2.50,
            'Shampoo(Large)': 3.50
        }
        basket = {
            'Baked Beans': 2,
            'Biscuits': 1,
            'Sardines': 2
        }
        response = basket_pricer.get_sub_total(basket, catalogue)
        self.assertEqual(response, 6.96)

    def test_get_sub_total_2(self):
        catalogue = {}
        basket = {}
        response = basket_pricer.get_sub_total(basket, catalogue)
        self.assertEqual(response, 0.00)
