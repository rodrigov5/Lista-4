def addNewName(name):
    arr = []
    phoneBook[name] = arr

def addNumber(name, num):
    value = phoneBook[name]
    value.append(num)
      

def removeNumber(name, i):
    value = phoneBook[name]
    value.pop(i)

def removeName(name):
    phoneBook.pop(name)

def consultNumber():
    return phoneBook.values()  

phoneBook = {}



print(phoneBook)

