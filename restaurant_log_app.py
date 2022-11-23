
import pandas as pd 
import csv 
import random


class Restaurant():

    def __init__(self,name="Paradise"):
        self.name = name 
        self.is_restaurant_open = False
        self.customer_list = []
        self.food_menu_list = []
        self.customer_log = [] #details of order of food item with customer name
        self.top_items_list = [] #details of mostly ordered items with quantity
    
    def open_restaurant(self):
        self.is_restaurant_open = True
    
    def close_restaurant(self):
        self.is_restaurant_open = False

    #by using pandas library now i'm updating data
    def load_restaurant_data(self,file_path = "log_list_1.csv" ):
        
        msg = True #for test cases
        #loading csv file
        file_path = file_path
        dataset = pd.read_csv(file_path)

        #extracting values from csv file
        customer_id_list = dataset.iloc[:,0].values
        customer_name_list = dataset.iloc[:,1].values
        food_item_id_list = dataset.iloc[:,2].values
        food_item_name_list = dataset.iloc[:,3].values

        customer_list = self.combine_id_with_name(customer_id_list,customer_name_list)
        self.customer_list = customer_list

        food_item_list = self.combine_id_with_name(food_item_id_list,food_item_name_list)
        self.food_menu_list = food_item_list

        if len(customer_list) == 0 or len(food_item_list) == 0:
            msg = False
            return msg


        return msg
    
    #creating function to combine id's with name 
    def combine_id_with_name(self,id_list,name_list):
        length = len(id_list)
        new_list = []

        for i in range(length):
            row = {}
            row[id_list[i]] = name_list[i]
            new_list.append(row)
        
        return new_list

    #creating get_menu function
    def get_menu(self):
        print("Menu items")
        food_item_list = self.food_menu_list
        for item in food_item_list:
            for key,val in item.items():
                msg = "{} - {} ".format(key,val)
                print(msg)
        print("Order with Food item Id")
        print()
    

    #getting customer list with the help of get_customer list
    def get_customer_list(self):
        print("Customer list")
        customer_list = self.customer_list
        for item in customer_list:
            for key,val in item.items():
                msg = "{} - {} ".format(key,val)
                print(msg)
        print()

    #creating order function
    def order_item(self, food_item_id,user_id):
        if self.is_restaurant_open:
            
            food_item_list = self.food_menu_list
            food_item_id_list =self.get_id_list(food_item_list)

            #checking food item available or not    
            if food_item_id in food_item_id_list:

                if len(self.customer_log) == 0:
                    self.customer_log += [(user_id,food_item_id)]
                    msg = "order success"
                    return msg
                else:
                    list_item = (user_id,food_item_id)
                    for item in self.customer_log:
                        if item == list_item:
                            msg = "Order Failured"
                            #raise ValueError("Item Repeated")
                            return msg
                    self.customer_log += [(user_id,food_item_id)]
                    msg = "order success"
                    return msg
                    
            else:
                msg = "Item not available"
                return msg
        else:
            msg = "Restaurant Closed"
            return msg

    ##for testing purpose i'm creating order_automatatically to order automatically by using instance attributes

    def order_automatatically(self):
        customer_list = self.customer_list
        food_item_list = self.food_menu_list
        

        ##getting id's using get_id_list method
        customer_id_list = self.get_id_list(customer_list)
        food_item_id_list =self.get_id_list(food_item_list)
        #print(customer_id_list)
        #print(food_item_id_list)


        no_of_orders = len(food_item_id_list)
        
        for i in range(no_of_orders):
            user_details = customer_id_list[i]
            food_item_details = food_item_id_list[i]
            #user_details = random.choice(customer_id_list)
            #food_item_details = random.choice(food_item_id_list)
            order = self.order_item(food_item_details, user_details)
            print((i+1),order)
        
    
    


    #creating id's list 
    def get_id_list(self,list_a):
        id_list = []
        for item in list_a:
            for key in item.keys():
                id_list += [key]
        return id_list



        
    #printing customer log
    def get_customer_log(self):

        log = self.customer_log

        for item in log:
            print(item)


    def write_top_food_items_in_a_file(self):
        ##getting ordered food items id's  in a list
        if len(self.customer_log) == 0:
            self.load_restaurant_data()
            self.order_automatatically()
        customer_log_list = self.customer_log
        customer_ids_from_log = []
        food_item_ids_from_log = []


        for log in customer_log_list:
            customer_ids_from_log += [log[0]]
            food_item_ids_from_log += [log[1]]
        

        #print(food_item_ids_from_log)
        #print(customer_ids_from_log)

        new_list = food_item_ids_from_log.copy()

        new_list.sort() #sorting in a ascending order
        #print(new_list) #debugging purpose

        ##creating a dict with item_id as key and count as a value
        item_id_with_qty = {}
        for i in range(len(new_list)):
            item = new_list[i]
            count = new_list.count(item)
            item_id_with_qty[item] = count

        #print(item_id_with_qty)
        
        ##creating top items list based on quantity
        top_list = []
        for j in range(3):

            #first getting max value and then removing that corresponding key and add it into our top list
            max_val = 0
            list_b = item_id_with_qty.copy() # creating duplicate to update the original dict while iterating
            for val in list_b.values():
                if max_val <= val:
                    max_val = val
            
            for k,v in list_b.items():
                if v == max_val:
                    item_name = ""
                    for dict_item in self.food_menu_list:
                        if k in dict_item.keys():
                            item_name = dict_item[k]

                        
                    quantity = list_b[k]
                    
                    order_item_dict = {}

                    order_item_dict["ItemName"] = item_name
                    order_item_dict["quantity"] = quantity

                    self.top_items_list.append(order_item_dict)

                    #deleting top served item from list for every iteration
                    del item_id_with_qty[k]
        
        
        #writing datainto a file
        data_list = self.top_items_list.copy()
        #print(data_list)
        
        if len(data_list) == 0:
            msg = "writing failured "
            return msg
        with open('log_of_top_list.csv', 'w') as csvfile:    #for every run, file will be overwrite
            fieldnames = ["ItemName","quantity"]    
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
        
            writer.writeheader()  
            for row in data_list:  
                writer.writerow(row)    
        
        msg = "Writing completed"  
        return msg

    def get_top_3_items_in_a_file(self):
        
        if len(self.top_items_list) == 0:
            self.write_top_food_items_in_a_file()
        
        top_3 = self.top_items_list
        if len(self.top_items_list) >= 3:
            top_3 = self.top_items_list[:3]
        #writing datainto a file
        data_list = top_3

        #print(data_list)
        

        with open('log_of_top_3_list.csv', 'w') as csvfile:    
            fieldnames = ["ItemName","quantity"]    
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
            writer.writeheader()  
            for row in data_list:  
                writer.writerow(row) 
        print("Writing complete")   
        
        
        
        
  

if __name__ == "__main__":

    r1 = Restaurant()
    r1.open_restaurant()
    r1.write_top_food_items_in_a_file()
    r1.get_top_3_items_in_a_file()
    
    
