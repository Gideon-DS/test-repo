def validate_quantity(quantity):
    return quantity > 0


def calculate_total(price, quantity):
    total = price * quantity
    return total


def process_order(price, quantity):
    result = calculate_total(price, quantity)
    return result


price = 2000
quantity = 3

final_result = process_order(price, quantity)

print(final_result)
