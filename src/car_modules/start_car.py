# === Verarbeitungsschritte für alle Fahrzeuge ===
from car_modules.car import Car , CarCoopMath
from car_modules.los_calc import CarCalculation
from optimization import Optimization

def start_car(car_configs, driving_distance):
   
    data_names = ["system1", "system2", "system3", "speed"]
    # === Fahrzeugspezifikationen definieren ===
    

    all_losses = []
    data_names = []
    all_achives = []
    calc = CarCalculation()
    opt = Optimization() 
    for i, cfg in enumerate(car_configs):
        car = Car(**cfg)
        speed_list = list(range(car.v_min, car.v_max+1))
        time_loss = calc.time_los_calc(car.v_min, car.v_max, driving_distance)
        car.P_R = car.PR_calc(drive_v_max=car.v_max)
        car.P_L = car.PL_calc(drive_v_max=car.v_max)

        P_red = calc.P_reduction_calc(car.P_L, car.P_R)
        
        achieve = opt.Achievment(P_red, time_loss, car.w_power, car.w_time)
        losses = opt.Optimization_losses(achieve)

        all_achives.append(achieve)
        all_losses.append(losses)
        data_names.append(f"System {i + 1}")


    # === Coop/Decision ===
    ccm = CarCoopMath()
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