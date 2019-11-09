
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


def get_sub_total(basket, catalogue):
    sub_total = 0.00
    for item, quantity in basket.items():
        sub_total += quantity * catalogue[item]
    return round(sub_total, 2)


def get_total_price(sub_total, discount):
    total = sub_total - discount
    if total < 0:
        raise ValueError("Total price cannot be negative")
    return round(total, 2)


def get_total_discount(basket, offers, catalogue):
    pass


def get_basket_price(basket, catalogue, offers):
    pass

