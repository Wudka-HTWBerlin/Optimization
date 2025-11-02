from typing import List

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

    def P_reduction_calc(self, Ph: List[float], Pv: List[float]) -> List[float]:
        P=[]
        if len(Ph) != len(Pv):
            # print("Size of PL and PR are differing")
            # print(f"PL_size = {len(PL)}")
            # print(f"PR_size = {len(PR)}")
            return [0.0]
        
        for ph, pv in zip(Ph, Pv):
            P.append(ph + pv)
        P_max = max(P)
        P.remove(P_max)

        if P_max == 0:
            return [0.0 for _ in P]

        P_reduction = [1 - p / P_max for p in P]
        return P_reduction