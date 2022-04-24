import json
from .logic import *
main = Logic()

def run():
    struct = {
        'max_number': main.max_number(),
        'min_number': main.min_number(),
        'first_number': main.first_number(),
        'last_number': main.last_number(),
        'number_of_prime_numbers': main.prime_numers(),
        'number_of_even_numbers': main.even_numbers(),
        'number_of_odd_numbers': main.odd_numbers(),
    }

    print(struct)
    with open('struct.json','r+',encoding='utf_8') as f:
        file = json.loads(f.read())
        file.append(struct)
        f.truncate(0)
        f.seek(0)
        f.write(json.dumps(file))
    print('the file saved successfully')

