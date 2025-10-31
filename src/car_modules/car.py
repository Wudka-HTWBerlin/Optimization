import math
import numpy as np
from typing import List
import matplotlib.pyplot as plt


class Car:
    def __init__(self, w_power,w_time,c_d, mass,v_min,v_max,reaction_time, follow):
        self.P_R : List = []
        self.P_L : List = []
        self.w_power = w_power
        self.w_time = w_time
        self.c_d = c_d
        self.mass = mass
        self.v_min = v_min
        self.v_max = v_max
        self.r_t =reaction_time
        self.follow = follow


    def PR_calc(self, drive_v_max: int) -> List[float]:
        PR = []
        for v in range(self.v_min, self.v_max+1):
            p_r = 0.006 * self.mass * 9.81 * (v / 3.6) 
            PR.append(p_r)
            # print(f"{p_r}, {v}")

        PR.append(0.006 * self.mass * 9.81 * drive_v_max / 3.6)
        # print (f"This is P_R: {PR} at ")
        return PR

    def PL_calc(self, drive_v_max: int) -> List[float]:
        PL = []
        c_d = 0
        for v in range(self.v_min, self.v_max + 1):
            speed = (v) / 3.6
            distance = speed * self.r_t
            if self.follow:
                c_d= (0.11661 * math.log(33.992 * distance + 93.9171) - 0.0795772) * self.c_d
            else:
                c_d=self.c_d
                
            PL.append(2.25 * 1.2 / 2 * c_d * speed**3)

        PL.append(self.c_d * 2.25 * 1.2 / 2 * (drive_v_max / 3.6)**3)
        # print (f"This is P_L: {PL}")
        return PL


class CarCoopMath:

    def file_output(self, all_losses: List[List[float]],all_achives: List[List[float]], speeds: List[int], name: str, data_names: List[str]):
    

        filename = f"{name}.csv"
        with open(filename, "w") as file:
            file.write("\t".join(data_names + ["Speed"]) + "\n")
            for i in range(len(speeds)):
                row = [f"{achives[i]:.2f}" for achives in all_achives] + [str(speeds[i])]
                # row = [f"{losses[i]:.2f}" for losses in all_losses] + [str(speeds[i])]
                file.write("\t".join(row) + "\n")

        # Plot
        # for losses, label in zip(all_losses, data_names):
        for achives, label in zip(all_achives, data_names):
            plt.plot(speeds, achives, label=label)
        plt.xlabel("Speed (km/h)")
        plt.ylabel("Loss (%)")
        plt.title("Losses for all systems")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{name}.png")
        plt.show()

        for losses, label in zip(all_losses, data_names):
            plt.plot(speeds, losses, label=label)
        plt.xlabel("Speed (km/h)")
        plt.ylabel("Loss (%)")
        plt.title("Losses for all systems")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{name}.png")
        plt.show()
    
    
    def performance_values(self, all_losses: List[List[float]]) -> List[float]:
        if not all_losses:
            print("No loss data provided.")
            return []

        # Prüfe, ob alle Loss-Listen die gleiche Länge haben
        length = len(all_losses[0])
        if not all(len(losses) == length for losses in all_losses):
            print("Loss vector sizes are differing")
            for idx, losses in enumerate(all_losses):
                print(f"losses{idx+1} size= {len(losses)}")
            return [0] * length

        # Summiere für jeden Geschwindigkeitsindex die Verluste aller Systeme
        performance_vector = []
        for losses_at_speed in zip(*all_losses):  # Transponiert -> [(l1_1, l2_1, ..., ln_1), ..., (l1_n, ..., ln_n)]
            performance_vector.append(sum(losses_at_speed))

        return performance_vector