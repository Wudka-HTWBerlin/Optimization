import math
def constraints( drones,total_length, water, speed):
        
        cell_length= 100 #m
        min_water_per_sqrM=1.3 #l/m^2 
        drop_time=4.5 #seconds
        max_circle_time = 600 #seconds
        speed_ms= speed/3.6
        
        min_circle_speed = total_length/(max_circle_time-30)

        circle_time = round(total_length/speed_ms + 30)

        if circle_time <= max_circle_time:
            print(f"A circle time of {circle_time} seconds is enough to reach the destination in time")
            circle_speed =speed

        else:
            print(f"A {circle_time} of is not enough to reach the destination in time")
            print (f"To reach destination in time a minimum speed of {min_circle_speed} m/s has to be set")
            circle_speed=min_circle_speed * 3.6

        # calculating water spreat at defined circle speed
        length= drop_time * speed_ms
        A_elipse= length/2 * 4/2* math.pi
        water_per_sqrm= water / A_elipse

        n_dr_length = round(cell_length/length)
        n_drones = round(min_water_per_sqrM/water_per_sqrm) * n_dr_length
        # wpsqrm_ndrones= n_drones*water_per_sqrm
        
        if drones < n_drones:
            print(f"{drones} drones aren´t enough to extinguish a fire in a length of {cell_length} meter")
            drones_inex=n_drones-drones
            print(f"Theirfore {drones_inex} drones have to be included into the fleet")
            
        elif drones > n_drones:
            print(f"{drones} drones are more then needed to extinguish a fire in a length of {cell_length} meter")
            drones_inex= n_drones - drones
            print(f"{abs(drones_inex)} drones can be excluded")

        
        elif drones == n_drones:
            print(f"{drones} drones are enough to extinguish a fire in a length of {cell_length} meter")
            drones_inex = 0
        

        return   circle_speed, drones_inex