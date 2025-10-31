import math
import numpy as np
from typing import List
import matplotlib.pyplot as plt



# es fhlt noch die gegneüberstellung der formation und die damit verbundene Auswirkung auf die Fläche der Drohnen, 
# das dann in der Power consunmptuion for atio eintragen hier dan P_L wie in car

class Drone:
    def __init__(self,
                  w_power,
                  w_time,
                  c_d,
                  mass ,
                  v_min,
                  v_max,
                  reaction_time,
                  follow ,
                  power_efficency,
                  wind_direction,
                  A_drone,
                  total_numbers,
                  V_shape):
        
        self_P_h : List = []
        self_P_v : List = []
        self.w_power = w_power
        self.w_time = w_time

        self.mass = mass
        self.v_min = v_min
        self.v_max = v_max
        self.r_t =reaction_time
        self.follow = follow
        
        self.g = 9.81      
        self.rho = 1.225   # Air thicknes  (kg/m^3)
        self.phi =wind_direction   #wind direction in degrees
        self.p_eff= power_efficency 
        self.total_numbers = total_numbers #drone power efficiency 
        self.V_shape = V_shape
        
        
        if follow:
            if V_shape:
                self.A_drone = A_drone/8
                self.c_d_= 0.5
                self.sigma = 0.9 # energy recovery value
            else:
                self.A_drone = A_drone * 0.8
                
                self.sigma = 0.8 # energy recovery value
                
        else: 
            self.A_drone = A_drone
            self.c_d = c_d
        


    def P_vertical(self, v_w, phi):
  
        P_vert=[] 
               
        for v in range(self.v_min, self.v_max+1):
            v_f= v/3.6
            if self.follow and not self.V_shape:
                distance = v_f * self.r_t
                self.c_d= (0.11661 * math.log(33.992 * distance + 93.9171) - 0.0795772) * self.c_d 

            F_constant= 0.5 * self.rho * self.A_drone * self.c_d * ((v_f+v_w) ** 2)

            F_vertical = F_constant * v_f/ self.sigma

            F_wind = F_constant * (math.sin(phi/2)**3) * v_w 
            
            P_Vertical = (F_vertical - F_wind)

            P_vert.append(P_Vertical)

        return P_vert

    def P_hover(self, water_min, water_max) -> List[float]:
        P_h = []
        for water in range (water_min, water_max):       
            F_g = (water+self.mass) * self.g
            P_h.append(F_g/self.p_eff )

        return P_h
    
    def P(self, P_hover, P_vert):
        P=[]
        for p_v in P_vert:
            p=[]
            for p_h in P_hover:
                p.append(p_v+p_h)
            P.append(p)
        return P
    
    def SOC_calc(self,P, capacity):
        SOC= []
        #nicht nützlich da keine auswirkung auf die Optimierung da sich dieser Wert aus der entnommen Leistung ergibt 
        return SOC
            
class DroneCoopMath:

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