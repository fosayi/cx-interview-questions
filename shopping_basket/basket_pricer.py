
VALID_OFFER_TYPES = ("PERCENT_OFFER", "MULTI_OFFER")


def is_basket_empty(basket):
    if not basket:
        return True
    return False


def is_catalogue_empty(catalogue):
    if not catalogue:
        return True
    return False


def are_basket_items_in_catalogue(basket, catalogue):
    for item in basket:
        if not catalogue.get(item):
            return False
    return True


def validate_offers(offers):
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
    # if the percentage value is not a number raise an error
    try:
        int(offer_value)
    except ValueError:
        raise TypeError(
            "Invalid Percent Offer value: {}. Value must be a number".format(
                offer_value))

    # if the percentage value is not between 1-100% raise an error
    if not (0 <= int(offer_value) <= 100):
        raise ValueError(
            "Invalid percentage value. {}. Percent value must "
            "be within range (0, 100)".format(offer_value))


def validate_multi_offer_value(offer_value):
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
    for item, price in catalogue.items():
        if price < 0:
            err_msg = "Item '{}' has a negative price '{}'".format(
                item, price)
            raise ValueError(err_msg)


def get_sub_total(basket, catalogue):
    sub_total = 0.00
    for item, quantity in basket.items():
        sub_total += quantity * catalogue[item]
    return round(sub_total, 2)


def get_total_price(sub_total, discount):
    total = sub_total - discount
    if total < 0:
        err_msg = "Total price is negative. subtotal={}, Discount={}".format(
            sub_total, discount)
        raise ValueError(err_msg)
    return round(total, 2)


def get_total_discount(basket, offers, catalogue):
    discount = 0.00

    for item, quantity in basket.items():
        offer_type = offers.get(item)
        if offer_type:
            offer_type = offers[item][0]
            offer_value = offers[item][1]
            item_price = catalogue[item]
            if offer_type == "PERCENT_OFFER":
                discount += quantity * item_price * int(offer_value) / 100
            elif offer_type == "MULTI_OFFER":
                charge_for_quantity = int(offer_value.split(",")[0])
                free_quantity = int(offer_value.split(",")[1])
                bundles, remainder = divmod(
                    quantity, charge_for_quantity + free_quantity)
                if remainder > charge_for_quantity:
                    bundles += 1
                    remainder = 0
                charge_quantity = (bundles * charge_for_quantity) + remainder
                discount += (quantity - charge_quantity) * item_price

    return round(discount, 2)


def get_basket_price(basket, catalogue, offers):
    pass

