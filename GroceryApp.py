user_input = ""
storeslist = []

class Store:
  def __init__(self,name,address):
     self.name = name
     self.address = address
     self.grocery_items = []

class GroceryItem:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

def show_menu():
    print("Press 1 to add stores:")
    print("Press 2 to add grocery items:")
    print("Press 3 to dispaly all the grocery items from the all the stores.")
    print("Press q to exit")
    # print("Please input only numbers..")

def add_store():
    storename = input("Enter the name of the store:")
    storeaddress = input("Enter the address of the store")
    store = Store(storename,storeaddress )
    #print(f"{store.name} {store.address}")
    storeslist.append(store)
    #print(storeslist)

def display_all_items():
    for index in range(0,len(storeslist)):
        storeelement = storeslist[index]
        print(f"{index+1} - {storeelement.name} - {storeelement.address}")
        totalprice = 0
        finaltotal =0
        for grocery_item in storeelement.grocery_items:
            print(f"  {grocery_item.name} -  {grocery_item.quantity} { grocery_item.price}")
            totalprice += (int(grocery_item.price))
            print(f"total price {totalprice}")
            finaltotal += totalprice
            print(f"final total {finaltotal}")


def add_grocery_item():

    display_all_items()
    try:
        store_number = int(input("Enter the store numner to add the grocery item:"))
        selected_store = storeslist[store_number-1]

        item_name = input("Enter the grocery item: ")
        item_quantity = input("Enter the quantity")
        item_price = input("Enter the price")

        grocery_item = GroceryItem(item_name,item_quantity,item_price)
        selected_store.grocery_items.append(grocery_item)

    except IndexError:
       print("Input the valid store number")
    # for store in storeslist:
    #     print(store.name)
    #     print(store.address)




while user_input != 'q':
    show_menu()
    user_input = input("Enter your choice:")
    #try:
    if user_input == "1":
        add_store()
    elif user_input == "2":
        add_grocery_item()
    elif user_input == "3":
        display_all_items()
    #except:
        #print("Please input only numbers..")


















# def add_item(self):
#         for index in range(0,len(AllStoreList)):
#             print (f"{index + 1}-{AllStoreList[index].name_store}")
#         additem = input("add your item:")
#         addquantity = input("add your quantity:")
#         addprice = input("add price")
#         grocery_item1 =  Grocery_Item(additem,addquantity,addprice)
#         self.grocery_items.append(grocery_item1)
#
#
#     def view_all_item(self):
#         print(self.name_store)
#         for item in self.grocery_items:
#             print(item)
#
# class Grocery_Item:
#     def __init__(self,itemname,itemquantity,itemprice):
#         self.itemname = itemname
#         self.quantity = itemquantity
#         self.price = itemprice
#     def __repr__(self):
#         return (f'{self.itemname} {self.quantity} {self.price}')
#
# user_input = ""
# while user_input != "q":
#     show_menu()
#     user_input = input("enter choice:")
#
#     if user_input == "1":
#         add_store()
#     elif user_input == "2":
#         shopping_list1.add_item()
#     elif user_input == "3":
#         view_all_item()
