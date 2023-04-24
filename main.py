#Wishlist 1.0 by Houman Hafez (SpecialSpicy)

#A Class with all the functions
class Wishlist:

    #A function to initialize our Wishlist text file
    def __init__(self):
        self.filename = "wishlist.txt"

    #A function to add each item to the wishlist (opens the txt file and adds the item's name to the wishlist.txt)
    def add_item(self, item):
        with open(self.filename, "a") as f:
            f.write(item + "\n")
        print('______________________________________________________________________')
        print()
        print(f"{item} has been added to the wishlist.")
        print()
        

    #A function to remove the already added item and tell the user to input the name of the Item
    #If there is no item, an error pops up
    def remove_item(self, item):
        items = []
        found = False
        with open(self.filename, "r") as f:
            for line in f:
                if line.strip() == item:
                    found = True
                else:
                    items.append(line.strip())
        if found:
            with open(self.filename, "w") as f:
                for item in items:
                    f.write(item + "\n")
            print(f"{item} has been removed from the wishlist.")
        else:
            print(f"{item} was not found in the wishlist.\nplease make sure the item exists before trying to remove it.")

    def display_wishlist(self):
        print("Your Wishlist: ")
        print()
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("Your Wishlist file does not contain any Items!")

#An object gets created
wishlist = Wishlist()

#Empty line and a greeting
print()
print(f"Welcome to Wishlist Created by Houman Hafez. ")
#A while loop that loops over instructions and uses class functions when the correct input has been given
#If the input is incorrect, the while loop starts over again
while True:
    print('______________________________________________________________________')
    print("Type 'add'  to add an item to the wishlist.")
    print("Type 'del' to remove an item from the wishlist.")
    print("Type 'view' to display the Wishlist.")
    print("Type 'q' to quit. ")
    print()
    user_input = input().lower()
    if user_input == 'add':
        item = input("Enter the item's name to add to the wishlist: ")
        wishlist.add_item(item)
    elif user_input == 'del':
        item = input("Which Item would you like to remove?: ")
        wishlist.remove_item(item)
    elif user_input == 'view':
        wishlist.display_wishlist()
    elif user_input == 'q':
        break
    
