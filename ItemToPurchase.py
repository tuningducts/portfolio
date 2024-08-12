#part 1 create class
class ItemToPurchase():
    #intailize name to none price to 0 quanity to 0
    item = {"name":'none',"price": 0, 'quantity' : 0}
    
    #default constructor
    #set name to string price to float and quantity to int
    def __init__(self,name = "none:",price: float = 0 ,quantity: int = 0):
        self.item = {'name': name, 'price' : float(price), 'quantity' : int(quantity)}
        
    def get_item_name(self):
        return self.item['name']

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

    def set_item_cost(self, new_cost: float):
        self.item['cost'] = new_cost

    def set_item_quantity(self, new_quantity: int):
        self.item['quantity'] = new_quantity

#main method
if __name__ == '__main__':
    
    def get_price():
        price = input("Enter item price X.XX: ")
        #check if user entered price with $ and remove it 
        if price[0] == "$":
             price = price[1:]
        #check if user entered input that can be converted to float
        try:
            float(price)
        except:
            print("Please enter price as a float X.XX")
            price = get_price()
        return price
    
    def get_quantity():
        quantity = input("Enter item quantity: ")
        try:
            int(quantity)
        except:
            print("Invalid input")
            quantity = get_quantity()
        return quantity
    
    #prompt user for 2 items
    items = ["item_1","item_2"]    
    for i in range(0,2):
        name = input("Please enter Item name: ")
        price = get_price()
        quantity = get_quantity()
        items[i] = ItemToPurchase(name,price,quantity)
    
    #print total cost of items 
    total = 0 
    print("Total Cost")
    ''' for item in items:
       print(f'{item.get_item_name()} {item.get_item_quantity()} @ ${item.get_item_price():.2f} = ${item.get_item_cost():.2f}')
       total += item.get_item_cost()'''
    for item in items:
       print(f'{item.item["name"]} {item.get_item_quantity()} @ ${item.get_item_price():.2f} = ${item.get_item_cost():.2f}')
       total += item.get_item_cost()
    print(f'Total = ${total:.2f}')
