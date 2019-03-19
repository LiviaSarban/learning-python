train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# Convert Fahrenheit temperature to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Test f_to_c function
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Convert Celsius temperature to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# Test c_to_f function
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Find force = mass * acceleration
def get_force(mass, acceleration):
  return (mass * acceleration)

# Test get_force function
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Find energy
def get_energy(mass, c=3*10**8):
  return(mass*c**2)

# Test get_energy function
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Find work value
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

# Test get_work function
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")