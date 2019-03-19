train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1


def fahrenheit_to_celsius(fahrenheit_temp):
    # Convert Fahrenheit temperature to Celsius
    celsius_temp = (fahrenheit_temp - 32) * 5 / 9
    return celsius_temp


# Test fahrenheit_to_celsius function
f100_in_celsius = fahrenheit_to_celsius(100)
print(f100_in_celsius)


def celsius_to_fahrenheit(celsius_temp):
    # Convert Celsius temperature to Fahrenheit
    fahrenheit_temp = celsius_temp * (9 / 5) + 32
    return fahrenheit_temp


# Test celsius_to_fahrenheit function
c0_in_fahrenheit = celsius_to_fahrenheit(0)
print(c0_in_fahrenheit)


def get_force(mass, acceleration):
    # Find force = mass * acceleration
    return mass * acceleration


# Test get_force function
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")


def get_energy(mass, c=3 * 10 ** 8):
    # Find energy
    return mass * c ** 2


# Test get_energy function
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")


def get_work(mass, acceleration, distance):
    # Find work value
    force = get_force(mass, acceleration)
    return force * distance


# Test get_work function
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
