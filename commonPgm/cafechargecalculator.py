item=raw_input("enter the item:")
n=len(item)
price=input("enter the price:")
s=0.0
s=price/100.0
if s<10:
    shipping=2
else:
    shipping=3
night=input("Overnight delivery(0==no:1==yes):")
if night==1:
    shipping=shipping+5;
print"invoice:       ",item,"             :",s
print"               ","Shipping          :",shipping
print"               ","total             :",shipping+s
