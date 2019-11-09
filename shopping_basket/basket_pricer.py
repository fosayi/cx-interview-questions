
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
    pass


def get_total_price(sub_total, discount):
    pass


def get_total_discount(basket, offers, catalogue):
    pass


def get_basket_price(basket, catalogue, offers):
    pass

