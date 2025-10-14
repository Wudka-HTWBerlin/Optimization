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


class Calculation:
    def __init__(self):
        self.time_loses: List[float] = []
        self.P_reduction: List[float] = []

    def time_los_calc(self, v_min: int, v_max: int,  drive_distance: float, ) -> List[float]:
        
        time_los = []
        v_max_avg= -0.0088853 * v_max ** 2 + 2.66526 * v_max - 77.2296
        v_min_avg= -0.0088853 * v_min ** 2 + 2.66526 * v_min - 77.2296
        t_min = drive_distance / v_max_avg
        for v in range(v_min, v_max + 1):
            
            v_avarage = v #stammt aus paper zur durchschnittsgeschwindigkeit auf Autobahnen je nach Geschwindigkeit
            # print(f"speed:{v}, speed avarage {v_avarage} ")
            if v_avarage == 0:
                time_los.append(0.0)
                continue
            time_avg = drive_distance / v_avarage
            time_red = 1-time_avg /t_min
            time_los.append(time_red)
        # print(f"length of time {len(time_los)}")
        return time_los

    def P_reduction_calc(self, PL: List[float], PR: List[float]) -> List[float]:
        P=[]
        if len(PL) != len(PR):
            # print("Size of PL and PR are differing")
            # print(f"PL_size = {len(PL)}")
            # print(f"PR_size = {len(PR)}")
            return [0.0]
        
        for pl, pr in zip(PL, PR):
            P.append(pl + pr)
        P_max = max(P)
        P.remove(P_max)

        if P_max == 0:
            return [0.0 for _ in P]

        P_reduction = [1 - p / P_max for p in P]
        return P_reduction