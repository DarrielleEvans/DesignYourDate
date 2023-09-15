import random

#This is a dating script where the user can decide who they will go on a date with
#They will also choose what the user and their date will be eating from the menu and decide if they want to pay
#the script will randomly decide if they will get a second date or not

# The following lines are the functions that will be used in the script

#Function has one parameter which will be the customers order and will place their input into a list
def createOrderList(order):
    orderList = []
    orderList = order.split(" ")
    return orderList

#Function will iterate through the list and match its values with the keys in the dictionary
#The total of all keys will be added and stored in the variable total
def calcBillTotal(orderList, foodMenu):
    total = 0
    for item in orderList:
        if item.lower() in foodMenu:
            total += foodMenu[item.lower()]
    return(total)

#function will calculate the remaining budget after each order is placed
def orderTotalDiff(amountOne, amountTwo):
    remainingBudget= amountOne - amountTwo
    return remainingBudget

#Function will ask the user if they want to pay
def payBill(userOrderTotal, dateOrderTotal):
    total = int(userOrderTotal) + int(dateOrderTotal)
    print(f"Your total is {total}")
    payAnswer=input("Would you like to pay? \n")
    if payAnswer == "yes" or "Yes":
        print("Great")
    elif payAnswer == "no" or "No":
        print(" I am calling the police")

#function will randomly decide if user gets another date
def secondDate():
    chances = random.randrange(1,2)
    if chances == 1:
        print("NO SECOND DATE FOR YOU!!")
    elif chances == 2:
        print("Can't wait for the second date!!")


print("Welcome to Savory Eats FoodHall!")
#User inputs who is on the date with them
dateName = input("Whose your date? \n")

#User inputs their budget for the date
dateAmount = float(input("How much do you want to spend \n"))

#Here are the items that the user can choose from stored in dictionaries based on category
entree = {"Shrimp-Alfredo": 25, "Crab-Legs": 40, "Lobster": 50, "Fried-Shrimp": 10, "Quesadilla": 8, "Enchiladas": 15}
drinks = {"Wine": 15, "Rum Punch": 15, "Margarita": 12}
dessert = {"Cheesecake": 10, "Tres-Leches": 8}
foodHalls ={"shrimp-alfredo": 25, "crab-legs": 40, "lobster": 50, "fried-shrimp": 10, "quesadilla":8, "enchiladas": 15, "wine": 15, "rum-punch": 15, "margarita": 12, "cheesecake": 10, "tres-leches": 8}

#The following print statements displays the menu items stored in the dictionaries
print("Check out the menu. You can mix and match any items you like. \n")
print("")
print(f"Remember your budget of ${dateAmount}. And don't forget you have to pay for your date. \n")
print("")
print(f"Here are the Entrees: {entree}")
print(f"Here are the Desserts: {dessert}")
print(f"Here are the Drinks {drinks}")
print("")

#The following lines are the functions being called
firstOrder = input("What would you like to order? Please put a hyphen between items with two words and use a space after each item. \n")
secondOrder = input(f"What would {dateName} like order? \n")

firstOrderList = createOrderList(firstOrder)
firstTotal =calcBillTotal(firstOrderList, foodHalls)
firstRemainingBudget = orderTotalDiff(dateAmount, firstTotal)
print(f"You ordered {firstOrderList} and your remaining budget is ${firstRemainingBudget}")
secondOrderList=createOrderList(secondOrder)
secondTotal=calcBillTotal(secondOrderList, foodHalls)
secondRemainingBudget = orderTotalDiff(firstRemainingBudget,secondTotal)
print(f" {dateName} ordered {secondOrderList} and your remaining budget is ${secondRemainingBudget}")
payBill(firstTotal, secondTotal)
secondDate()
