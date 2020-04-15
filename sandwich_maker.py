"""
A program that asks users for their sandwich preferences,
and displays a total cost after the user enters their preferences.
"""
import pyinputplus as pyip

price_dict = {
    "wheat": float(0.99),
    "white": float(1.99),
    "sourdough": float(2.09),
    "chicken": float(4.29),
    "turkey": float(5.29),
    "ham": float(6.79),
    "tofu": float(7.29),
    "cheese": float(8.49),
    "cheedar": float(1.19),
    "swiss": float(2.29),
    "mozzarella": float(3.99),
    "mayo": float(1.89),
    "mustard": float(2.69),
    "lettuce": float(3.19),
    "tomato": float(4.69)
    }

amount = 0
subtotal = 0
total = 0

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
subtotal += price_dict.get(bread_type)
print(subtotal)

protein_type = pyip.inputMenu(['chicken', 'turkey','ham','tofu'], lettered=True)
subtotal += price_dict.get(protein_type)
print(subtotal)

cheese_desired = pyip.inputYesNo(prompt="Want cheese?")
if cheese_desired == 'yes':
    cheese_type = pyip.inputMenu(['cheedar', 'swiss', 'mozzarella'], numbered=True)
    subtotal += price_dict.get(cheese_type)
    print(subtotal)

side_order_desired = pyip.inputYesNo(prompt="Want source or vegetable?", yesVal='y', noVal='n')
if side_order_desired == 'y':
    side_order_type = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], numbered=True)
    subtotal += price_dict.get(side_order_type)
    print(subtotal)

amount += pyip.inputInt(prompt="How many sandwiches do you want? ", min=1)
total = float(subtotal * amount)
print('Total price is ' + str(total))

