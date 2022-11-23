
import unittest
from restaurant_log_app import *

#creating object 
r2 = Restaurant()
#r2.load_restaurant_data() 
r2.open_restaurant()

class TestRestaurantApp(unittest.TestCase):

    def test_load_data_function_case_1(self):
        fname = "empty_log_list.csv" 
        empty_file = r2.load_restaurant_data(fname)
        self.assertEqual(False, empty_file)
    
    def test_load_data_function_case_2(self):
        fname = "log_list_1.csv"
        data_file = r2.load_restaurant_data(fname)
        self.assertEqual(True, data_file)

    def test_order_item_case_3(self):
        if r2.is_restaurant_open:

            #ordering food item
            msg = "order success"
            order_1 = r2.order_item(1, 1)
            
            self.assertEqual(msg,order_1)
            print(msg)
        else:
            msg = "Restaurant Closed"
            self.assertEqual(msg, r2.order_item(1, 1))
            print(msg)
    
    def test_order_item_case_4(self):
        if r2.is_restaurant_open:

           #ordering food item but item is not present in the list
            msg = "Item not available"
            order_1 = r2.order_item(12, 1)
            self.assertEqual(msg,order_1)
            print(msg)
        else:
            msg = "Restaurant Closed"
            self.assertEqual(msg, r2.order_item(1, 1))
            print(msg)
    
    def test_order_item_case_5(self):
        if r2.is_restaurant_open:

           #ordering same food item again by user
            msg = "Order Failured"
            order_1 = r2.order_item(1, 10)
            order_2 = r2.order_item(1, 10)
            self.assertEqual(msg,order_2)
            print(msg)
        else:
            msg = "Restaurant Closed"
            self.assertEqual(msg, r2.order_item(1, 1))
            print(msg)
    
    

#taking all the test cases into a suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestRestaurantApp)

#Running test cases using Testcases suit
unittest.TextTestRunner(verbosity=2).run(suite)