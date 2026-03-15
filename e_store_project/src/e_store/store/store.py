from ..inventory.store_inventory import StoreInventory

class Store:
    def __init__(self, initial_money):
        self.inventory = StoreInventory()
        self.initial_money = initial_money

    def sell_to_customer(self, item, quantity, customer):
        price_per_unity = item.get_price() * (1-customer.get_discount())
        total_price = quantity * price_per_unity

        if total_price <= customer.money:
            if self.inventory.remove_stock(item, quantity):
                customer.money -= total_price    
                print(f"Venduti {quantity} {item.name} al prezzo di {total_price}$, new balance is {customer.money}")
        else:
            print("Not enough money or stock, sorry.")

