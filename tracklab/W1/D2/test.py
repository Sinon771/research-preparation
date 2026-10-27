quantity_text = "8"
price_text = "2.5"
paid_text = "False"

quantity = int(quantity_text)
price = float(price_text)
paid = paid_text == "True"

cost = quantity * price
valid = (quantity > 0) and (price >= 0)

print(cost, type(cost))
print(paid, type(paid))
print(valid, type(valid))

"""
20.0 <class 'float'>
False <class 'bool'>
True <class 'bool'>
"""