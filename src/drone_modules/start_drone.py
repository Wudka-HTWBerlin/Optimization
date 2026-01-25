from drone_modules.drone import Drone
from drone_modules.swarm import Optimization
from drone_modules.los_calc import DroneCalculation
from drone_modules.coop_math import DroneCoopMath
from drone_modules.constraints import constraints

from  ex_sys import exclude_systems 
# import constraints as c
import numpy as np


def start_drone(drone_configs, flying_distance, w_direction, w_speed ):
    
#    c.constraints(n_drones,max_speed, min_speed, total_length=flying_distance)

    data_names = ["System_"+str(system) for system in range( len(drone_configs) )]
    data_names.append("speed")
        
    # === Fahrzeugspezifikationen definieren ===
    
    PH=[]
    predu=[]
    all_losses = []
    
    all_achives = []
    calc = DroneCalculation()

    opt = Optimization() 

    ccm = DroneCoopMath(plot_2D=False, plot_3D=False)

    for cfg in drone_configs:
        drone = Drone(**cfg)

        speed_list = list(range(drone.v_min, drone.v_max+1))
        time_loss = calc.time_los_calc(drone.v_min, drone.v_max, flying_distance)
        drone.P_h = drone.P_hover()
        # ccm.plot_data_2D_from_2d(data_names="PH",data=drone.P_h )
        PH.append(drone.P_h)
        
        phred= drone.P_h/np.max(drone.P_h)

        drone.P_v = drone.P_vertical(v_w=w_speed, phi=w_direction)

        P_red = calc.P_reduction_calc(drone.P_h, drone.P_v)
        
        achieve = opt.Achievment(P_red, time_loss, drone.w_power, drone.w_time)
        losses = opt.Optimization_losses(achieve)

        predu.append(phred)
        all_achives.append(achieve)
        all_losses.append(losses)
        

    ccm.plot_data_2D_from_2d(data_names,predu, True, "ph_redu")
    ccm.plot_data_2D_from_2d(data_names ,PH,True, "PH all drones")

    # === Coop/Decision ===
    
    # ccm.file_output(all_losses, "LossesAll", data_names)
    # ccm.file_output(all_achives, "LossesAll", data_names)

    # performance = ccm.performance_values(losses1, losses2, losses3)
    sum_ph = ccm.sum_array(PH)
    sum_array = ccm.sum_array(all_achives)
    ccm.plot_data_2D_from_2d(data_names="PH",data=sum_ph,threeD_list=False, title="sum_PH")
    ccm.plot_data_2D(data_names, all_achives, title="all_achives")
    ccm.plot_data_3D(sum_array, "LossesAll", "performance data")
    turning_point_speed, turning_point_mass=ccm.turning_point(sum_array)


    print(f"Position (Zeile, Spalte): ({turning_point_speed}, {turning_point_mass})")
    # min_index = performance.index(min(performance))
    best_speed = speed_list[turning_point_speed]
    water_mass = turning_point_mass + 20
    
    set_speed, inex_drones = constraints(len(drone_configs), flying_distance, water_mass, best_speed )
    if inex_drones<0:

        ex_system=exclude_systems(abs(inex_drones), all_losses, speed_list.index(set_speed), turning_point_mass )

    print(f" The drones should fly with a speed of {set_speed} km/h and using a water mass of {water_mass}l ")
    
    for idx, (name, loss) in enumerate(zip(data_names, all_losses)):
        if idx in ex_system:
            print(f"Skipping {name}: System is excluded and had a loss of {loss[speed_list.index(set_speed)][turning_point_mass]:.5f}")
            continue  # Skip to the next system
        else:
            print(f"Loss for {name}: {loss[speed_list.index(set_speed)][turning_point_mass]:.5f}")

    