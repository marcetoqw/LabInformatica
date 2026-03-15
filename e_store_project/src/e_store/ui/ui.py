from ..store.store import Store
from ..customer.customer import GenericCustomer, NormalCustomer, PromotionalCustomer
from ..item.store_item import GenericItem, NormalItem, ForeignItem
import sys

def start_app():
    mio_store = Store(500.0)

    mela = GenericItem("mela", 1.0)
    switch2 = ForeignItem("switch2", 250.0)
    monster = GenericItem("monster", 2.0)
    spezie = ForeignItem("spezie", 3.0)
    libro = NormalItem("libro", 10.0)

    mio_store.inventory.add_stock(mela, 10)
    mio_store.inventory.add_stock(switch2, 3)
    mio_store.inventory.add_stock(monster, 15)
    mio_store.inventory.add_stock(spezie, 5)
    mio_store.inventory.add_stock(libro, 8)

    print("Welcome to the E-Store!")
    client_type = input("Insert client type: ").lower()

    if client_type == "generic customer":
        client = GenericCustomer(input("Insert client's name: "), int(input("Insert amount of money: ")))
        if not client.check_password(input("Insert password for the type of client you chose before: ")):
            print("Wrong password!")
            sys.exit(1)
    elif client_type == "normal customer":
        client = NormalCustomer(input("Insert client's name: "), int(input("Insert amount of money: ")))
        if not client.check_password(input("Insert password for the type of client you chose before: ")):
            print("Wrong password!")
            sys.exit(1)
    elif client_type == "promotional customer":
        client = PromotionalCustomer(input("Insert client's name: "), int(input("Insert amount of money: ")))
        if not client.check_password(input("Insert password for the type of client you chose before: ")):
            print("Wrong password!")
            sys.exit(1)
    else:
        print("Unrecognized type of client.")
        sys.exit(1)

    while True:
        print("\nThis is what we have in the store today, their quantities and their price:")
        for object in mio_store.inventory.items:
            print(f"{object.name} x {mio_store.inventory.items.get(object)} - {object.prezzo}$")

        chosen = input("Choose what'd you like to do, buy or quit? ").lower()
        if chosen != "buy":
            break

        print("Great! You chose to buy. Now choose what you want to buy and how many: ")
        tobuy = input("Item: ")
        quantity = int(input("Quantity: ")) 
        for object in mio_store.inventory.items:
            if object.name == tobuy:
                mio_store.sell_to_customer(object, quantity, client)
                

if __name__ == "__main__":
    start_app()


