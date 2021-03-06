# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# DONE: Replace temporary variable with extracted method/query

# Code snippet. Not runnable.
def get_price():
    base_price = get_quantity() * get_item_price()
    discount_factor = 0.95 if base_price > 1000 else 0.98
    return base_price * discount_factor
