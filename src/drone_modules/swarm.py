import math
from typing import List

class Optimization:
    def __init__(self):
        self.Achieve: List[float] = []
        self.losses: List[float] = []

    def Achievment(self, P_opt: List[float], t_opt: List[float], P_weight: int, t_weight: int) -> List[float]:
        if len(P_opt) != len(t_opt):
            # print("Size of Optimization factors are differing")
            # print(f"Opt_fact1 = {len(Opt_fact1)}")
            # print(f"Opt_fact2 = {len(Opt_fact2)}")
            return [0.0]
        
        gen_weight = max(P_weight, t_weight)
        Calc_result = []

        for P, t in zip(P_opt, t_opt):
            value = P_weight* P / gen_weight + t_weight * t/ gen_weight 
            Calc_result.append(value)

        return Calc_result

    def Optimization_losses(self, Achievemnt_system: List[float]) -> List[float]:
        max_value = max(Achievemnt_system)
        losses = [max_value - val for val in Achievemnt_system]
        return losses