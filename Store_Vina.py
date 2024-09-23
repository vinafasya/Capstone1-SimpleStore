#Capstone 1 Python
#Vina Fasya Kartamanah
#DTIDS-0206

shopping_cart = [] #to store dynamic data that will be modified and updated over time
total_price = 0

# the products of the store program is food and beverage of 'Cats & Clouds Eatery'
products_db = {
    1: {'id': 1, 'name': 'Caesar Salad', 'stock': 4, 'price': 25000, 'category': 'Promo', 'max_item': 1},
    2: {'id': 2, 'name': 'Chicken Salad', 'stock': 17, 'price': 25000, 'category': 'Promo', 'max_item': 1},
    3: {'id': 3, 'name': 'Salmon Soup', 'stock': 2, 'price': 35000, 'category': 'Promo', 'max_item': 1},
    4: {'id': 4, 'name': 'Omelette', 'stock': 10, 'price': 25000, 'category': 'Promo', 'max_item': 1},
    5: {'id': 5, 'name': 'Argentine Smoked Beef', 'stock': 15, 'price': 35000, 'category': 'Promo', 'max_item': 1},
    6: {'id': 6, 'name': 'Toasted Berry\'s', 'stock': 50, 'price': 25000, 'category': 'Promo', 'max_item': 1},
    7: {'id': 7, 'name': 'Homemade Wedges', 'stock': 110, 'price': 22000, 'category': 'Normal', 'max_item': 99},
    8: {'id': 8, 'name': 'Onion Rings', 'stock': 80, 'price': 22000, 'category': 'Normal', 'max_item': 99},
    9: {'id': 9, 'name': 'Bolognaise Potato Beef', 'stock': 70, 'price': 32000, 'category': 'Normal', 'max_item': 99},
    10: {'id': 10, 'name': 'Wagyu Satay', 'stock': 90, 'price': 60000, 'category': 'Normal', 'max_item': 99},
    11: {'id': 11, 'name': 'Umami Chicken Rice Bowl', 'stock': 65, 'price': 39000, 'category': 'Normal', 'max_item': 99},
    12: {'id': 10, 'name': 'Salmon Cream Soup', 'stock': 50, 'price': 29000, 'category': 'Normal', 'max_item': 99},
    13: {'id': 10, 'name': 'Pasta Primavera', 'stock': 50, 'price': 50000, 'category': 'Normal', 'max_item': 99},
    14: {'id': 10, 'name': 'Beef Steak', 'stock': 50, 'price': 60000, 'category': 'Normal', 'max_item': 99},
    15: {'id': 10, 'name': 'Garlic Duck Rice', 'stock': 85, 'price': 50000, 'category': 'Normal', 'max_item': 99},
    16: {'id': 10, 'name': 'Signature Tuna Pasta', 'stock': 90, 'price': 50000, 'category': 'Normal', 'max_item': 99},
    17: {'id': 10, 'name': 'French Soft Ice Cone', 'stock': 100, 'price': 29000, 'category': 'Normal', 'max_item': 99},
    18: {'id': 10, 'name': 'Apple Tart', 'stock': 65, 'price': 27000, 'category': 'Normal', 'max_item': 99},
    19: {'id': 10, 'name': 'Tiramisu', 'stock': 55, 'price': 27000, 'category': 'Normal', 'max_item': 99},
    20: {'id': 10, 'name': 'Iced Chocolate', 'stock': 70, 'price': 35000, 'category': 'Normal', 'max_item': 99},
    21: {'id': 10, 'name': 'Chamomile Tea', 'stock': 100, 'price': 35000, 'category': 'Normal', 'max_item': 99},
    22: {'id': 10, 'name': 'Passion Fruit Tea', 'stock': 100, 'price': 35000, 'category': 'Normal', 'max_item': 99},
    23: {'id': 10, 'name': 'Golden Mango Latte', 'stock': 50, 'price': 35000, 'category': 'Normal', 'max_item': 99},
    24: {'id': 10, 'name': 'Tropical Juice', 'stock': 120, 'price': 39000, 'category': 'Normal', 'max_item': 99},
    25: {'id': 10, 'name': 'Sparkling Water', 'stock': 200, 'price': 19000, 'category': 'Normal', 'max_item': 99},
    26: {'id': 10, 'name': 'Espresso', 'stock': 100, 'price': 31000, 'category': 'Normal', 'max_item': 99},
    27: {'id': 10, 'name': 'Matcha Latte', 'stock': 35, 'price': 35000, 'category': 'Normal', 'max_item': 99},
}

#store member data where for every transaction by member will be recorded and seen in display member feature
members_db = {
    1: {'id': 1, 'name': 'Vina', 'phone': '1234567890', 'total transaction': 0},
    2: {'id': 2, 'name': 'Priscilla Sherman', 'phone': '2345678901', 'total transaction': 0},
    3: {'id': 3, 'name': 'Simone Sims', 'phone': '3456789012', 'total transaction': 0},
    4: {'id': 4, 'name': 'Kimberly Decker', 'phone': '4567890123', 'total transaction': 0},
    5: {'id': 5, 'name': 'Damari Miranda', 'phone': '5678901234', 'total transaction': 0},
    6: {'id': 6, 'name': 'Remy Wise', 'phone': '6789012345', 'total transaction': 0},
    7: {'id': 7, 'name': 'Elaine Ford', 'phone': '7890123456', 'total transaction': 0},
    8: {'id': 8, 'name': 'Dream Cameron', 'phone': '8901234567', 'total transaction': 0},
    9: {'id': 9, 'name': 'Aubrey Fox', 'phone': '9012345678', 'total transaction': 0},
    10: {'id': 10, 'name': 'Ruby Hayden', 'phone': '0123456789', 'total transaction': 0},
    11: {'id': 11, 'name': 'Troy Lang', 'phone': '1234567891', 'total transaction': 0},
    12: {'id': 12, 'name': 'Melvin French', 'phone': '2345678902', 'total transaction': 0},
    13: {'id': 13, 'name': 'Andrea Baker', 'phone': '3456789013', 'total transaction': 0},
    14: {'id': 14, 'name': 'Cecelia Harrell', 'phone': '4567890124', 'total transaction': 0},
    15: {'id': 15, 'name': 'Sasha Lim', 'phone': '5678901235', 'total transaction': 0},
    16: {'id': 16, 'name': 'Roman Vance', 'phone': '6789012346', 'total transaction': 0},
    17: {'id': 17, 'name': 'Maia Chung', 'phone': '7890123457', 'total transaction': 0},
    18: {'id': 18, 'name': 'Blake Kirby', 'phone': '8901234568', 'total transaction': 0},
    19: {'id': 19, 'name': 'Missouri Bailey', 'phone': '9012345679', 'total transaction': 0},
    20: {'id': 20, 'name': 'Samantha Allen', 'phone': '0123456780', 'total transaction': 0}
}

#display item feature
def display_menu(items):
  print("-" * 90)
  print(f"{'ID':<5} {'Name':<25} {'Stock':<10} {'Price (IDR)':<15} {'Category':<15} {'Max Purchase':<10}")
  print("-" * 90)
  for item_id, item in items.items():
    print(f"{item_id:<5} {item['name']:<25} {item['stock']:<10} {item['price']:<15} {item['category']:<15} {item['max_item']}")
  print("-" * 90)
  print("1. Filter menu by category")
  print("2. Sort menu by stock")
  print("0. Go back to Main Menu")
  print("-" * 90)
  choice = int(input("Enter your choice number: "))
  if choice == 1:
    filter_menu()
  elif choice == 2:
    sort_menu()
  elif choice == 0:
    main_menu()
  else:
    print("Redirecting to main menu. Please input available option only.")
    main_menu()

#to show display in other features beside display item (more user friendly)
def display_only(items):
  print("-" * 90)
  print(f"{'ID':<5} {'Name':<25} {'Stock':<10} {'Price (IDR)':<15} {'Category':<15} {'Max Purchase':<10}")
  print("-" * 90)
  for item_id, item in items.items():
    print(f"{item_id:<5} {item['name']:<25} {item['stock']:<10} {item['price']:<15} {item['category']:<15} {item['max_item']}")

#Display Item: Filter by category
def filter_menu():
  category = input("Enter category to filter by (Promo or Normal): ").strip().capitalize()
  filtered_items = dict(filter(lambda item: category == item[1]['category'], products_db.items()))
  display_menu(filtered_items)

#Display Item: Sort by stock, ASC
def sort_menu():
  sorted_items = dict(sorted(products_db.items(), key=lambda item: item[1]['stock'], reverse=False))
  display_menu(sorted_items)


#DisplayMemberFeature
def display_members(items):
  print("-" * 90)
  print(f"{'ID':<5} {'Name':<25} {'Phone':<20} {'Total Transaction (IDR)':<15}")
  print("-" * 90)
  for item_id, item in items.items():
    print(f"{item_id:<5} {item['name']:<25} {item['phone']:<20} {item['total transaction']:<15}")



#Add Item Feature
def add_item():
  try:
    display_only(products_db)
    name = input("Enter new item name or 0 to go back: ").strip()
    if name == "0":
      main_menu()
    else:
      stock = int(input("Enter stock quantity: ").strip())
      price = int(input("Enter price in IDR: ").strip())
      category = input("Enter category (Promo or Normal): ").strip().capitalize()
      if category == 'Promo':
        max_item = int(input("Enter max item quantity: ").strip())
      else:
        max_item = 99
      item_id = max(products_db.keys(), default=0) + 1
      products_db[item_id] = {
          'name': name,
          'stock': stock,
          'price': price,
          'category': category,
          'max_item': max_item
          }
      print("Item successfully added.")

  except ValueError:
    print("The option you entered is not valid.")

#Remove Item Feature
def remove_item():
  try:
    display_only(products_db)
    item_id = int(input("Enter item ID to remove or 0 to go back: ").strip())
    if item_id == 0:
      main_menu()
    else:
      if item_id in products_db:
        confirmation = input("Are you sure you want to delete this item? (yes/no): ").strip().lower()
        if confirmation == 'yes':
          del products_db[item_id]
          print("Data successfully deleted.")
        else:
          print("Item removal canceled.")
      else:
          print("The item does not exist.")
  except ValueError:
      print("The option you entered is not valid.")

#Update Item Feature
def update_item():
  try:
    display_only(products_db)
    item_id = int(input("Enter item ID to update or 0 to go back: ").strip())
    if item_id == 0:
      main_menu()
    else:
      if item_id in products_db:
        print(f"Current data for item {item_id}: {products_db[item_id]}")
        name = input("Enter new name: ").strip()
        stock = int(input("Enter new stock: ").strip())
        price = int(input("Enter new price: ").strip())
        category = input("Enter new category (Promo or Normal): ").strip()
        max_item = int(input("Enter new max item quantity: ").strip())
        products_db[item_id] = {
            'name': name,
            'stock': stock,
            'price': price,
            'category': category,
            'max_item': max_item
            }
        print("Data successfully updated.")

      else:
        print("The item does not exist.")
  except ValueError:
      print("The option you entered is not valid.")

#Customer Purchase Feature
def purchase_item():
  display_only(products_db)
  shopping_cart = []
  member_choice = input("\nAre you a member? (yes/no): ").strip().lower()
  total_price = 0
  if member_choice == 'yes':
    try:
      member_id = int(input("Enter your member ID or 0 to go back: ").strip())

      if member_id == 0:
        print("Transaction cancelled.")
        main_menu()
        return
      if member_id not in members_db:
        print("The member ID does not exist.")
        return

      while True:
          item_id = int(input("Enter item ID to purchase: ").strip())
          if item_id in products_db:
            if products_db[item_id]['stock'] ==0:
              print("Out of stock")
              continue

          shopping_cart = []
          total_price = 0

          quantity = int(input("Enter quantity: ").strip())

          #max purchase restriction for promo item
          if products_db[item_id]['category'] == 'Promo' and quantity >1:
            print("Maximum purchase quantity of promo item is 1.")
            continue

          if quantity > 0 and quantity <= products_db[item_id]['stock']:
            item_price = products_db[item_id]['price']
            member_price = item_price * quantity * 0.9 #get 10% discount for members
            total_price += member_price
            shopping_cart.append({'item_id': item_id, 'quantity': quantity, 'total_price': member_price})
            break
          else:
            print("Invalid quantity. Please do not buy exceed stock.")





      #payment
      print(f"Total amount to be paid after discount: {total_price}")
      while True:
          money = float(input("Enter amount of money you want to pay (enter 0 to cancel): "))

          if money < 0:
            print("Amount cannot be less than 0.")
            continue

          elif money >= total_price:
            # Print receipt
            print('-'*30)
            print("\nCats and Clouds Eatery Receipt")
            print('-'*30)
            for item in shopping_cart:
              print(f"Item: {products_db[item['item_id']]['name']}")
              print(f"Quantity: {item['quantity']}")
              print(f"Unit Price: {products_db[item['item_id']]['price']}")
              print(f"Special Discount for Member: 10%")
              print(f"Price After Discount: {item ['total_price']}")
            print('-'*30)
            print(f"Total Price: {total_price}")
            print('-'*30)


            print(f"Money Paid: {money}")
            change = money - total_price
            print(f"Change: {change}")
            print("Thanks for coming in. See you again soon!")



            # Update stock
            for item in shopping_cart:
              products_db[item['item_id']]['stock'] -= item['quantity']

            #add total transaction to member data
            members_db[member_id]['total transaction'] += total_price

            # reset cart item and total price for next transaction
            shopping_cart.clear()
            total_price = 0

            main_menu()
            return

          elif money == "0":
            print("The transaction has been cancelled.")
            main_menu()
            return

          else:
            print("Insufficient amount. Please input valid amount.")





    except ValueError:
      print("The option you entered is not valid.")
      return

  elif member_choice == 'no':
    try:
      while True:
        item_id = int(input("Enter item ID to purchase or 0 to go back: ").strip())

        if item_id == "0":
            print("Transaction cancelled.")
            main_menu()
            return


        if item_id in products_db:
          #check max purchase for promo item
          if products_db[item_id]['stock'] == 0:
            print("Out of stock")
            continue

          quantity = int(input("Enter quantity: ").strip())

          if products_db[item_id]['category'] == 'Promo' and quantity >1:
            print("Maximum purchase quantity of promo item is 1.")
            continue

          #quantity <= available stock
          if quantity > 0 and quantity <= products_db[item_id]['stock']:
            item_price = products_db[item_id]['price'] * quantity #no discount for non member
            total_price += item_price
            shopping_cart.append({'item_id': item_id, 'quantity': quantity, 'total_price': item_price})

            break

          else:
            print("Invalid quantity. Please ensure it does not exceed stock.")
        else:
            print("Invalid item ID.")




      #payment
      print(f"Total amount to be paid: IDR {total_price}")
      while True:
        try:
          money = float(input("Enter amount of money you want to pay (enter 0 to cancel): ").strip())
          if money < 0:
            print("Amount cannot be less than 0.")
            continue
          if money == 0:
            print("Transaction cancelled.")
            main_menu()
            return

          if money >= total_price:
            # Print receipt
            print('-'*30)
            print("\nCats and Clouds Eatery Receipt")
            print('-'*30)
            for item in shopping_cart:
              print(f"Item: {products_db[item['item_id']]['name']}")
              print(f"Quantity: {item['quantity']}")
              print(f"Unit Price: {products_db[item['item_id']]['price']}")
              print(f"Subtotal: {item ['total_price']}")

            print('-'*30)
            print(f"Total Price: {total_price}")
            print('-'*30)

            print(f"Money Paid: {money}")
            change = money - total_price
            print(f"Change: {change}")
            print("Thanks for coming in. See you again soon!")


            # Update stock
            for item in shopping_cart:
              products_db[item['item_id']]['stock'] -= item['quantity']



            #reset cart item and total price for next transaction
            shopping_cart.clear()
            total_price = 0


            main_menu()
            return



          else:
            print("Insufficient amount. Please input valid amount.")

        except ValueError:
          print("Invalid input. Please input a valid amount.")
    except ValueError:
      print("Redirecting to main menu. The option you entered is not valid.")




# Main menu of the program
def main_menu():
  while True:
    print('-'*90)
    print("\t \t \t   * * * * Cats & Clouds Eatery * * * *")
    print('-'*90)
    print("1. Display Menu")
    print("2. Add Item to Menu")
    print("3. Remove Item from Menu")
    print("4. Update Menu")
    print("5. Customer Purchase")
    print("6. Display Member")
    print("7. Exit Program")

    try:
      choice = int(input("Enter your choice: ").strip())
      if choice == 1:
        display_menu(products_db)
      elif choice == 2:
        add_item()
      elif choice == 3:
        remove_item()
      elif choice == 4:
        update_item()
      elif choice == 5:
        purchase_item()
      elif choice == 6:
        display_members(members_db)
      elif choice == 7:
        print("This program is exiting. Thank you.")
        exit()
      else:
        print("The option you entered is not valid.")
    except ValueError:
      print("The option you entered is not valid.")

# Run the program
main_menu()
