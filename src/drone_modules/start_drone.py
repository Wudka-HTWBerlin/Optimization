from drone_modules.drone import Drone, DroneCoopMath
from drone_modules.swarm import Optimization
from drone_modules.los_calc import DroneCalculation

def start_car(car_configs, flying_distance):
    driving_distance = 100 # km
    water_min = 20 # l
    water_max = 50 # l

    v_wind = 10 #m/s
    wind_direction = 0 #°  North= 0° East=90°
  
    
    data_names = ["system1", "system2", "system3", "speed"]
    # === Fahrzeugspezifikationen definieren ===
    

    all_losses = []
    data_names = []
    all_achives = []
    calc = DroneCalculation()
    opt = Optimization() 

    for i, cfg in enumerate(car_configs):
        drone = Drone(**cfg)

        speed_list = list(range(drone.drive_v_min, drone.drive_v_max+1))
        time_loss = calc.time_los_calc(drone.v_min, drone.v_max, flying_distance)
        drone.P_h = drone.P_hover(water_max=water_max, water_min=water_min)
        drone.P_v = drone.P_vertical(v_w=v_wind, phi=wind_direction)

        P_red = calc.P_reduction_calc(drone.P_h, drone.P_v)
        
        achieve = opt.Achievment(P_red, time_loss, Drone.w_power, Drone.w_time)
        losses = opt.Optimization_losses(achieve)

        all_achives.append(achieve)
        all_losses.append(losses)
        data_names.append(f"System {i + 1}")


    # === Coop/Decision ===
    ccm = DroneCoopMath()
    ccm.file_output(all_losses,all_achives, speed_list, "LossesAll", data_names)

    # performance = ccm.performance_values(losses1, losses2, losses3)
    performance = ccm.performance_values(all_losses)
    if performance:
        min_index = performance.index(min(performance))
        best_speed = speed_list[min_index]
        print(f"\n🚗 The cars should drive with a speed of {best_speed} km/h")
        for name, losses in zip(data_names, all_losses):
            print(f"Loss for {name}: {losses[min_index]:.2f}")

    else:
        print("No valid performance data found.")