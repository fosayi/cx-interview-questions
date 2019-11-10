from basket_pricer import get_basket_price

CATALOGUE = {
        'Baked Beans': 0.99,
        'Biscuits': 1.20,
        'Sardines': 1.89,
        'Shampoo(Small)': 2.00,
        'Shampoo(Medium)': 2.50,
        'Shampoo(Large)': 3.50
}


OFFERS = {
        'Baked Beans': ('PERCENT_OFFER', '50'),
        'Biscuits': ('PERCENT_OFFER', '0'),
        'Sardines': ('PERCENT_OFFER', '25'),
}


def run():

    basket = {
        'Baked Beans': 2,
        'Biscuits': 1,
        'Sardines': 2
    }

    result = get_basket_price(basket, CATALOGUE, OFFERS)
    print(result)


if __name__ == "__main__":
    run()
