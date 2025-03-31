def calculate_discount(price, discount_percent):
    """calculates the final price after applying a discount"""
    if discount_percent > 20 or discount_percent == 20:
        price = price - price * discount_percent * 0.01
        return price
    return price

price = int(input("Enter original price: "))
discount = int(input("Enter discount percentage: "))

ans = calculate_discount(price, discount)
print(ans)
