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
                  follow ,
                #   power_efficency,
                  A_drone,
                  total_numbers,
                  V_shape,
                  wind_direction):
       
        self.P_h = []
        self.P_v =[]
        self.w_power = w_power
        self.w_time = w_time

        

        self.mass = mass
        self.v_min = v_min
        self.v_max = v_max
        self.r_t = 0.5
        self.follow = follow

        ## Drone specifications
        self.v_0= 22 #m/s
        self.n = 4  #amount of rotors
        self.delta = 0.012 # profile drag coefficent
        self.s_bl= 0.15 #middle Solidity 0.1 bis 0.25
        self.C_T = 0.09   #0.08 bis 0.15 thrust coefficent
        self.k = 0.11 # Incremental correction factor to induced power
        self.g = 9.81      #m/s^2
        self.rho = 1.225   # Air thicknes  (kg/m^3)
        self.R_bl= 0.5      # m
        self.water_min = 20 # l
        self.water_max = 50 # l

        self.phi =wind_direction   #wind direction in degrees
        # self.p_eff= power_efficency 
        self.total_numbers = total_numbers #drone power efficiency 
        self.V_shape = V_shape
        self.A_bl= self.R_bl**2 *math.pi 
        

        # Results
        # self.P_bl = [ ]
        # self.P_in = [ ]
        
        if follow:
            if V_shape:
                self.A_drone = A_drone/8
                self.c_d= 0.5
                self.sigma = 0.9 # energy recovery value
            else:
                self.A_drone = A_drone * 0.8
                
                self.sigma = 0.8 # energy recovery value
                
        else: 
            self.A_drone = A_drone
            self.c_d = c_d
            self.sigma =0.2


    def P_vertical(self, v_w, phi ):
  
        P_vert=[] 
               
        for v_t in range(self.v_min, self.v_max+1):
            v_f= v_t/3.6
            if self.follow and not self.V_shape:
                distance = v_f * self.r_t
                self.c_d= (0.11661 * math.log(33.992 * distance + 93.9171) - 0.0795772) * self.c_d 
 
            v= v_f+v_w    
            P_constant= 0.5 * self.rho * self.A_drone * self.c_d * v**2

            P_vertical = P_constant * v_f/ self.sigma

            P_wind = P_constant * (math.sin(phi/2)**3) * v_w 
            
            P_Vertical = (P_vertical - P_wind)

            P_vert.append(P_Vertical)

        return P_vert

    def P_hover(self, ) :
        P_h = []
        n=4
        
        for water in range (self.water_min, self.water_max):       
            F_g = (water+self.mass) * self.g
            p_bl = F_g**(3/2)/(math.sqrt(n*self.rho*self.A_bl) )*self.C_T**(-3/2) *self.delta/8 * self.s_bl  
            p_in = (1+self.k)*(F_g**(3/2)/(math.sqrt(2*self.rho*self.A_bl)))
            P_h.append(p_bl+p_in)
            # self.P_bl.append(p_bl)
            # self.P_in.append(p_in)

        return P_h
    
    


    def SOC_calc(self,P, capacity):
        SOC= []
        #nicht nützlich da keine auswirkung auf die Optimierung da sich dieser Wert aus der entnommen Leistung ergibt 
        return SOC
            
class DroneCoopMath:

    def file_output(self, all_losses ,all_achives, speeds: List[int], name: str, data_names: List[str]):
        #x = speed
        #y=mass
        #z=time
        # --- 2. 3D Plot erstellen ---
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        for achives in  all_achives:
            
            x_coords_achieves = np.arange(achives.shape[0])
            z_coords_achieves = np.arange(achives.shape[1])
            X_achives, Z_achives = np.meshgrid(z_coords_achieves, x_coords_achieves)

            

            surf = ax.plot_surface(Z_achives, X_achives, achives, 
                       cmap='viridis', # Farbschema
                       rstride=1, cstride=1, # Steuerungen für Detailgrad
                       antialiased=False)
            
            # 3. Beschriftungen und Farbleiste
            

            # Farbleiste für die Y-Werte
            fig.colorbar(surf, shrink=0.6, aspect=20, label='Y-Wert')
        ax.set_xlabel('mass')
        ax.set_zlabel('speed')
        ax.set_ylabel('achievement')
        ax.set_title('3D Oberfläche: X, Z bestimmen Position, Y ist Wert')
        plt.show()
                        
                        

         
        # filename = f"{name}.csv"
        # with open(filename, "w") as file:
        #     file.write("\t".join(data_names + ["Speed"]) + "\n")
        #     for i in range(len(speeds)):
        #         row = [f"{achives[i]:.2f}" for achives in all_achives] + [str(speeds[i])]
        #         # row = [f"{losses[i]:.2f}" for losses in all_losses] + [str(speeds[i])]
        #         file.write("\t".join(row) + "\n")

        # Plot
        # for losses, label in zip(all_losses, data_names):
        # for achives, label in zip(all_achives, data_names):
        #     plt.plot(speeds, achives, label=label)
        # plt.xlabel("Speed (km/h)")
        # plt.ylabel("Loss (%)")
        # plt.title("Losses for all systems")
        # plt.legend()
        # plt.grid(True)
        # plt.tight_layout()
        # plt.savefig(f"{name}.png")
        # plt.show()

        # for losses, label in zip(all_losses, data_names):
        #     plt.plot(speeds, losses, label=label)
        # plt.xlabel("Speed (km/h)")
        # plt.ylabel("Loss (%)")
        # plt.title("Losses for all systems")
        # plt.legend()
        # plt.grid(True)
        # plt.tight_layout()
        # plt.savefig(f"{name}.png")
        # plt.show()
    
    
    def performance_values(self, all_losses: List[List[float]]) -> List[float]:
        if not all_losses:
            print("No loss data provided.")
            return []

        # proof that all list have the same length
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