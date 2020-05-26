def reverseLookup(dictionary,val):
    list_of_keys = []
    for key,value in dictionary.items():
        if val == value:
            list_of_keys.append(key)
    print(list_of_keys)

d = {1:'hippo', 2:'hippo', 3:'olive', 4:'mud', 5:'orange'}
reverseLookup(d,'hippo')