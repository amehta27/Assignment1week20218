AllStoreList = []

def show_menu():
    print("Press 1 to add a store:")
    print("Press 2 to add more item to the store :")
    print("Press 3 to view all the stores:")
    print("Press q to quit:")


def add_store():
    storename = input("Enter the store name:")
    shopping_list1 = Shopping_List(storename)
    AllStoreList.append(shopping_list1)

class Shopping_List:
    def __init__(self,name_store):
        self.name_store = name_store
        self.grocery_items = []
    def add_item(self):
        for index in range(0,len(AllStoreList)):
            print (f"{index + 1}-{AllStoreList[index].name_store}")
        additem = input("add your item:")
        addquantity = input("add your quantity:")
        addprice = input("add price")
        grocery_item1 =  Grocery_Item(additem,addquantity,addprice)
        self.grocery_items.append(grocery_item1)


    def view_all_item(self):
        print(self.name_store)
        for item in self.grocery_items:
            print(item)

class Grocery_Item:
    def __init__(self,itemname,itemquantity,itemprice):
        self.itemname = itemname
        self.quantity = itemquantity
        self.price = itemprice
    def __repr__(self):
        return (f'{self.itemname} {self.quantity} {self.price}')

user_input = ""
while user_input != "q":
    show_menu()
    user_input = input("enter choice:")

    if user_input == "1":
        add_store()
    elif user_input == "2":
         AllStoreList[0].add_item()
    elif user_input == "3":
         AllStoreList[0].view_all_item()
