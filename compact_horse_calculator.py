def welcome():
    print("Welcome to the ideal horse calculator!"'\n')

def main():
    welcome()
    jump_input()
    speed_input()
    health_input()
    distance_from_ideal()
    comparision_plack()

def jump_input():
    global jump_percentage
    whole_blocks = float(input("How many whole blocks can the horse jump? "))
    snow_layers = float(input("How many snow layers can it jump above the whole blocks? "))
    max_jump = whole_blocks + (snow_layers / 8)
    max_jump_value = (max_jump / 5.293) ** (1 / (3 ** 0.5))
    jump_percentage = get_percentage(max_jump_value, 0.995301, 0.382094) #ideal_jump_value = 0.9953015590933703 #min_jump_value = 0.3820942627538009

def speed_input():
    global speed_percentage
    max_speed = float(input("What is the horse's maximum speed in blocks per second? "))
    speed_percentage = get_percentage(max_speed, 14.6, 4.8) # ideal_speed = 14.6 # min_speed = 4.8

def health_input():
    global health_percentage
    hearts = int(input("How many hearts of health does the horse have? "))
    extra_hearts = int(input("How many extra half hearts does the horse have? "))
    max_health = 2 * hearts + extra_hearts
    health_percentage = get_percentage(max_health, 30, 15) #ideal_health = 30 # min_health = 15

def get_percentage(actual, ideal, minimum):
    return (actual - minimum)/(ideal - minimum)

def cube_of_sphere(radius):
    pi = 3.14159265358979
    if radius <= 1:
        return 1/6 * pi * (radius) ** 3
    if radius <= 2 ** 0.5:
        return 1/6 * pi * (radius) ** 3 - pi * (2 * (radius)**3 - 3 * (radius)**2 + 1) / 4.
    if radius < 3 ** 0.5:
       print("this horse is too bad to compare)")
    return 1

def distance_from_ideal():
    global score
    radius = ((1-jump_percentage)**2 + (1-speed_percentage)**2 + (1-health_percentage)**2) ** 0.5
    score = 1 - cube_of_sphere(radius)

def comparision_plack():
    print('\n''  COMPARISON PLACK')
    print(f'Total Score = {100*score:.2f}%')
    print(f'Jump   = {100*jump_percentage:.2f}%')
    print(f'Speed  = {100*speed_percentage:.2f}%')
    print(f'Health = {100*health_percentage:.2f}%')

main()
#in 64 minutes I shortened this code from 180 lines of code to 59 lines of code