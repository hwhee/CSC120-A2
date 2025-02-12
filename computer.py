class Computer:
# Contains all computer specifications and deals with refurbishing and updating the price and OS.

    # Attributes:
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # Constructor:
    def __init__(self, 
                 description: str, 
                 processor_type: str, 
                 hard_drive_capacity: int, 
                 memory: int, 
                 operating_system: str, 
                 year_made: int, 
                 price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # Methods:
    def update_price (self, updated_price: int):
        self.price = updated_price
        print (f"Price updated to: {self.price}")
        #updates price and prints updated price

    def refurbish (self, updated_os:str):
        if updated_os is not None:
            self.operating_system = updated_os
        #updates OS as part of refurbishing process

        if self.year_made < 2000:
            self.price = 0
        elif self.year_made <2012:
            self.price = 250
        elif self.year_made <2018:
            self.price = 550
        else:
            self.price = 1000
        #updates price based on year made

        print (f"Computer refurbished. Price updated to: {self.price}")
        #prints refurbishing statement and updated price

    def update_OS (self, updated_OS:str):
        self.operating_system = updated_OS
        print (f"Operating system updated to: {self.operating_system}")
        #updates OS and prints updated OS