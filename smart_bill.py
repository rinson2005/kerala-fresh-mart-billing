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


print("=" *50)
print("KERALA FRESH MART".center(50) + "\n" + "SMART BILLING".center(50) + "\n" + "=" *50)

print(" " *50)

print(f"Customer: {name}")
print("-" *50)
print(f"{'Item'}{'Qty':>21}{'Price':>14}{'Amount':>11}")
print(f"{item}{qty:>14}{price:>14,.2f}{amount:>11,.2f}")

print("-" *50)
print(f"Amount: {amount:>42,.2f}")

#Discount rate

if(amount >=2000):
  print(f"Discount rate: {'10%':>35}")
  dis=amount*.1
elif(amount >=1000 and amount <2000):
  print(f"Discount rate: {'5%':>34}")
  dis=amount*.05
elif(amount >=500 and amount <1000):
  print(f"Discount rate: {'2%':>35}")
  dis=amount*.02
else:
  print(f"Discount rate: {0:>34.2f}")
print(f"Discount :{dis:>39,.2f}")

#Loyalty bonus

if(amount >=500 and member.lower()=="y"):
  y=25
  print(f"{'Loyalty bonus:'}{y:>35,.2f}")
else:
  print(f"{'Loyalty bonus:'}{0:>35.2f}")

ta= amount-dis-y

print(f"Taxable amount:{ta:>34,.2f}")


gst=ta*0.05

print(f"GST (5%):{gst:>40,.2f}")

total=ta+gst

print(f"Grand total:{total:>37,.2f}")
print("=" *50)

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


