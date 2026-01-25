from typing import List
import numpy as np
import math

class DroneCalculation:
    def __init__(self):
        self.time_loses: List[float] = []
        self.P_reduction: List[float] = []

    def time_los_calc(self, v_min: int, v_max: int,  drive_distance: float, ) -> List[float]:
        
        time_los = []
        t_min = drive_distance / v_max
        t_max = drive_distance / v_min
        for v in range(v_min, v_max):
            if v == 0:
                time_los.append(0.0)
                continue
            time_avg = drive_distance / v
            time_red = time_avg/t_min  
           
            time_los.append(time_red)
        # print(f"length of time {len(time_los)}")
        return time_los

    def P_reduction_calc(self, Ph: List[float], Pv: List[float]) -> List[float]:
        P=[]
        for pv in Pv:
            new_line = []
            for ph in Ph:
                sum = pv + ph
                new_line.append(sum)
            P.append(new_line)
        
        P_max = np.min(P)
        
        P_max_row = max(P)
        P.remove(P_max_row)

        if P_max == 0:
            return [0.0 for _ in P]
        P_reduction =np.array(P)/ P_max
        # P_reduction =[ [1 - p / P_max for p in row] for row in P]
        return P_reduction
    
    