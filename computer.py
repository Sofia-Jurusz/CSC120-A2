"""
This class creates and gives attributes to a 'Computer'. It also contains a function so the computer can update its OS
"""
class Computer:

    """
    these are all the characteristics the computer has
    """
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    """
    We can use this function to make a new computer, as long as we give it all the appropriate attributes
    """
    def __init__(self, description : str, processor_type : str, hard_drive_capacity : int, memory : int, operating_system : str, year_made : int, price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    """
    This function lets the computer update its OS
    """
    def update_os(computer, new_os : str):
        computer.operating_system = new_os
        print("The operating system is updated to", computer.operating_system)
        

def main():
    pass

if __name__ == "__main__": main()