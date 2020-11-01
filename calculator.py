from typing import ItemsView


class ShoppingCart:
    def __init__(self):
        self.list_items = []
        self.total_price = 0

    def additems(self, item, item_price):
        self.list_items.append(item)
        self.total_price += float(item_price)

    def removeitems(self, item, item_price):
        self.list_items.remove(item)
        self.total_price -= float(item_price)

    def show_shopping_cart(self):
        for item in self.list_items:
            print(item)
        print(self.total_price)


my_cart = ShoppingCart()
while True:

    choice = input("would you like to add , remove,  or quit ")
    if choice == "add":
        item = input("what item whould you like to add ")
        item_price = input("what is the price of this item ")
        my_cart.additems(item, item_price)

        my_cart.show_shopping_cart()

    elif choice == "remove":
        remove_item = input("what item would you like to remove ? ")
        item_price = input("what is the price of this item ")
        my_cart.removeitems(ItemsView, item_price)
        my_cart.show_shopping_cart()

    elif choice == "quit":
        my_cart.show_shopping_cart()
        break
