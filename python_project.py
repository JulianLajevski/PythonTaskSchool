from typing import ItemsView, Match
from Option import OptionItem
from Items import Item

print("Hello to eShop!")

options = []
option1 = OptionItem("1. All products")
option2 = OptionItem("2. Add products")
option4 = OptionItem("3. Delete products")
option5 = OptionItem("4. Update products")
option6 = OptionItem("5. Search product")
options.append(option1)
options.append(option2)
options.append(option4)
options.append(option5)
options.append(option6)

while True:

    print("***************")

    for x in options:
        print(x.title)

    print("***************")

    foo = input('Choose option! ')


    def addItem(title, price):
        items = open('items.txt', 'a+')
        items.write(title + ' ' + price + '$\n')

    def allItems():
        with open('items.txt', 'r') as f:
            f_contents = f.read()
            if(f_contents != ""):
                print(f_contents)
            else:
                print("No items!")


    match foo:
            case "1":
                print('\nThere is a list of all items:')
                allItems()
            case "2":
                title = input('Input title: ')
                price = input('Input price: ')
                addItem(title, price)
            case "3":
                print('\nChoose item:')
                allItems()
                itemToDelete = input('Item: ')

                file = open('items.txt', "r")
                lines = file.readlines()

                del lines[int(itemToDelete)-1]

                newFile = open("items.txt", "w+")

                for line in lines:
                    newFile.write(line)

                newFile.close()
                print('\nItem successfully deleted!')
            case "4":
                print('\nChoose item:')
                allItems()
                itemToUpdate = input('Item: ')
                editedText = input('New text: ')

                file = open("items.txt", "r")
                itemList = file.readlines()
                itemList[int(itemToUpdate)-1] = editedText + "\n"
                file = open("items.txt", "w")
                file.writelines(itemList)
                file.close()
                print('\Changed!')
            case "5":
                items = []
                with open('items.txt') as my_file:
                    for line in my_file:
                        item = Item(line)
                        items.append(item)
                searchItem = input('What item you search?: ')
                for item in items:
                    if(searchItem in item):
                        print('There is your item:')
                        print(item)