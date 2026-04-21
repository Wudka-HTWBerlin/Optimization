from car_modules.start_car import start_car

import random

def main():
    distance=100000 #m
    min_w_power = 1 
    max_w_power = 20
    min_w_time = 1
    max_w_time = 20
    min_v_mass = 1200
    max_v_mass = 2200

    number_of_collaborators =8 # definition how many vehicles drive or fly together

    v_min = 80  #km/h
    v_max = 130  #km/h  

    car_configs = [
        {
            "w_power": random.randint(min_w_power, max_w_power),
            "w_time":  random.randint(min_w_time, max_w_time),
            "c_d":     round(random.uniform(0.2, 0.4), 2),
            "mass":    random.randint(min_v_mass, max_v_mass),
            "v_min":   v_min,
            "v_max":   v_max,
            "reaction_time": 0.5,
            "follow":  True if i > 0 else False
        }
        for i in range(number_of_collaborators)

    
    ]
    start_car(car_configs, driving_distance=distance)
 


if __name__ == "__main__":
    main()













            # {"w_power": 1, "w_time": 1, "c_d": 0.36, "mass": 1680, "v_min": v_min, "v_max": v_max, "reaction_time": 0.5, "follow": False},
        # {"w_power": 1, "w_time": 1, "c_d": 0.34, "mass": 1500, "v_min": v_min, "v_max": v_max, "reaction_time": 0.5, "follow": True},
        # {"w_power": 6, "w_time": 3, "c_d": 0.32, "mass": 1250, "v_min": v_min, "v_max": v_max, "reaction_time": 0.5, "follow": True},
        # {"w_power": 1, "w_time": 5, "c_d": 0.36, "mass": 1200, "v_min": v_min, "v_max": v_max, "reaction_time": 0.5, "follow": True},
        # {"w_power": 4, "w_time": 3, "c_d": 0.4, "mass": 1310, "v_min": v_min, "v_max": v_max, "reaction_time": 0.5, "follow": True},
        # {"w_power": 2, "w_time": 3, "c_d": 0.4, "mass": 1310, "v_min": v_min, "v_max": v_max, "reaction_time": 0.5, "follow": True},
        #  {"w_power": 4, "w_time": 9, "c_d": 0.36, "mass": 1200, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
        # {"w_power": 8, "w_time": 2, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
        # {"w_power": 7, "w_time": 1, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},