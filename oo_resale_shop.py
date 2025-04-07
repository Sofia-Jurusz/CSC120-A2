"""
We need to import the 'Computer' file so we can use the Computer class we made
"""
from Computer import Computer

"""
This class creates a computer resale shop. When a resale shop is made, it has an inventory (the attribute we gave it).
"""
class ResaleShop:
    

    inventory : list
    
    """
    Resale Shop Constructer
    """
    def __init__(self, inventory:list): 
        self.inventory = inventory
    
    """
    The resale Shop can perform all the following actions:
    """


    """
    This function buys a new computer by adding it to the Resale Shop's inventory
    """
    def buy(self, new_computer):
        print("Buying", new_computer.description)
        print("Adding to inventory...")
        self.inventory.append(new_computer)
        print("New Computer added!")
        print()
        
    """
    This function sells a computer by removing it from the resale shop's inventory
    If there are no computers in the inventory, it prints an error message
    """
    def sell(self, old_computer:Computer):
        print("Selling", old_computer.description, "......")
        if old_computer in self.inventory: 
            computer_location = self.inventory.index(old_computer)
            self.inventory.pop(computer_location) #removes the computer
            print(old_computer.description, "Sold!!!!!")
        else:
            print("Sorry, we don't have that one in shop!")
        print()

    """
    This function updates the price of a new computer based on what year it came out
    """
    def update_price(computer):
        if computer.year_made < 2000:
            computer.price = 0 # too old to sell, donation only
        elif computer.year_made < 2012:
            computer.price = 250 # heavily-discounted price on machines 10+ years old
        elif computer.year_made < 2018:
            computer.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer.price = 1000 # recent stuff
        print("Price is updated!")

    
    """
    This function refurbishes a computer by updating the operating system and updating the price.
    If the computer is not in the inventory, then it prints an error message
    """  
    def refurbish_computer(self, new_computer:Computer, new_OS): #make it so you can input new OS
        print("Refurbishing", new_computer.description, ", updating OS to", new_OS)
        if new_computer in self.inventory:
            print("Updating OS...")
            new_computer.update_os(new_OS) # calls on the update_os function from the Computer class
            print("Updating price...")
            ResaleShop.update_price(new_computer) # calls on the update price function from the Resale shop class
        else:
            print("Computer store does not have that one!!!")
        print()

    """
    This function prints out the inventory contents
    """
    def check_inventory(self):
        print("Checking inventory...")
        if not self.inventory:
            print("We have nothing in stock :(")
        else:
            for computer in self.inventory:
                print(computer.description,", ", end ='')
                print(computer.processor_type,", ", end ='')
                print(computer.hard_drive_capacity,", ", end ='')
                print(computer.memory,", ", end ='')
                print(computer.operating_system,", ", end ='')
                print(computer.year_made,", ", end ='')
                print(computer.price) 
        print()

"""
This function prints out a cute little banner for my resale shop
"""
def print_banner():
    print("-" * 29)
    print("SOFIA'S COMPUTER RESALE STORE")
    print("-" * 29)

def main():
    print_banner()
    # first, let's make some computers using the Computer constructer!!
    pc_1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500) 
    pc_2 = Computer("Mac Book Air",
        "3.5 GHc 6-Core Intel Xeon E5",
        300, 80,
        "macOS Catalina", 2017, 2000) 
    pc_3 = Computer("Windows",
        "3.5 GHc 6-Core Intel Xeon E5",
        300, 80,
        "macOS Catalina", 2017, 2000) 
    
    # next, let's build my computer store using the resale shop constructer and creating a place for my inventory
    shop_inventory = []
    sof_shop = ResaleShop(shop_inventory)
    sof_shop.check_inventory()

    # next, we need to buy some computers to sell and take a peek at our new and improved inventory
    sof_shop.buy(pc_1)
    sof_shop.buy(pc_2)
    sof_shop.check_inventory()

#new_OS = "MacOS Monterey" 
    # these computers are old! we need to do some updating
    sof_shop.refurbish_computer(pc_2, "MacOS Monterey")
    sof_shop.refurbish_computer(pc_3, "MacOS High Sierra")
    sof_shop.check_inventory()

    # now we gotta make some money and sell them
    sof_shop.sell(pc_2)
    sof_shop.check_inventory()
    sof_shop.sell(pc_1)
    sof_shop.check_inventory()
    print("This time it's a good thing! We bought and sold all of our computers!")

if __name__ == "__main__": main()

