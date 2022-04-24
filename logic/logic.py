# {"a": 1, // Rango -> [1, 100]"b": 0 // Rango -> [0, 2^32)}

#---------------------------------returns the result if num is prime or not prime----------------------------------
def isPrime(num):
        if num < 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True  
#..................................................................................................................

class Logic():

#--------------------------------get the largest number---------------------------------

    def max_number(self):
        
        list_data = []
        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            
            
            list_data.append(data["b"])
            list_data.sort()

        return list_data[-1]


#---------------------------------get the smallest number----------------------------------

    def min_number(self):
        list_data = []

        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            
            
            list_data.append(data["b"])
            list_data.sort()
            

        return list_data[0]


#----------------------------------get the first number---------------------------------------

    def first_number(self):
        
        for i in range(1,2):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            if i == 1:
                first_number_data = data["b"]
                

        return first_number_data


#------------------------------------get the last number---------------------------------

    def last_number(self):
        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            if i == 100:
                last_number_data = data['b']

        return last_number_data



#-------------------------------------get the prime----------------------------------          
    
    def prime_numers(self):
        prime_number = 0
        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            result = isPrime(data["b"])

            if result is True:
                prime_number += 1
            else:
                continue
        return prime_number
        

#-------------------------------------------get the evens---------------------------------------

    def even_numbers(self):
        even_numbers_counter = 0
        
        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            
            
            if data['b'] % 2 == 0:
                even_numbers_counter += 1

        return even_numbers_counter

#-------------------------------------------get the odds---------------------------------------

    def odd_numbers(self):
        odds_numbers = 0
        for i in range(1,101):
            a = i // i + 100
            data = {
                "a": i // i + 100,
                "b": a // i + 2^32,
                }
            
            
            if data['b'] % 2 != 0:
                odds_numbers += 1

        return odds_numbers
#------------------------------------------------------------------End-------------------------------------------