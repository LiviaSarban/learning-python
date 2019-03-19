# Alternative version where each shipping method uses a separate function


def shipping_cost_ground(weight):
    # Calculates ground shipping cost
    if weight <= 2:
        cost_per_pound = 1.50
    elif 2 < weight <= 6:
        cost_per_pound = 3.00
    elif 6 < weight <= 10:
        cost_per_pound = 12.00
    else:
        cost_per_pound = 4.75

    flat_charge = 20

    return cost_per_pound * weight + flat_charge


def shipping_cost_premium_ground(weight):
    # Calculates premium ground shipping cost

    flat_charge = 125.00

    return flat_charge


def shipping_cost_drone(weight):
    # Calculates drone shipping cost
    if weight <= 2:
        cost_per_pound = 4.50
    elif 2 < weight <= 6:
        cost_per_pound = 9.00
    elif 6 < weight <= 10:
        cost_per_pound = 12.00
    else:
        cost_per_pound = 14.25

    flat_charge = 0

    return cost_per_pound * weight + flat_charge


def print_cheapest_shipping_method(weight):
    # Compares shipping costs and displays the cheapest shipping method

    ground = shipping_cost_ground(weight)
    premium = shipping_cost_premium_ground(weight)
    drone = shipping_cost_drone(weight)

    if ground >= premium <= drone:
        method = "premium ground"
        cost = premium
    elif premium >= drone <= ground:
        method = "drone"
        cost = drone
    else:
        method = "standard ground"
        cost = ground

    print("The cheapest option available is $%.2f with %s shipping." % (cost, method))

    # Displays costs for all methods
    print("Here is the breakdown:")
    print("* Ground shipping: $%.2f" % ground)
    print("* Drone shipping: $%.2f" % drone)
    print("* Premium ground shipping: $%.2f" % premium)


print_cheapest_shipping_method(41.5)

# Later to-do: display the shipping methods by cost (cheapest first)
