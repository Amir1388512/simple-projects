import math
from time import sleep


gravitational_acceleration = {
    "Earth": 9.81,
    "Mars": 3.71,
    "Venus": 8.87,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.69,
    "Neptune": 11.15,
    "Pluto": 0.62
}


def drop_time(h, g):
    """
    This function calculates when the object reaches the ground.

    params:
        h = height in meters
        g = gravity in m/s²

    """
    return round(math.sqrt((2 * h) / g))  # Formula from physics


def speed_when_reach_to_earth(g, t):
    """
    This function calculates the speed of the object when it reaches the ground.

    params:
        g = gravity in m/s²
        t = time in seconds
    
    """
    return round((g * t))  # gt = v -> v = speed


while True:
    h = float(input('Type height (meters): '))
    g = input('Choose one planet in the solar system from this list \n[Earth, Mars, Venus, Jupiter, Saturn, Neptune, Uranus, Pluto] \nType ... ').capitalize()

    if g not in gravitational_acceleration:
        print('Your input is undefined. Please try again.\n')
    else:
        gravity = gravitational_acceleration[g]
        
        time = drop_time(h, gravity)
        speed = speed_when_reach_to_earth(gravity, time)

        time_step = 0.1
        current_time = 0

        print("\nTime (s)  |  Height (m)  |  Velocity (m/s)")
        print("--------------------------------------------")

        while current_time <= time:
            height = h - 0.5 * gravity * current_time**2  
            velocity = gravity * current_time
            
            # Display time, height, and velocity
            print(f"{current_time:.1f}  |  {height:.2f}  |  {velocity:.2f}")
            
            # Increase the time for the next iteration
            current_time += time_step
            sleep(0.1)
            
            
    continue_running = input("\nDo you want to calculate for another height and planet? (y/n): ").lower()
    if continue_running != 'y':
        break

    


