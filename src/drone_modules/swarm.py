import math
import numpy as np
from typing import List

class Optimization:
    def __init__(self):
        self.Achieve: List[float] = []
        self.losses: List[float] = []

    def Achievment(self, P_opt, t_opt, P_weight: int, t_weight: int):
        # if len(P_opt) != len(t_opt):
        #     print("Size of Optimization factors are differing")
        #     print(f"Opt_fact1 = {len(P_opt)}")
        #     print(f"Opt_fact2 = {len(t_opt)}")
        #     return [0.0]
        
        gen_weight = max(P_weight, t_weight)
        Calc_result = []



        
        t = t_weight * np.array(t_opt)/ gen_weight 
        t_new= t[:,np.newaxis] # change to row vector
        P= P_weight* P_opt / gen_weight

        value = P+t_new 
        Calc_result.append(value)

        return Calc_result

    def Optimization_losses(self, Achievemnt_system):
        max_value = np.max(Achievemnt_system)
        losses = [max_value - val for val in Achievemnt_system]
        return losses