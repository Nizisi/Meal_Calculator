
"""
	We start by asking the client if they bought an item
		If they answer with an "n" or a word that starts with "n", exit the loop
		If they answer with anything else:
			Ask how much it cost
			if that cost is a positive number greater than zero
				Add it to a "prices" list and return to Step 1.
	If the list is smaller than 1 item (empty): 
		Print out a notice that they "Must enter a valid price."
	Otherwise, process each item in the list
		Print each as "Item purchased for price_of_item"
		Add it to a total variable
	Display the price of the total variable the tax and the total price with the tax added to total
	Display a "suggested tip" (using tiprate)
	Ask what the client wants to add as their tip
		get the custom amount and verify it (cannot be negative number)
			If it is - assume $0 tip if negative
	Print out a message such as "Your tip of TIP (rounded to 2 decimals) plus your meal of MEALPRICE (with tax) equals a total of TOTALPRICE"
"""



def add_to_priceList():
    clientItemPrice = float(input("Please enter the price of your item: "))
    if clientItemPrice > 0:
        prices.append(clientItemPrice)
        return



if __name__ == "__main__":
	TAXRATE = .065
	TIPRATE = .18
	tip = 0.0
	
	prices = []
	
	while True:
	    if input(f"DId you buy any item? (y/n): ").startswith("n"):
	        break
	    else:
	        add_to_priceList()
	if  len(prices)<1:
	    print("Must enter a valid price")
	else:
	    for i,e in  enumerate(prices):
	        print(f"item {i+1} purchased for {e}")
	totalPrice = sum(prices) 
	print(f"Total price before tax is {totalPrice}, tax is {totalPrice*TAXRATE}, total price with the tax is {totalPrice*TAXRATE+totalPrice}\n")
	print(f"Suggested tip is {totalPrice*TIPRATE}")
	clientTip = float(input("Put in your ideal tip: "))
	if clientTip <= 0:
	    clientTip = 0
	print(f"Your tip of clientTip:.2f plus your meal of {totalPrice*TAXRATE+totalPrice} equals a total of {totalPrice*TAXRATE+totalPrice+clientTip}")   
