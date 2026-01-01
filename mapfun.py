products = [
                ("Processor",250),
                ("Graphic Card",500),
                ("RAM",100),
                ("SSD",150)
            ]

def applyDiscount(component):
    name,price = component
    disc_price = price * 0.9
    return (name,disc_price)

disc_products = list(map(applyDiscount,products))
print(disc_products)