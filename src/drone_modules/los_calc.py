from typing import List
import numpy as np

class DroneCalculation:
    def __init__(self):
        self.time_loses: List[float] = []
        self.P_reduction: List[float] = []

    def time_los_calc(self, v_min: int, v_max: int,  drive_distance: float, ) -> List[float]:
        
        time_los = []
        t_min = drive_distance / v_max
        
        for v in range(v_min, v_max):
            
            v_avarage = v 
            if v_avarage == 0:
                time_los.append(0.0)
                continue
            time_avg = drive_distance / v_avarage
            time_red = 1-time_avg /t_min
            time_los.append(time_red)
        # print(f"length of time {len(time_los)}")
        return time_los

    def P_reduction_calc(self, Ph: List[float], Pv: List[float]) -> List[float]:
        P=[]
        # if len(Ph) != len(Pv):
        #     print("Size of PL and PR are differing")
        #     print(f"Ph_size = {len(Ph)}")
        #     print(f"Pv_size = {len(Pv)}")
        #     return [0.0]
        for pv in Pv:
            new_line = []
            for ph in Ph:
                sum = pv + ph
                new_line.append(sum)
            P.append(new_line)
        
        # for ph, pv in zip(Ph, Pv):
        #     P.append(ph + pv)
        P_max = max(P)
        P.remove(P_max)

        if P_max == 0:
            return [0.0 for _ in P]
        P_reduction =1 - (np.array(P)/ P_max )
        # P_reduction =[ [1 - p / P_max for p in row] for row in P]
        return P_reduction