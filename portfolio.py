import os
#part 1 create Item class
class ItemToPurchase():
    #intailize name to none price to 0 quanity to 0
    item = {"name":'none',"price": 0, 'quantity' : 0}
    
    #default constructor
    #set name to string price to float and quantity to int
    def __init__(self,name = "none:",price: float = 0 ,quantity: int = 0, desciption = "N/A"):
        self.item = {'name': name, 'price' : float(price), 'quantity' : int(quantity),'description' : desciption}
        
    def get_item_name(self):
        return self.item['name']
    
    def get_item_description(self):
        return self.item['description']

    def get_item_price(self):
        return self.item['price']
    
    def get_item_quantity(self):
        return self.item['quantity']
    
    def get_item_cost(self):
        total_cost = round((self.get_item_price() * self.get_item_quantity()),2)
        return total_cost
    #print item cost
    def print_item_cost(self):
        print(self.get_item_cost())
    
    def set_item_name(self,new_name: str):
        self.item['name'] = new_name

    def set_item_description(self,new_description: str):
        self.item['description'] = new_description
    def set_item_price(self, new_price: float):
        self.item['price'] = new_price
    def set_item_cost(self, new_cost: float):
        self.item['cost'] = new_cost
    def set_item_quantity(self, new_quantity: int):
        self.item['quantity'] = new_quantity

#step 4 implement shopping cart class
class shoppingcart:
    #intialize name and date default values of none for name and January 1, 2020 for date
    def __init__(self, name = "none", date = "January 1, 2020" ):
        self.customer_name = name
        self.current_date= date
        self.cart_items = []

    def add_item(self,item):
        """appends the list of items in shopping cart"""
        self.cart_items.append(item)
    
    # Step 9 Implement remove item menu option
    def remove_item(self,item_name):
        """takes item name as input and removes item if an item with that name is in cart"""
        item_found = False
        for item in self.cart_items:
            if  item_name == item.get_item_name():
                self.cart_items.remove(item)
                item_found = True
        if item_found == False:
            print("Item not found in cart. Nothing removed.")
    #Step 10 modfiy item quanity 
    def modify_item(self,item_name): 
        """takes the name of an item and asks for new parameters"""
        item_found = False
        for item in self.cart_items:
            if  item_name == item.get_item_name():
                #Requirement are to only update quantity commenting out undeeded functionality 
                #item.set_item_name (input("Please enter a new name (required): "))
                #item.set_item_description(input("Please enter a new description: "))
                #item.set_item_price(float(input("Please enter a new price X.XX: ")))
                item.set_item_quantity(int(input("Please enter a new quantity: ")))
                item_found = True
        if item_found == False:
            print("Item not found in cart. Nothing removed.")
            
        
    def get_num_items_in_cart(self):
        """returns the amount of items in the cart"""
        return(len(self.cart_items))
    
    def get_cost_of_cart(self):
        """returns total cost of all items in cart"""
        self.total =0
        for item in self.cart_items:
            self.total += item.get_item_cost()
        return self.total
   
    def print_total(self):
        """prints the cart total"""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of items: {self.get_num_items_in_cart()}")
        for item in self.cart_items:
            print(f"{item.get_item_name()} {item.get_item_quantity()} @ ${item.get_item_price()} = ${item.get_item_cost()}")
        print(f"Total = ${self.get_cost_of_cart()}")

    def print_description(self):
         print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
         print("Item Descriptions")
         for item in self.cart_items:
             print(f"{item.get_item_name()}: {item.get_item_description()}")

class menu:
     def __init__(self,cart) -> None:
        self.cart = cart 

     def print_menu(self):
        self.clear_screen()
        option = input("""
                Menu
        a - Add item to cart
        r - Remove item from cart
        c - Modify item
        i - Output items' descriptions
        o - Output shopping cart
        q - Quit
        Choose an option:""")
        option.lower()
        #Step 8 Implement Add item to cart menu option
        if option == "a":
            self.new_item()
            self.print_menu()
        # Step 9 Implement remove item menu option
        elif option == "r":
            item = input("Enter name of item to remove: ")
            self.cart.remove_item(item)
            self.return_to_menu()
            self.print_menu()
        #Step 10 Implement Change item quantity menu option
        elif option == "c":
            item_name = input("Enter name of item to update: ")
            self.cart.modify_item(item_name)
            self.return_to_menu()
            self.print_menu()
        #Step 6 Implement Output item's description menu 
        elif option == "i":
            self.cart.print_description()
            self.return_to_menu()
            self.print_menu()
        #Step 6 Implement Output shopping cart menu option
        elif option == "o":
            self.cart.print_total()
            self.return_to_menu()
            self.print_menu()
        elif option == "q":
            print("have a great day")
            exit
        else:
            print(f"{option} is an invalid input please enter one of the fwollowing options")
            self.print_menu()
     ### Menu helper functions to validate and sanitize user input ###
    
     def new_item(self):
        name = input("Please enter Item name: ")
        description = input("Please enter item description: ")
        price = self.get_price()
        quantity = self.get_quantity()
        self.cart.add_item(ItemToPurchase(name,price,quantity,description))
        self.return_to_menu()


     def get_price(self):
        price = input("Enter item price X.XX: ")
        #check if user entered price with $ and remove it 
        if price[0] == "$":
             price = price[1:]
        #check if user entered input that can be converted to float
        try:
            float(price)
        except:
            print("Please enter price as a float X.XX")
            price = self.get_price()
        return price
    
     def get_quantity(self):
        quantity = input("Enter item quantity: ")
        try:
            int(quantity)
        except:
            print("Invalid input")
            quantity = self.get_quantity()
        return quantity
     
     def return_to_menu(self):
        """waits for user to press any key"""
        return_to_menu = input("Press Any Key to Return to Main Menu")
     
     def clear_screen(self):
         if os.name == 'nt':
             clear = os.system('cls')
         else:
             clear = os.system('clear')
         
#main method
if __name__ == '__main__':
    #step 7 prompt user for name and date
    customer = {"name" :"", "date":""}
    customer["name"] = input("Enter Customer name: ")
    customer["date"] = input("Enter Date: ")
    #step 7 create an instance of shopping cart in main section of code
    cart = shoppingcart(customer["name"],customer["date"])
    cusomter_menu = menu(cart)
    # Step 5 In the main section of your code, implement the print_menu()
    cusomter_menu.print_menu()
