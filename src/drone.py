import math
import numpy as np
from typing import List
import matplotlib.pyplot as plt


class Car:
    def __init__(self, w_power,w_time,d_0, mass, water_min, water_max,v_min,v_max,reaction_time, follow):
        self.w_power = w_power
        self.w_time = w_time
        self.d_0 = d_0
        self.mass = mass
        self.v_min = v_min
        self.v_max = v_max
        self.r_t =reaction_time
        self.follow = follow
        self.g = 9.81  
        self.rho = 1.225           # Air thicknes  (kg/m^3)

    def P_drone(self, drone_effizency, front_windshield, C_D):
  
        P=[] 
        P_h = []
        for m in self.mass  :       
            F_g = m * self.g
            P_h.append(F_g / drone_effizency)

     
        
        for v in range(self.v_min, self.v_max+1):
            v= v/3.6

            F_Air = 0.5 * self.rho * front_windshield * C_D * (v ** 2)
            
            P_Vertical = F_Air * v

            P.append(P_hover + P_Vertical)

        return P_hover, P


    def SOC_calc(self,P, capacity):

    def Phover_calc(self, drone_effizency , drive_v_max: int) -> List[float]:
        PH = []
        F= self.mass * self.g
        for v in range(self.v_min, self.v_max+1):
            
            p_h = F / drone_effizency 
            PH.append(p_h)
            # print(f"{p_r}, {v}")

        PH.append(0.006 * self.mass * 9.81 * drive_v_max / 3.6)
        # print (f"This is P_R: {PR} at ")
        return PH

    def PL_calc(self,flight_dist, drive_v_max: int) -> List[float]:
        rho_s=1.225
        
        R=1
        k1 = 1.15
        v_0 = 8 #m/s
        A=R**2 * np.pi
        zeta = 0.03
        Omega =150
        mass = 125 # kg
        F = mass * self.g
        U_tip = Omega * R  
        p_i = (1 + k1) * (F**1.5) / np.sqrt(2 * rho_s * A)
        p_0 = (zeta / 8) * rho_s* A * Omega**3 * R**3
        PL = []
        d_0 = 0.1
       
        for v in range(self.v_min, self.v_max + 1):
            speed = (v) / 3.6
            
            distance = speed * self.r_t
            if self.follow:
                d_0= (0.11661 * math.log(33.992 * distance + 93.9171) - 0.0795772) * self.d_0
            else:
                d_0=self.d_0
           
            term1 = p_0 * (3 * v**2 / U_tip**2)
            term2_inner = np.sqrt(1 + (v**4) / (4 * v_0**4) - (v**2) / (2 * v_0**2))
            term2 = p_i * np.sqrt(term2_inner)
            term3 = (d_0 * rho_s * A * v**3) / 2   

            PL.append(term1 + term2 + term3)

        PL.append(self.d_0 * 2.25 * 1.2 / 2 * (drive_v_max / 3.6)**3)
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