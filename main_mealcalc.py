''' 
Calculate a meal's price with tax and tip.
Tiprate can be changed but Tax is constant.
'''

# We don't know the price of the meal so let's ask (get input as float)


# Calculate the standard tiprate and print it out
# Then ask the client what they want their tip to be
# Finally print a whole message "With a tip of the tip price (rounded) your cost is fullprice (rounded)"
#####
# Except if its a dollar or less then no tax or tip
#        instead print a message with the meal price then " but no tax or tip"
#####
# Or if its 0 or negative: then print out an "invalid price" notice


if __name__ == "__main__":
	TAXRATE = .065
	TIPRATE = .18
	tip = 0.0

	clientMealPrice = float(input("Please enter the price of your meal: "))

	if(clientMealPrice <= 0):
		print("Must enter a valid price!")
	elif(clientMealPrice <= 1 and clientMealPrice > 0):
		print(f"No tax or tip will be added. Your cost is: {clientMealPrice}")
	else:
		print(f"Suggested tip: {clientMealPrice*.18:.2f}\n")
		customTip=float(input("Please enter your ideal tip: "))
		if(customTip < 0):
			customTip = 0

		clientMealPrice = clientMealPrice*.065 + clientMealPrice
		totalPrice = clientMealPrice + customTip
		print(f"Your tip of {customTip:.2f} plus your meal of {clientMealPrice} equals a total of {totalPrice:.2f}")

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