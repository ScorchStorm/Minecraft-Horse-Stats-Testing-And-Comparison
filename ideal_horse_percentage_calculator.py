from math import pi
from scipy.integrate import quad
from numpy import sqrt, cos, arccos

"These are the max measurable values, change them if your measurement device becomes more or less precise."
"The ideal (highest possible) values are - jump: 5.29 blocks, speed: 14.57 blocks/second, health: 30 points"

"currently measurable to 1/8th block"
ideal_jump = 5.25
"currently measurable to 0.2 meters/second" "I'm assuming the measurement can round up"
ideal_speed = 14.6
"always exactly measurable"
ideal_health = 30

min_jump = 1
min_speed = 4.8
min_health = 15

# create variables, the current values are placeholders.
extra_hearts = -1
jump_percentage = -1
speed_percentage = -1
health_percentage = -1
percentage_ideal = -1
percentage_from_ideal = -1
score = -1

def welcome():
    print("")
    print("Welcome to the ideal horse calculator!")
    print("")

def main():
    welcome()
    jump_percentage, max_jump = jump_input("max jump height")
    speed_percentage, max_speed = speed_input("max speed")
    health_percentage, max_health = health_input("max health")
    score = calculate_score(jump_percentage, speed_percentage, health_percentage)
    comparision_plack(score, jump_percentage, speed_percentage, health_percentage)
    #stats_plack(score, max_jump, max_speed, max_health)

def test():
    jump_percentage = float(input("What is the jump percentage? "))/100
    speed_percentage = float(input("What is the speed percentage? "))/100
    health_percentage = float(input("What is the health percentage? "))/100
    print('')
    calculate_score(jump_percentage, speed_percentage, health_percentage)

def jump_input(name):
    print(name.title())
    whole_blocks = float(input("How many whole blocks can the horse jump? "))
    snow_layers = float(input("How many snow layers can it jump above the whole blocks? "))
    min_jump_value = calculate_jump_value(min_jump)
    ideal_jump_value = calculate_jump_value(ideal_jump)
    max_jump = whole_blocks + (snow_layers / 8)
    max_jump_value = calculate_jump_value(max_jump)
    jump_percentage = get_percentage(name, max_jump_value, ideal_jump_value, min_jump_value)
    print("")
    return(jump_percentage, max_jump)

def calculate_jump_value(jump):
    jump_value = (jump / 5.293) ** (1 / (3 ** 0.5))
    return(jump_value)

def speed_input(name):
    print(name.title())
    max_speed = float(input("What is the horse's maximum speed in blocks per second? "))
    speed_percentage = get_percentage(name, max_speed, ideal_speed, min_speed)
    print("")
    return(speed_percentage, max_speed)

def health_input(name):
    print(name.title())
    hearts = int(input("How many hearts of health does the horse have? "))
    extra = input("(Yes/No) Does the horse have an extra half heart of health? ")
    if extra.lower() == "yes" or extra.lower() == "y":
        extra_hearts = 1
    elif extra.lower() == "no" or extra.lower() == "n":
        extra_hearts = 0
    else:
        print("Sorry, that's not a valid answer. Please try again")
    max_health = 2 * hearts + extra_hearts
    health_percentage = get_percentage(name, max_health, ideal_health, min_health)
    print("")
    return(health_percentage, max_health)

def get_percentage(variable, actual, ideal, minimum):
    percent = (actual - minimum)/(ideal - minimum)
    print(f"The horse's {variable} is {100*percent:.2f}% of the max!")
    return(percent)

def pythagoras_theorem(distance1, distance2, distance3):
    total_distance = ((distance1 ** 2) + (distance2 ** 2) + (distance3 ** 2)) ** 0.5
    return(total_distance)

def cube_of_sphere(radius):
    if radius <= 1:
        return 1/6 * pi * (radius) ** 3
    if radius <= sqrt(2):
        return 1/6 * pi * (radius) ** 3 - pi * (2 * (radius)**3 - 3 * (radius)**2 + 1) / 4.
    if radius < sqrt(3):
        return 2 * (0.5 * ( sqrt(radius**2 - 2)) + region_2(radius) + region_3(radius))
    return 1

#square regions
def region_1_2_theta(radius):
    return arccos(1 / sqrt(radius ** 2 - 1))

#curved square regions
def region_2_integrand(theta, radius):
    return sqrt(cos(theta) ** 2 - (1 / radius)**2) / (cos(theta) ** 3)

def region_2(radius):
    i4 = 1 / 6 * (radius**2 / - 1) * (pi / 4 - region_1_2_theta(radius))
    i3 = radius / 3. * quad(region_2_integrand, region_1_2_theta(radius), pi / 4, args=(radius))[0] 
    return i4 + i3

#spherical region
def region_3_integrand(theta, radius):
    return sqrt(cos(theta) ** 2 - (1 / radius)**2) / cos(theta)

def region_3(radius):
    return radius ** 3 / 3. * (1 / radius * (pi / 4 - region_1_2_theta(radius)) - quad(region_3_integrand, region_1_2_theta(radius), pi / 4, args=(radius))[0])

def trirectangular_tetrahedron(side):
    volume = side**3/6
    return(volume)

def distance_from_origin(jump_percentage, speed_percentage, health_percentage):
    radius = pythagoras_theorem(jump_percentage, speed_percentage, health_percentage)
    distance_percentage = radius / (3**0.5)
    #print(f'The horse is {100*distance_percentage:.2f}% of the largest possible distance from the origin.')
    volume = cube_of_sphere(radius)
    print(f'The horse is further from the origin than {100*volume:.2f}% of horses.')

def distance_from_ideal(jump_percentage, speed_percentage, health_percentage):
    radius = pythagoras_theorem(1-jump_percentage, 1-speed_percentage, 1-health_percentage)
    distance_percentage = radius / (3**0.5)
    #print(f'The horse is {100*distance_percentage:.2f}% of the total distance to ideal.')
    volume = cube_of_sphere(radius)
    compare = 100*(1-volume)
    print(f'The horse is more ideal than {compare:.2f}% of horses.')
    return(compare)

def linear_addition(jump_percentage, speed_percentage, health_percentage):
    addition = (jump_percentage + speed_percentage + health_percentage)
    #print(f'The horse has {(100*addition/3):.2f}% of all ideal attributes by simple addition')
    side = addition
    if side <= 1:
        volume = trirectangular_tetrahedron(side)
    elif side >= 1 and side <= 2:
        volume = trirectangular_tetrahedron(side) - 3*trirectangular_tetrahedron(side-1)
    elif side >= 2 and side <= 3:
        volume = trirectangular_tetrahedron(side) - 3*trirectangular_tetrahedron(side-1) + 3*trirectangular_tetrahedron(side-2)
    print(f'The horse has a greater percentage of ideal attributes than {100*volume:.2f}% of horses')

def calculate_score(jump_percentage, speed_percentage, health_percentage):
    linear_addition(jump_percentage, speed_percentage, health_percentage)
    distance_from_origin(jump_percentage, speed_percentage, health_percentage)
    score = distance_from_ideal(jump_percentage, speed_percentage, health_percentage)
    print("")
    return(score)

def comparision_plack(score, jump_percentage, speed_percentage, health_percentage):
    print('  COMPARISON PLACK')
    print(f'Total Score = {score:.2f}%')
    print(f'Jump   = {100*jump_percentage:.2f}%')
    print(f'Speed  = {100*speed_percentage:.2f}%')
    print(f'Health = {100*health_percentage:.2f}%')
    print('')

def stats_plack(score, max_jump, max_speed, max_health):
    print('    STATS PLACK')
    print(f'Total Score = {score:.2f}%')
    print(f'Jump: {max_jump//1:.0f} + {8*(max_jump %1)//1:.0f}/8 Blocks')
    print(f'speed:  {max_speed:.0f} m/s')
    print(f'Health: {max_health:.0f} HP')
    print('')

main()