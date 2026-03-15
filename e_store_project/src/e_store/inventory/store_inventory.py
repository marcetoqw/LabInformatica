class StoreInventory:
    def __init__(self):
        self.items = {}
    def add_stock(self, item, quantity):
        self.items[item] = self.items.get(item, 0) + quantity
    def remove_stock(self, item, quantity):
        if self.items.get(item) - quantity >= 0:
            self.items[item] = self.items.get(item) - quantity
            return True
        return False