print("-" * 100)
print(" ")
print("Welcome to the Greek Odyssey!")
print("The World's best authentic Greek restaurant")
print(" ")
print("-" * 100)
print(" ")
print("Our menu is below!")
print(" ")
print("Main items: ") 
print("|#1 Gyro Sandwich        $9.00|         #2 Gyro Salad           $8.50|")
print(" ")
print("|#3 Chicken Kebob        $8.00|         #4 Falafel Sandwich     $9.50|")
print(" ")
print("Sides: ")
print("|A: Lemon Rice           $3.00|         B: Fries                $2.00|")
print(" ")
print("|C: Pita Bites           $2.50|         D: Extra Tzatziki Sauce $0.50|")
print(" ")
print("You can Make any Main item a combo, ")
print("includes fries or lemon rice and a drink                      + $3.00|")
print(" ")
print("-" * 100)
print(" ")
meal_num = "y"
running_total = 0
input("When you are ready to order press enter!")
print("")
while meal_num == "y":
    print(" ")
    main = "y"
    while main == "y" or main == "Y" or main == "Yes" or main == "yes" or main == "yeah":
        main_order_question = input("What Main Menu item would you like to order? Please enter the corresponding number...  ")
        if main_order_question == "1":
            print("Gyro Sandwich")
            running_total += 9.00
        elif main_order_question == "2":
            print("Gyro Salad")
            running_total += 8.50
        elif main_order_question == "3":
            print("Chicken Kebob")
            running_total += 8.00
        elif main_order_question == "4":
            print("Falafel Sandwich")
            running_total += 9.50
        else:
            print("Invalid answer...")
#combo question
        combo = input("Would you like to make your Main dish a combo?  ")
        if combo == "yes" or combo == "y" or combo == "Yes" or combo == "YES" or combo == "Y":
            rice_fries = input("Would you like lemon rice or fries with your combo?    ")
            if rice_fries == "lemon rice":
                print("Lemon rice")
            elif rice_fries == "fries":
                print("Fries")
            running_total += 3.0
        print(" ")
        main = input("Would you like to order another main menu item?   ")
    print(" ")
    print("Your current total is $" + str(running_total))
    #side_order questions
    print(" ")
    side = "y"
    while side == "y" or side == "Y" or side == "Yes" or side == "yes" or side == "yeah" :
        side_order = input("What Sides would you like? Please enter the corresponding letter... ")
        if side_order == "A" or side_order == "a":
            running_total += 3.0
            print("Extra Lemon Rice")
        elif side_order == "B" or side_order == "b":
            running_total +=  2.0
            print("Side of Fries")
        elif side_order == "C" or side_order == "c":
            running_total += 2.50
            print("Pita Bites")
        elif side_order == "D" or side_order == "d":
            running_total += 0.50
            print("Extra Tzatziki Sauce")
        else:
            print("Invalid side order ")
        print(" ")
        side = input("Would you like to order anymore sides? ")
    print("")
    print("Your current total is $" + str(running_total))
    print("")
    #question to either end or restart the while loop
    meal_num = input("Would you like to order anything else? Enter y/n  ")
print(" ")
print("Your total is $" + str(running_total))
input("Please rate our service 1-5   ")
print("Thank you for your business!")



