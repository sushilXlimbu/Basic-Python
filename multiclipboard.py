import sys
import json
import clipboard

#clipboard.copy('abc')
#data = clipboard.paste()
#print(data)

SAVE_ITEMS = 'clipboard.json'

def save_data(filepath,data):
    with open(filepath,'w') as f:
        json.dump(data,f)


def load_data(filepath):
    try:
        with open(filepath,'r') as f:
            data=json.load(f)
            return data
    except:
        return {}



#print(sys.argv)
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVE_ITEMS)

    if command == "save":
        key = input('Enter the key: ')
        data[key]=clipboard.paste()
        save_data(SAVE_ITEMS,data)  #data = {'key','clipboard text'}
        print('data saved')

    elif command == "load":
        key = input('Enter the key: ')
        if key in data:
            clipboard.copy(data[key]) 
            print('Data copied to clipboard')

    elif command == "list":
        print(data)
    else:
        print('Invalid Command')

else:
    print('Invalid command')
