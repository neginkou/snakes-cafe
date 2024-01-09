class Restaurant:
    def __init__(self):
        self.menu = {
            'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
            'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
            'Desserts': ['Ice Cream', 'Cake', 'Pie'],
            'Drinks': ['Coffee', 'Tea', 'Unicorn Tears']
        }
        self.order = {}

    def print_menu(self):
        print("**************************************")
        print("**    Welcome to the Snakes Cafe!   **")
        print("**    Please see our menu below.    **")
        print("** To quit at any time, type 'quit' **")
        print("**************************************\n")

        for category, items in self.menu.items():
            print(f"{category}\n----------")
            for item in items:
                print(item)
            print()

    def take_order(self):
        print("***********************************")
        print("** What would you like to order? **")
        print("***********************************")

        while True:
            order_input = input("> ")
            if order_input.lower() == 'quit':
                break
            else:
                self.add_to_order(order_input)

    def add_to_order(self, item):
        if item in self.menu['Appetizers'] + self.menu['Entrees'] + self.menu['Desserts'] + self.menu['Drinks']:
            self.order[item] = self.order.get(item, 0) + 1
            print(f"** {self.order[item]} order{'s' if self.order[item] > 1 else ''} of {item} "
                  f"{'have' if self.order[item] > 1 else 'has'} been added to your meal **")
        else:
            print("Sorry, that item is not on the menu.")

    def display_exit_message(self):
        print("Exiting")


if __name__ == "__main__":
    restaurant = Restaurant()
    
    restaurant.print_menu()
    restaurant.take_order()
    restaurant.display_exit_message()