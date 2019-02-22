from datetime import datetime
total_tables = []
table_occupied_array = []

class Pool_Table:
    def __init__(self,table_no):
        self.table_no = table_no
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.is_open = "open"

    def checkout_table(self):


        if self.is_open == "close":
            print("Table is not avilable")
        else:
            #print(f"{self.start_time} Total time played {self.end_time - self.start_time}")
            self.is_open = "close"
            self.start_time = datetime.now()

    def checkin_table(self):
        # if self.is_open = "open"
        self.end_time= datetime.now()
        self.writing_to_file()
        self.is_open = "open"
        total_time = str(self.end_time - self.start_time)
        total_time_string = datetime.strptime(total_time, "%H:%M:%S.%f")
        total_time_format = total_time_string.strftime("%H:%M:%S")
        print(f"Table Number {self.table_no} {self.is_open} {self.start_time} Total time played {total_time_format}")


    def writing_to_file(self):
        with open("PoolTableReport.txt",'w') as text_file:
            for table in total_tables:
               if table.is_open == "open":
                  text_file.write("------------------------- \n")
                  text_file.write(f"Table number: {total_tables.index(table) + 1} \n")
                  text_file.write("Available \n")
               else:
                  text_file.write("------------------------- \n")
                  text_file.write(f"Table number: {total_tables.index(table) + 1} \n")
                  text_file.write(f"Start time: {table.start_time} \n")
                  text_file.write(f"End time: {table.end_time} \n")
                  text_file.write(f"Total time: {datetime.now().minute - table.end_time.minute} minute(s) \n")
                  text_file.write(f"Current cost: ${(datetime.now().minute - table.end_time.minute) * 0.5} \n")


            #print(f"{self.start_time} Total time played {self.end_time - self.start_time}")

        # for table in total_tables:
        # if self.is_open == False:
        #     print("Table is not avilable")
        #     print(f"{self.start_time} Total time played {self.end_time - self.start_time}")
        #
        # else:
        #     self.is_open == False



def setup_tables():
    for index in range(1,13):
        pool_table = Pool_Table(index)
        total_tables.append(pool_table)

def display_all_tables():
    # start_time = datetime.now()
    # end_time = datetime.now()
    for table in total_tables:
        if table.is_open == "close":
            total_time = str(datetime.now() - table.start_time)
            total_time_string = datetime.strptime(total_time, "%H:%M:%S.%f")
            total_time_format = total_time_string.strftime("%H:%M:%S")
            print(f"Table Number {table.table_no} {table.is_open} {table.start_time} Total time played {total_time_format}")
        else:
            print(f"Table Number {table.table_no} {table.is_open}")

def show_menu():
    print("Press 1 to checked out the table :")
    print("Press 2 to checked in the table :")
    print("Press 3 to dispaly all the tables")
    print("Press q to exit")


#table = PoolTable(1)
setup_tables()
user_input = ""
while user_input != 'q':

    show_menu()
    user_input = input("Enter your choice:")
    #try:
    if  user_input == "1":
        table_no = int(input("Please type the table no to play"))
        selected_table = total_tables[table_no-1]
        selected_table.checkout_table()

    elif user_input == "2":
        table_no = int(input("Please type the table no to exit"))
        selected_table = total_tables[table_no-1]
        selected_table.checkin_table()
         #print(total_table[3])
    # elif user_input == "2":
    #     checkout_table()
    elif user_input == "3":
         display_all_tables()
