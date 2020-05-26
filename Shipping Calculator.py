def ShippingCharge(items):
    return 10.95 + 2.95 * (items - 1)

items = int(input('Input item amount: '))

print('Total shipping fee: $' + str(round(ShippingCharge(items), 2)))