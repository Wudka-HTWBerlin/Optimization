from car_modules.start_car import start_car
from drone_modules.start_drone import start_drone
import random

def main():
    distance=10 #km
    drive_v_min = 20  #km/h
    drive_v_max = 60  #km/h  
    wind_direction= 0 #° 0°=North, 90°=East
    V_shape = True # if False colaboriotin in linear formation
    number_of_collabortors = 3 # definition how many vehicles drive or fly together
    A_drones =[]
    
    car = False

    if car:
        
        car_configs = [
            {"w_power": 3, "w_time": 3, "c_d": 0.36, "mass": 1680, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": False},
            {"w_power": 1, "w_time": 8, "c_d": 0.34, "mass": 1500, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            {"w_power": 6, "w_time": 3, "c_d": 0.32, "mass": 1250, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            {"w_power": 1, "w_time": 5, "c_d": 0.36, "mass": 1200, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            {"w_power": 4, "w_time": 3, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            {"w_power": 2, "w_time": 3, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
             {"w_power": 4, "w_time": 9, "c_d": 0.36, "mass": 1200, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            {"w_power": 8, "w_time": 2, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            {"w_power": 7, "w_time": 1, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
        
        ]
        start_car(car_configs, driving_distance=distance)
    else:
        
        for i in range(number_of_collabortors):
            
            x = random.uniform(0.5, 0.6)            
            y = random.uniform(0.7, 0.8)

            A_drones.append(x*y)
            
            
            

        drone_configs = [
            {"w_power": 3, "w_time": 3, "c_d": 0.36, "mass": 150, "v_min": drive_v_min, "v_max": drive_v_max,  "follow": False,  "A_drone" : A_drones[0], "total_numbers": number_of_collabortors , "V_shape": True, "wind_direction": wind_direction},
            {"w_power": 1, "w_time": 8, "c_d": 0.34, "mass": 200, "v_min": drive_v_min, "v_max": drive_v_max,  "follow": True,"A_drone" : A_drones[1], "total_numbers": number_of_collabortors , "V_shape": True, "wind_direction": wind_direction},
            {"w_power": 6, "w_time": 3, "c_d": 0.32, "mass": 250, "v_min": drive_v_min, "v_max": drive_v_max,  "follow": True,"A_drone" : A_drones[2], "total_numbers": number_of_collabortors , "V_shape": True, "wind_direction": wind_direction},
            # {"w_power": 1, "w_time": 5, "c_d": 0.36, "mass": 1200, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            # {"w_power": 4, "w_time": 3, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            # {"w_power": 2, "w_time": 3, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            # {"w_power": 4, "w_time": 9, "c_d": 0.36, "mass": 1200, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            # {"w_power": 8, "w_time": 2, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
            # {"w_power": 7, "w_time": 1, "c_d": 0.4, "mass": 1310, "v_min": drive_v_min, "v_max": drive_v_max, "reaction_time": 0.5, "follow": True},
        
        ]

        start_drone(drone_configs, flying_distance=distance)
       


if __name__ == "__main__":
    main()