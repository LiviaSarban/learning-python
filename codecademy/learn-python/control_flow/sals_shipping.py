def cost(weight):
    # Sets ground and drone shipping price per pound
    if weight <= 2:
        ground_price = 1.50
        drone_price = 4.50
    elif 2 < weight <= 6:
        ground_price = 3.00
        drone_price = 9.00
    elif 6 < weight <= 10:
        ground_price = 4.00
        drone_price = 12.00
    else:
        ground_price = 4.75
        drone_price = 14.25

    # Sets flat charges for the 3 shipping methods
    ground_flat_charge = 20
    drone_flat_charge = 0
    premium_ground_flat_charge = 125.00

    # Calculates shipping costs for each method
    ground_shipping = ground_price * weight + ground_flat_charge
    drone_shipping = drone_price * weight + drone_flat_charge
    premium_ground_shipping = premium_ground_flat_charge

    # Compares shipping costs and displays the cheapest shipping method
    if premium_ground_shipping <= ground_shipping and premium_ground_shipping <= drone_shipping:
        print("We recommend using premium ground shipping. Your package will cost $", premium_ground_shipping, ".")
    elif drone_shipping < premium_ground_shipping and drone_shipping <= ground_shipping:
        print("We recommend using drone shipping. Your package will cost $", drone_shipping, ".")
    else:
        print("We recommend using ground shipping. Your package will cost $", ground_shipping, ".")

    # Displays costs for all methods
    print('Here is the breakdown:')
    print('* Ground shipping: $', ground_shipping)
    print('* Drone shipping: $', drone_shipping)
    print('* Premium ground shipping: $', premium_ground_shipping)


cost(41.5)

# Later to-dos: round the shipping costs to two digits and display the shipping methods by cost (cheapest first)
