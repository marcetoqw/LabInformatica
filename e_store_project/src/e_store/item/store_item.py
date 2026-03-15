class GenericItem:
    def __init__(self, name, prezzo):
        self.name = name
        self.prezzo = prezzo
    def get_price(self):
        return self.prezzo

class NormalItem(GenericItem):
    pass

class ForeignItem(GenericItem):
    def get_price(self):
        return (self.prezzo*0.2) + self.prezzo