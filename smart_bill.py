name=input("Customer name: ")
item=input("Item name: ")
qty=int(input("Quantity: "))
price=int(input("Price per unit (Rs): "))
member=input("Loyalty member? [y/n]: ")
payment=input("Payment mode (cash/upi/card): ")
amount=qty*price
dis=0

member=="y"
y=0

#Allignment set up
width=50
 #
item_width=20
qty_width=8
price_width=10
amount_width=12
 #
label_width=35
value_width=15


print("=" *width)
print("KERALA FRESH MART".center(50) + "\n" + "SMART BILLING".center(50) + "\n" + "=" *width)

print(" " *width)

print(f"Customer: {name}")

print("-" *width)

print(f"{'Item':<{item_width}}{'Qty':>{qty_width}}{'Price':>{price_width}}{'Amount':>{amount_width}}")
print(f"{item:<{item_width}}{qty:>{qty_width}}{price:>{price_width},.2f}{amount:>{amount_width},.2f}")

print("-" *width) 

print(f"{'Amount:':<{label_width}}{amount:>{value_width},.2f}")

#Discount rate

if(amount >=2000):
  print(f"{'Discount rate:':<{label_width}}{'10%':>{value_width}}")
  dis=amount*.1
elif(amount >=1000 and amount <2000):
  print(f"{'Discount rate:':<{label_width}}{'5%':>{value_width}}")
  dis=amount*.05
elif(amount >=500 and amount <1000):
  print(f"{'Discount rate:':<{label_width}}{'2%':>{value_width}}")
  dis=amount*.02
else:
  print(f"{'Discount rate:':<{label_width}}{'0%':>{value_width}}")
print(f"{'Discount:':<{label_width}}{dis:>{value_width},.2f}")

#Loyalty bonus

if(amount >=500 and member.lower()=="y"):
  y=25
  print(f"{'Loyalty bonus:':<{label_width}}{y:>{value_width},.2f}")

else:
  print(f"{'Loyalty bonus:':<{label_width}}{0:>{value_width},.2f}")

ta= amount-dis-y

print(f"{'Taxable amount:':<{label_width}}{ta:>{value_width},.2f}")


gst=ta*0.05

print(f"{'GST (5%):':<{label_width}}{gst:>{value_width},.2f}")

total=ta+gst

print(f"{'Grand total:':<{label_width}}{total:>{value_width},.2f}")
print("=" *width)

#Free bag

bonus="Bonus: free cloth bag with this order!"
if(qty%12==0):
  print(bonus)

#Payment

if(payment.lower()!="cash" and payment.lower()!="card" and payment.lower()!="upi"):
  print("Invalid payment mode. Bill not Settled")
elif(amount >=10000 and payment.lower()== "cash"):
  print("Cash limit of Rs 10,000 exceeded. Please pay by UPI or card")
else:
  print(f"Payment accepted via {payment.upper()}")


