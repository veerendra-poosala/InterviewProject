
#creating csv file (comma separated values file)

import csv
import pandas as pd


data=[{"customer_id":1,"customer_name":"Jason","food_item_id":1,"food_item_name":"Biryani"},
    {"customer_id":2,"customer_name":"Tyrion","food_item_id":2,"food_item_name":"Fried Rice"},
    {"customer_id":3,"customer_name":"Sansa","food_item_id":3,"food_item_name":"Chinese Noodles"},
    {"customer_id":4,"customer_name":"Snow","food_item_id":4,"food_item_name":"Pasta"},
    {"customer_id":5,"customer_name":"Alex","food_item_id":5,"food_item_name":"Veg-Meals"},
    {"customer_id":6,"customer_name":"James","food_item_id":6,"food_item_name":"Mutton Soup"},
    {"customer_id":7,"customer_name":"Jhon","food_item_id":7,"food_item_name":"Lollypop"},
    {"customer_id":8,"customer_name":"Steve","food_item_id":8,"food_item_name":"Springers"},
    {"customer_id":9,"customer_name":"Smith","food_item_id":9,"food_item_name":"Sand-wich"},
    

]

with open('log_list_2.csv', 'w') as csvfile:    
    fieldnames = ['customer_id', 'customer_name', 'food_item_id', 'food_item_name']    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)    
     
    writer.writeheader()  
    for row in data:  
        writer.writerow(row)    
      
     
print("Writing complete")    