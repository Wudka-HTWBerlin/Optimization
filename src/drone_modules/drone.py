import math

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
                  ):
       
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
        self.water_max = 60 # l
        self.drop_time = 35/4.5 # sec

           #wind direction in degrees
        # self.p_eff= power_efficency 
        
        self.V_shape = True
        self.A_bl= self.R_bl**2 *math.pi 
        
        if follow:
            if self.V_shape:
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
        c_d=1   
        for v_t in range(self.v_min, self.v_max+1):
            v_f= v_t/3.6
            if self.follow and not self.V_shape:
                distance = v_f * self.r_t
                c_d= (0.11661 * math.log(33.992 * distance + 93.9171) - 0.0795772) * self.c_d 
 
            v= v_f+v_w    
            P_constant= 0.5 * self.rho * self.A_drone * c_d * v_f**2

            P_vertical = P_constant * v_f/ self.sigma

            P_wind = (P_constant * (math.sin(phi/2)**3) * v_w)
            
            P_Vertical = (P_vertical - P_wind)

            P_vert.append(P_Vertical)

        return P_vert

    def P_hover(self, ) :
        P_h = []
        n=4 # number of blades / rotors
        
        for water in range (self.water_min, self.water_max):       
            F_g = (water+self.mass) * self.g
            p_bl = F_g**(3/2)/(math.sqrt(n*self.rho*self.A_bl) )*self.C_T**(-3/2) *self.delta/8 * self.s_bl  
            p_in = (1+self.k)*(F_g**(3/2)/(math.sqrt(2*self.rho*self.A_bl)))
            P_h.append(p_bl+p_in)
            # self.P_bl.append(p_bl)
            # self.P_in.append(p_in)

        return P_h
    
            
