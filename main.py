from logic.run import *

if __name__ == '__main__':
    run()
    print('''
    [A] to leave the result in struct.json
    [B] to remove the result from struct.json''')
    question = str(input('----: '))

    if question == 'a' or question == 'A':
        print('Bye, have a nice day :)')

    elif question == 'b' or question == 'B':
        with open('struct.json','r+',encoding='utf_8') as f:
            file = []
            f.truncate(0)
            f.seek(0)
            f.write(json.dumps(file))
        print('the file delete successfully')

    else:
        print('eso no esta disponible')
