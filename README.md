# Savory Eats FoodHall Date Night

Welcome to the Savory Eats FoodHall Date Night Python Script! Use this script to simulate a dinner date at the FoodHall, making choices about entrees, desserts, and drinks. Make decisions on paying the bill and wait to see if you'll get a second date!

## Features:

** Choose Your Date's Name: Start by naming your date.
* Set Your Budget: Determine how much you'd like to spend for the night.
* Order from the Menu: Pick from a list of entrees, drinks, and desserts for both you and your date.
* Bill Calculation: The script calculates the total bill based on your choices.
* Decision to Pay: Decide whether you'll cover the bill or let your date take care of it.
* Random Outcome: At the end, a random outcome will determine if you're getting a second date or not.
  
## Usage:

Run the script.
Follow the on-screen prompts to make your selections.
Note:

When ordering, please use a hyphen (-) for items with two words and separate items with a space.

Example: Shrimp-Alfredo Fried-Shrimp

Code Overview:

## Functions:
* createOrderList(order): Converts the input order into a list.
* calcBillTotal(orderList, foodMenu): Calculates the total bill based on selected items.
* orderTotalDiff(amountOne, amountTwo): Computes the remaining budget after each order.
* payBill(userOrderTotal, dateOrderTotal): Asks the user if they would like to cover the bill.
* secondDate(): Randomly determines if there will be a second date.
## Dictionaries:
* entree: A list of main dishes with their prices.
* drinks: A list of available drinks and their prices.
* dessert: A list of desserts with their prices.
* foodHalls: Combined list of all the items and their prices.
## Dependencies:

Python's built-in random module.
