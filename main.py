flag = False
loop = True
#self type
from time import sleep
def printt(string, delay):
  for i in str(string):
    print(i, end="", flush = True)
    sleep(delay)

DISCOUNT = 0
language = input("Englis - 1, Spanish - 2")

if language == "1":
	#welcome!
	printt("Welcome to Adith Pizzeria.\n", 0.05)
	#order name
	name = input("What would you like your order name to be? ")
	#boss's command pallete
	if name == "Boss":
		printt("Hello Boss. Menu?",0.05)
		menu=input("Would you like the menu?y/n")
		if menu=="y":
			print ("Menu \n Follow exact capitlization!\n 1. Large Pizza - $12 \n 2. Medium Pizza - $8 \n 3. Small Pizza - $5 \n 4. Thin Crust - No extra charge\n O. olives-.50 \n A. Artichokes-.50 \n P. Pinaples-.50 \n 5. Thick Crust - $1 extra charge!\n Drinks \n 6. Cola - $2 \n 7. Orange Juice - $2 \n 8. Water - Free \n Dessert \n 9. Ice Cream - $2 \n 10. Brownie- $1 \n 11. Cookie- 50 cents \n end. End Order \n menu. menu ")
		else:
			printt("Ok. Your shop works perfectly",0.05)
	#normal command pallete
	else:
		printt("Welcome to my fully automated pizza shop! Here is my menu",0.05)
		print ("\n Follow exact capitlization!\n 1. Large Pizza - $12 \n 2. Medium Pizza - $8 \n 3. Small Pizza - $5 \n 4. Thin Crust - No extra charge\n O. olives-.50 \n A. Artichokes-.50 \n P. Pinaples-.50 \n 5. Thick Crust - $1 extra charge!\n Drinks \n 6. Cola - $2 \n 7. Orange Juice - $2 \n 8. Water - Free \n Dessert \n 9. Ice Cream - $2 \n 10. Brownie- $1 \n 11. Cookie- 50 cents \n end. End Order \n menu. menu ")
	 #define cost and number
	cost=0
	number=0
	
	
		#ordering mechanisim
	while loop == True:
		order = input("What would you like? Print the number of your desired item to buy.")
		if order == "end" :
			loop = False
		elif order == "1":
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 12
			number = number+ 1
		elif order == "2" :
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 8
			number = number+ 1
		elif order == "3" :
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 5
			number = number+ 1
		elif order == "4":
			number_things = eval(input("How many would you like"))
			printt ("FREE")
			cost = cost + int(number_things) * 0
		elif order == "5" :
			number = number+ 1
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 1
		elif order == "6" :
			number = number+ 1
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 2
			number = number+ 1
		elif order == "7" :
	   		number = number+ 1
	   		number_things = eval(input("How many would you like?"))
	   		cost = cost + int(number_things) * 2
		elif order == "8" :
			number = number+ 1
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 0 
			printt ("FREE!!")
		elif order == "9" :
			number = number+ 1
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 2
		elif order == "10" :
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 1
		elif order == "11" :
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 0.050
		elif order == "A" or "a":
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 0.050
		elif order == "O" or "o":
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 0.050
		elif order == "P" or "p":
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 0.050
		elif order=="menu":
			printt ("Menu \n 1. Large Pizza - $12 \n 2. Medium Pizza - $8 \n 3. Small Pizza - $5 \n 4. Thin Crust - No extra charge\n O. olives-.50 \n A. Artichokes-.50 \n P. Pinaples-.50 \n 5. Thick Crust - $1 extra charge!\n Drinks \n 6. Cola - $2 \n 7. Orange Juice - $2 \n 8. Water - Free \n Dessert \n 9. Ice Cream - $2 \n 10. Brownie- $1 \n 11. Cookie- 50 cents \n End. End Order \n menu. menu ",0.05)
		else:
			break
	DISCOUNT = input("What is the discount code?(ENTER 5 FOR 1 DOLLARS OFF!!!!")
	if DISCOUNT == "5":
		cost = cost-1
	else :
		printt("OK your loss.",0.05)
			
	sales = cost + number
	tip = input("What is your tip?(Whole number. No decimals...)")
	cost = cost + int(tip)
	if name == "Boss":
		password = input("What is the password?")
		if password == "34745":
			cost = 0
			sales= 0
			print("Total cost for", number, "items is $", cost,"and your sales tax is", sales)
			restore = input("System Restoration needed?")
			if restore == "yes":
				printt("System Restoration Started",0.05)
				printt("1------2------3------4------5------",0.05)
				printt("System Restoration Completed",0.05)
				number == 0
				cost == 0
				sales == 0
				printt("Total cost for", number, "items is $", cost,"and your sales tax is", sales,0.05)
			elif restore == "no":
				printt("Ok, Bye",0.05)
				flag = True
		else:
			printt("Boss system failed.",0.05)

			
			
	else:
		print("Total cost for", number, "items is $", cost,"and your sales tax is", sales)
		print("Thank You,",name,"for eating at Adiths Pizzeria!",0.05)
		flag = True
		printt("Your pizza can be found at: https://bit.ly/whatyoupaidfor. You have to copy and paste the link in a different tab, or else it will give you an error. Idk why.",0.05)
		
elif language == "2":
		#welcome!
	printt("Welcome to Adith Pizzeria.\n", 0.05)
	#order name
	name = input("What would you like your order name to be? ")
	#boss's command pallete
	if name == "Boss":
		printt("Hello Boss. Menu?",0.05)
		menu=input("Would you like the menu?y/n")
		if menu=="y":
			print ("Menu \n Follow exact capitlization!\n 1. Large Pizza - $12 \n 2. Medium Pizza - $8 \n 3. Small Pizza - $5 \n 4. Thin Crust - No extra charge\n O. olives-.50 \n A. Artichokes-.50 \n P. Pinaples-.50 \n 5. Thick Crust - $1 extra charge!\n Drinks \n 6. Cola - $2 \n 7. Orange Juice - $2 \n 8. Water - Free \n Dessert \n 9. Ice Cream - $2 \n 10. Brownie- $1 \n 11. Cookie- 50 cents \n end. End Order \n menu. menu ")
		else:
			printt("Ok. Your shop works perfectly",0.05)
	#normal command pallete
	else:
		printt("Welcome to my fully automated pizza shop! Here is my menu",0.05)
		print ("\n Follow exact capitlization!\n 1. Large Pizza - $12 \n 2. Medium Pizza - $8 \n 3. Small Pizza - $5 \n 4. Thin Crust - No extra charge\n O. olives-.50 \n A. Artichokes-.50 \n P. Pinaples-.50 \n 5. Thick Crust - $1 extra charge!\n Drinks \n 6. Cola - $2 \n 7. Orange Juice - $2 \n 8. Water - Free \n Dessert \n 9. Ice Cream - $2 \n 10. Brownie- $1 \n 11. Cookie- 50 cents \n end. End Order \n menu. menu ")
	 #define cost and number
	cost=0
	number=0


		#ordering mechanisim
	while loop == True:
		order = input("What would you like? Print the number of your desired item to buy.")
		if order == "end" :
			loop = False
		elif order == "1":
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 12
			number = number+ 1
		elif order == "2" :
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 8
			number = number+ 1
		elif order == "3" :
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 5
			number = number+ 1
		elif order == "4":
			number_things = eval(input("How many would you like"))
			printt ("FREE")
			cost = cost + int(number_things) * 0
		elif order == "5" :
			number = number+ 1
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 1
		elif order == "6" :
			number = number+ 1
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 2
			number = number+ 1
		elif order == "7" :
	   		number = number+ 1
	   		number_things = eval(input("How many would you like?"))
	   		cost = cost + int(number_things) * 2
		elif order == "8" :
			number = number+ 1
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 0 
			printt ("FREE!!")
		elif order == "9" :
			number = number+ 1
			number_things = eval(input("How many would you like?"))
			cost = cost + int(number_things) * 2
		elif order == "10" :
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 1
		elif order == "11" :
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 0.050
		elif order == "A" or "a":
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 0.050
		elif order == "O" or "o":
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 0.050
		elif order == "P" or "p":
			number_things = eval(input("How many would you like?"))
			number = number+ 1
			cost = cost + int(number_things) * 0.050
		elif order=="menu":
			printt ("Menu \n 1. Large Pizza - $12 \n 2. Medium Pizza - $8 \n 3. Small Pizza - $5 \n 4. Thin Crust - No extra charge\n O. olives-.50 \n A. Artichokes-.50 \n P. Pinaples-.50 \n 5. Thick Crust - $1 extra charge!\n Drinks \n 6. Cola - $2 \n 7. Orange Juice - $2 \n 8. Water - Free \n Dessert \n 9. Ice Cream - $2 \n 10. Brownie- $1 \n 11. Cookie- 50 cents \n End. End Order \n menu. menu ",0.05)
		else:
			break
	DISCOUNT = input("What is the discount code?(ENTER 5 FOR 5 DOLLARS OFF!!!!")
	if DISCOUNT == "5":
		cost = cost-5
	else :
		printt("OK your loss.",0.05)

	sales = cost + number
	tip = input("What is your tip?(Whole number. No decimals...)")
	cost = cost + int(tip)
	if name == "Boss":
		password = input("What is the password?")
		if password == "34745":
			cost = 0
			sales= 0
			printt("Total cost for", number, "items is $", cost,"and your sales tax is", sales,0.05)
			printt("Thank You for eating at Adiths Pizzeria!",0.05)
			restore = input("System Restoration needed?")
			if restore == "y":
				printt("System Restoration Started",0.05)
				printt("1------2------3------4------5------",0.05)
				printt("System Restoration Completed")
				number == 0
				cost == 0
				sales == 0
				printt("Total cost for", number, "items is $", cost,"and your sales tax is", sales,0.05)
			elif restore == "n":
				printt("Ok, Bye",0.05)
				flag = True
	else:
		print("Total cost for", number, "items is $", cost,"and your sales tax is", sales)
		print("Thank You,",name,"for eating at Adiths Pizzeria!",0.05)
		flag = True
		printt("Your pizza can be found at: https://bit.ly/whatyoupaidfor. You have to copy and paste the link in a different tab, or else it will give you an error. Idk why.",0.05)

else:
	printt("an error has occured, please try again",0.05)