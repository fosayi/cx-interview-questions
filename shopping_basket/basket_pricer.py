
VALID_OFFER_TYPES = ("PERCENT_OFFER", "MULTI_OFFER")


def is_basket_empty(basket):
    """
    Check if the shopping basket is empty

    :param basket: dict
    :return: bool
    """
    if not basket:
        return True
    return False


def check_catalogue_empty(catalogue):
    """
    Check if there are catalogue of products available

    :param catalogue: dict
    :return: None
    :raises: ValueError (if catalogue is empty)
    """
    if not catalogue:
        raise ValueError("Catalogue cannot be empty.")


def check_basket_items_in_catalogue(basket, catalogue):
    """
    Check that the items in the basket are in the catalogue

    :param basket: dict
    :param catalogue: dict
    :return: None
    :raises: ValueError (if item not found in catalogue)
    """
    for item in basket:
        if not catalogue.get(item):
            raise ValueError("Basket item '{}' not found in catalogue: '{}'"
                             .format(item, catalogue))


def validate_offers(offers):
    """
    Check that the offers are the right type and in the right format

    :param offers: dict
    :return: None
    :raises: TypeError (if the offer type or format is invalid)
    """
    for _, offer_type in offers.items():
        if len(offer_type) != 2:
            raise TypeError(
                "Invalid offer type: {}. Offer type must be in the format:"
                "('TYPE', 'VALUE')".format(offer_type))
        if offer_type[0] not in VALID_OFFER_TYPES:
            raise TypeError("Offer type must be one of: {}".format(
                VALID_OFFER_TYPES))

        if offer_type[0] == "PERCENT_OFFER":
            validate_percent_offer_value(offer_type[1])
        elif offer_type[0] == "MULTI_OFFER":
            validate_multi_offer_value(offer_type[1])


def validate_percent_offer_value(offer_value):
    """
    Check that the percent offer are the right type and in the right format

    :param offer_value:
    :return: None
    :raises: ValueError (if the percentage value is not valid)
    """
    # if the percentage value is not a number raise an error
    try:
        int(offer_value)
    except ValueError:
        raise ValueError(
            "Invalid Percent Offer value: {}. Value must be a number".format(
                offer_value))

    # if the percentage value is not between 1-100% raise an error
    if not (0 <= int(offer_value) <= 100):
        raise ValueError(
            "Invalid percentage value. {}. Percent value must "
            "be within range (0, 100)".format(offer_value))


def validate_multi_offer_value(offer_value):
    """
    Check that the multi offer are the right type and in the right format

    :param offer_value:
    :return: None
    :raises: ValueError (if the multioffer value is not valid)
    """
    if len(offer_value.split(",")) != 2:
        raise ValueError(
            "Invalid Multi offer value: {}. MultiOffer value must be in the "
            "format: '2,1'. Where 2 is the charge_quantity and 1 is the "
            "free_quantity.".format(offer_value))

    # if the multi value is not a number raise an error
    try:
        int(offer_value.split(",")[0])
        int(offer_value.split(",")[1])
    except ValueError:
        raise ValueError(
            "Invalid Multi Offer value: {}. Value must be a number".format(
                offer_value))


def check_catalogue_item_have_negative_price(catalogue):
    """
    Check if the catalogue has items with negative price

    :param catalogue: dict
    :return: None
    :raises: ValueError (if there is a negative price for an item)
    """
    for item, price in catalogue.items():
        if price < 0:
            err_msg = "Item '{}' has a negative price '{}'".format(
                item, price)
            raise ValueError(err_msg)


def get_sub_total(basket, catalogue):
    """
    Calculate the total price for all items in the basket without any discounts

    :param basket: dict
    :param catalogue: dict
    :return: float
    """
    sub_total = 0.00
    for item, quantity in basket.items():
        sub_total += quantity * catalogue[item]
    return round(sub_total, 2)


def get_total_price(sub_total, discount):
    """
    Calculate the total price for all items in the basket including all
    discounts available.

    :param sub_total: float
    :param discount: float
    :return: float
    :raises: ValueError (if the total price works out to be negative)
    """
    total = sub_total - discount
    if total < 0:
        err_msg = "Total price is negative. subtotal={}, Discount={}".format(
            sub_total, discount)
        raise ValueError(err_msg)
    return round(total, 2)


def get_total_discount(basket, offers, catalogue):
    """
    Calculate the total discounts based on the offers available for each item

    :param basket: dict
    :param offers: dict
    :param catalogue: dict
    :return: float
    """
    discount = 0.0

    for item, quantity in basket.items():
        offer_type = offers.get(item)
        if offer_type:
            offer_type = offers[item][0]
            offer_value = offers[item][1]
            item_price = catalogue[item]
            if offer_type == "PERCENT_OFFER":
                discount += quantity * item_price * int(offer_value) / 100
            elif offer_type == "MULTI_OFFER":
                charge_for_quantity = float(offer_value.split(",")[0])
                free_quantity = float(offer_value.split(",")[1])
                bundles, remainder = divmod(
                    quantity, charge_for_quantity + free_quantity)
                if remainder > charge_for_quantity:
                    bundles += 1
                    remainder = 0
                charge_quantity = (bundles * charge_for_quantity) + remainder
                discount += (quantity - charge_quantity) * item_price

    return round(discount, 2)


def get_basket_price(basket, catalogue, offers):
    """
    A basket-pricer interface which if given a selection of products within a
    basket, a "catalogue" of products available in a  supermarket and a
    collection of special-offers, will return price of goods including any
    applicable discounts.

    :param basket: a dictionary containing the items on a product i.e.
                   basket = {
                        'Baked Beans': 2,
                        'Sardines': 5
                   }
    :param catalogue: a dictionary containing all products available i.e
                   catalogue = {
                       'Baked Beans': 0.99,
                       'Biscuits': 1.20,
                       'Sardines': 1.89,
                       'Shampoo(Small)': 2.00,
                       'Shampoo(Medium)': 2.50,
                       'Shampoo(Large)': 3.50
                   }
    :param offers: a dictionary containing special offers for each product.
                    offers = {
                        'Baked Beans': ('MULTI_OFFER', '2,1'),
                        'Biscuits': ('PERCENT_OFFER', '0'),
                        'Sardines': ('PERCENT_OFFER', '25')
                    }
                    Available offer types: "PERCENT_OFFER", "MULTI_OFFER"
    :return: a dictionary containing response. i.e.
                    response = {
                        'sub_total': 6.77,
                        'discount': 2.21,
                        'total': 4.56
                    }
    """
    response = {
        'sub_total': 0.0,
        'discount': 0.0,
        'total': 0.0
    }

    if is_basket_empty(basket):
        return response

    # validate the catalogue for negative price and empty-ness
    check_catalogue_empty(catalogue)
    check_catalogue_item_have_negative_price(catalogue)

    # check that the items in the basket are in the catalogue
    check_basket_items_in_catalogue(basket, catalogue)

    # make sure the offers are the right type and in the right format
    validate_offers(offers)

    # If all the checks pass, begin the computation
    sub_total = get_sub_total(basket, catalogue)
    discount = get_total_discount(basket, offers, catalogue)
    total = get_total_price(sub_total, discount)

    response['sub_total'] = sub_total
    response['total'] = total
    response['discount'] = discount

    return response
