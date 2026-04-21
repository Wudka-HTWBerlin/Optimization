
from drone_modules.start_drone import start_drone
import random

def main():
    distance=5000 #m
    
    wind_direction= 0 #° 0°=North, 90°=East
    wind_speed = 10 # m/s
    min_w_power = 1 
    max_w_power = 20
    min_w_time = 1
    max_w_time = 20
    min_mass = 105
    max_mass= 120
    number_of_collaborators =10 # definition how many vehicles drive or fly together

    v_min = 20  #km/h
    v_max = 60  #km/h  
  
    drone_configs = [
        {
            "w_power": random.randint(min_w_power, max_w_power),
            "w_time":  random.randint(min_w_time, max_w_time),
            "c_d":     round(random.uniform(0.85, 0.95), 2),
            "mass":    random.randint(min_mass, max_mass),
            "v_min":   v_min,
            "v_max":   v_max,
            "follow":  True if i > 0 else False, 
            "A_drone": random.uniform(0.5, 0.6) * random.uniform(0.7, 0.8)
        }
        for i in range(number_of_collaborators)
    ]   
        

    
    start_drone(drone_configs, flying_distance=distance, w_direction = wind_direction, w_speed = wind_speed)
       


if __name__ == "__main__":
    main()









    # drone_configs = [
    #     {"w_power": 2  ,    "w_time": 5  , "c_d": 0.87, "mass": 120, "v_min": v_min, "v_max": v_max, "follow": False,  "A_drone" : A_drones[0]  },
    #     {"w_power": 3,      "w_time":  7  , "c_d": 0.9, "mass": 140, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[1]  },
    #     {"w_power": 16  ,   "w_time": 3 , "c_d": 0.92, "mass": 110, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[2] },
    #     {"w_power": 2  ,    "w_time": 11 , "c_d": 0.95, "mass": 115, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[3] },
    #     {"w_power": 1 ,     "w_time": 4 , "c_d": 0.91, "mass": 130, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[4]},
    #     {"w_power": 10  ,   "w_time": 8 , "c_d": 0.9, "mass": 125, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[5]},
    #     {"w_power": 9  ,    "w_time": 1 , "c_d": 0.86, "mass": 112, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[6] },
    #     {"w_power": 6 ,     "w_time": 2 , "c_d": 0.87, "mass": 116, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[7] },
    #     {"w_power": 15  , "w_time": 1 , "c_d": 0.91, "mass": 119, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[8] },
    #     {"w_power": 8  , "w_time": 20 , "c_d": 0.89, "mass": 133, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[9] },
    #     {"w_power": 3  , "w_time": 11, "c_d": 0.92, "mass": 126, "v_min": v_min, "v_max": v_max,  "follow": True,"A_drone" : A_drones[10]},

    
    # ]
