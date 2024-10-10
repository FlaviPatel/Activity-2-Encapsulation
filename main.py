class Computer:
    # class Variable
    #Make it private using __
    _max_price = 1000

    # Getter method
    def get_max_price(self):
        return self._max_price 

    
    # Setter method
    def set_max_price(self, price):
        self._max_price = price




comp = Computer()
print(comp.get_max_price())
comp.set_max_price(900)
print(comp.get_max_price())
