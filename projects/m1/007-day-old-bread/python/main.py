bakery_sell_loaves = 3.49

old_loaves_purchased = int(input('Hey how many old loaves do you want to buy? '))

loaves_price = bakery_sell_loaves * old_loaves_purchased

total = loaves_price - (loaves_price * 60) / 100
discount = loaves_price - total

print(f'{"LOAVES BREAD = $":>20} {loaves_price:6.2f}\n{"DISCOUNT = $":>20} {discount:6.2f}\n{"TOTAL = $":>20} {total:6.2f}')