class GenericCustomer:
    DEFAULT_PASSWORD = "Iamagenericcustomer"

    def __init__(self, name, money):
        self.name = name
        self.money = money
    def get_discount(self):
        return 0
    def check_password(self, password):
        if self.DEFAULT_PASSWORD == password:
            return True
        return False
    
class NormalCustomer(GenericCustomer):
    DEFAULT_PASSWORD = "Iamanormalcustomer"
    pass

class PromotionalCustomer(GenericCustomer):
    DEFAULT_PASSWORD = "Iamapromotionalcustomer"

    def get_discount(self):
        return 0.05