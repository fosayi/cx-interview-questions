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

    def test_get_total_price(self):
        sub_total = 5.66
        discount = 0.66
        response = basket_pricer.get_total_price(sub_total, discount)
        self.assertEqual(response, 5.00)

    def test_get_total_price_2(self):
        sub_total = 5.66
        discount = 5.66
        response = basket_pricer.get_total_price(sub_total, discount)
        self.assertEqual(response, 0.00)

    def test_get_total_price_raises_Exception(self):
        sub_total = 5.66
        discount = 5.67
        self.assertRaises(ValueError, basket_pricer.get_total_price,
                          sub_total, discount)

    def test_get_percent_type_discount_1(self):
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
        offers = {
            'Baked Beans': ('PERCENT_OFFER', '50'),
            'Biscuits': ('PERCENT_OFFER', '0'),
            'Sardines': ('PERCENT_OFFER', '25'),
        }
        response = basket_pricer.get_total_discount(basket, offers, catalogue)
        self.assertEqual(response, 1.94)

    def test_get_percent_type_discount_2(self):
        # It's possible that there are offers on products which
        # are no longer in the catalogue.
        catalogue = {
            'Baked Beans': 0.99,
            'Biscuits': 1.20,
            'Shampoo(Small)': 2.00,
            'Shampoo(Medium)': 2.50,
            'Shampoo(Large)': 3.50
        }
        basket = {
            'Baked Beans': 2,
            'Biscuits': 1,
        }
        offers = {
            'Baked Beans': ('PERCENT_OFFER', '50'),
            'Biscuits': ('PERCENT_OFFER', '0'),
            'Sardines': ('PERCENT_OFFER', '25'),
        }
        response = basket_pricer.get_total_discount(basket, offers, catalogue)
        self.assertEqual(response, 0.99)

    def test_get_percent_type_discount_3(self):
        # It's also possible that there are items in the catalogue with
        # no offers, or multiple offers.
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
        offers = {
            'Biscuits': ('PERCENT_OFFER', '0'),
            'Sardines': ('PERCENT_OFFER', '0'),
        }
        response = basket_pricer.get_total_discount(basket, offers, catalogue)
        self.assertEqual(response, 0.00)

    def test_check_catalogue_item_have_negative_price_raises_Exception(self):
        catalogue = {
            'Baked Beans': -0.99,
        }
        self.assertRaises(
            ValueError, basket_pricer.check_catalogue_item_have_negative_price,
            catalogue)

    def test_check_catalogue_item_have_negative_price_passes(self):
        catalogue = {
            'Baked Beans': 0.99,
        }
        self.assertIsNone(
            basket_pricer.check_catalogue_item_have_negative_price(catalogue))

    def test_validate_offers_without_value_raises_type(self):
        offers = {
            'Biscuits': 'INVALID_OFFER',
        }
        self.assertRaises(TypeError, basket_pricer.validate_offers, offers)

    def test_validate_offers_invalid_type_raises_type(self):
        offers = {
            'Sardines': ('INVALID_OFFER', '0'),
        }
        self.assertRaises(TypeError, basket_pricer.validate_offers, offers)

    def test_validate_percent_offer_value_invalid_number_raises_error(self):
        self.assertRaises(TypeError,
                          basket_pricer.validate_percent_offer_value, "blah")

    def test_validate_percent_offer_value_invalid_range_raises_error(self):
        self.assertRaises(ValueError,
                          basket_pricer.validate_percent_offer_value, "300")

    def test_validate_offers_success(self):
        offers = {
            'Sardines': ('PERCENT_OFFER', '0'),
        }
        self.assertIsNone(basket_pricer.validate_offers(offers))