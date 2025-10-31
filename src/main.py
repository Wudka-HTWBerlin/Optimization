import car_modules.start_car as start_car
import drone_modules.start_drone as start_drone

def main():
    distance=10 #km
    drive_v_min = 20  #km/h
    drive_v_max = 60  #km/h  
    
    car = True

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


        drone_configs = [
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
        start_drone(drone_configs, flying_distance=distance)
       


if __name__ == "__main__":
    main()