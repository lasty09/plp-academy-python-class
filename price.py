def calculate_discount(price, discount_percent):
   
    if discount_percent >= 20:  
        discount_amount = price * (discount_percent / 100)  
        total_price = price - discount_amount
        return total_price
    else:
        return price