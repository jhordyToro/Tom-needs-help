from logic.logic import *
from logic.run import *
import main
import unittest

main = Logic()


class Logic_test(unittest.TestCase):


#--------------------------------test to get the largest numbe---------------------------------

    def test_max_number(self):
        list_data = []
        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            
            
            list_data.append(data["b"])
            list_data.sort()
            max_number_data_test = list_data[-1]

        max_number_data = main.max_number()
        self.assertEqual(max_number_data, max_number_data_test)


#---------------------------------test to get the smallest number----------------------------------

    
    def test_min_number(self):
        list_data = []

        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            
            
            list_data.append(data["b"])
            list_data.sort()
            min_number_data_test = list_data[0]

        min_number_data = main.min_number()
        self.assertEqual(min_number_data_test, min_number_data)


#----------------------------------test to get the first number---------------------------------------

    
    def test_first_name(self):
        for i in range(1,2):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            if i == 1:
                first_number_data = data["b"]
        number1 = main.first_number()

        self.assertEqual(number1,first_number_data)


#------------------------------------test to get the last number---------------------------------


    def test_last_number(self):
        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            if i == 100:
                last_number_data = data['b']
        last_number_test = main.last_number()

        self.assertEqual(last_number_test,last_number_data)


#-------------------------------------test to get the prime---------------------------------- 


    def test_prime_true(self):
        true_or_false = isPrime(2)
        return self.assertEqual(true_or_false,True)



    def test_prime_false(self):
        true_or_false = isPrime(9)
        self.assertEqual(true_or_false,False)        


#-------------------------------------------test to get the evens---------------------------------------


    def test_even_number(self):
        even_numbers_test = 0
        
        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            
            
            if data['b'] % 2 == 0:
                even_numbers_test += 1

        even_numbers = main.even_numbers()

        self.assertEqual(even_numbers_test,even_numbers)


#-------------------------------------------test to get the odds---------------------------------------


    def test_odd_numbers(self):
        odds_numbers_test = 0
        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            
            
            if data['b'] % 2 != 0:
                odds_numbers_test += 1

        odds_numbers = main.odd_numbers()

        self.assertEqual(odds_numbers_test,odds_numbers)

        

if __name__ == '__main__':
    unittest.main()