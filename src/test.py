import math
import numpy as np

g_c_old = 1501

green_cells = 1500

burning_cells = 291
bc_old = 300


gradient = (green_cells - g_c_old)/10
rad = math.atan(gradient)
    
reward_gc= math.cos(rad)

if gradient == 0.0:
    gradient_bc = (bc_old-burning_cells)/10 
    rad_bc = math.atan(gradient_bc)
    reward_bc=  math.sin(rad_bc)
else:
    reward_bc=0

# print("action reward: ", action_reward)
#action_reward=(len(self.burned_cells_old)-len(burned_cells))/self.grid_size**2
action_reward = reward_gc + reward_bc
    
print("result: ",action_reward)





# zellen = alte_zellen-neue_zellen

# steigung = (neue_zellen -alte_zellen)/10

# print("steigung: ", steigung)
# winkel_rad = math.atan(steigung)
# winkel = math.degrees(winkel_rad)
# rad = math.radians(winkel+90)
# print("Winkel: ", winkel+90)
# result = math.sin(winkel_rad)
# # if zellen > 0:

# #     result = math.cos(winkel_rad)
    
# # elif zellen <= 0:
# #     result = -math.sin(rad)

# print("result: ",result)


