from computer import *

class ResaleShop:
    #Deals with inventory, printing the inventory, buying, and selling. includes a main for testing purposes taken and updated from main.py

    # Attributes:
    inventory = []


    # Constructor:
    def __init__(self):
        inventory = []

    # Methods:
    def buy (self, computer: Computer):
        self.inventory.append(computer)
        #adds computer to inventory
        print (f"Item {computer.description} added to inventory")

    def sell (self, computer: Computer):
        if computer is not None:
            self.inventory.pop(0)
            #removes computer from inventory
            print (f"Item {computer.description} sold!")
        else:
            print (f"Item {computer.description} not found. Please select another item to sell.")
            #prints error message if item you are trying to sell is not in inventory

    def print_inventory (self):
        if self.inventory:
            for computer in self.inventory:
                print (computer.description)
            #prints all computers in inventory if there is inventory
        else:
            print ("No items in inventory.")
            #prints error message if there is no inventory
    
def main():
    
    # First, let's make a computer
    computer1 = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer1.description)
    print("Adding to inventory...")
    ResaleShop.buy(ResaleShop,computer1)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.print_inventory(ResaleShop)
    print("Done.\n")

    # Now, let's refurbish it
    updated_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer1.description, "updating OS to", updated_OS)
    print("Updating inventory...")
    computer1.refurbish(updated_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.print_inventory(ResaleShop)
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer1.description)
    ResaleShop.sell(ResaleShop,computer1)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    ResaleShop.print_inventory(ResaleShop)
    print("Done.\n")


main()
