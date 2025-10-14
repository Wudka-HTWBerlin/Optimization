from car import Car , CarCoopMath
from platoon import Optimization, Calculation

def main():
    driving_distance = 100
    drive_v_min = 80
    drive_v_max = 140
    speeds = list(range(drive_v_min, drive_v_max+1))
    data_names = ["system1", "system2", "system3", "speed"]
    # === Fahrzeugspezifikationen definieren ===
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
        # weitere Fahrzeuge kannst du einfach hier hinzufügen
    ]

    # === Verarbeitungsschritte für alle Fahrzeuge ===
    all_losses = []
    data_names = []
    all_achives = []
    for i, cfg in enumerate(car_configs):
        car = Car(**cfg)
        calc = Calculation()
        opt = Optimization()

        time_loss = calc.time_los_calc(car.v_min, car.v_max, driving_distance)
        car.P_R = car.PR_calc(drive_v_max=drive_v_max)
        car.P_L = car.PL_calc(drive_v_max=drive_v_max)

        P_red = calc.P_reduction_calc(car.P_L, car.P_R)
        
        achieve = opt.Achievment(P_red, time_loss, car.w_power, car.w_time)
        losses = opt.Optimization_losses(achieve)

        all_achives.append(achieve)
        all_losses.append(losses)
        data_names.append(f"System {i + 1}")


    # === Coop/Decision ===
    ccm = CarCoopMath()
    ccm.file_output(all_losses,all_achives, speeds, "LossesAll", data_names)

    # performance = ccm.performance_values(losses1, losses2, losses3)
    performance = ccm.performance_values(all_losses)
    if performance:
        min_index = performance.index(min(performance))
        best_speed = speeds[min_index]
        print(f"\n🚗 The cars should drive with a speed of {best_speed} km/h")
        for name, losses in zip(data_names, all_losses):
            print(f"Loss for {name}: {losses[min_index]:.2f}")

    else:
        print("No valid performance data found.")

if __name__ == "__main__":
    main()