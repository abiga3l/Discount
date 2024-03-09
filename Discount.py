def calculate_discount(price,discount_percent):
    if discount_percent >= 20 :
      result =(price-(price*(discount_percent/100)))
    else:
      result = price
price =(input("Enter original price: "))
discount_percent=(input("Enter the percentage: "))
result= calculate_discount(price,discount_percent)
if result==price:
   print("No discount.Final:",result)
else:
   print("Final price:",result)
