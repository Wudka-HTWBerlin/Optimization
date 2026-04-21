import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter

class DroneCoopMath:
    def __init__(self, plot_2D, plot_3D):
        self.plot_2D = plot_2D
        self.plot_3D= plot_3D
        
    def file_output(self, all_data, name: str, data_names):
     
        fig1 = plt.figure(figsize=(12, 10))
        
        ax = fig1.add_subplot(111, projection='3d')
        for data in  all_data:
            
            y_coords_ = np.arange(data.shape[0])
            x_coords_ = np.arange(data.shape[1])
            X_, Z_ = np.meshgrid(x_coords_ + 20 , y_coords_)

            

            surf = ax.plot_surface(Z_, X_, data, 
                       cmap='viridis', 
                       rstride=1, cstride=1, 
                       antialiased=False)
            
            # fig1.colorbar(surf, shrink=0.6, aspect=20, label='Y-Wert')
        ax.set_xlabel('speed [km/h]')
        ax.set_zlabel('objective value')
        ax.set_ylabel('mass [km/h]')
        ax.set_title(f'{name}')
        if self.plot_2D:
            plt.show()

    def plot_data_3D(self, data, name: str, data_names):
        fig1 = plt.figure(figsize=(12, 10))
        
        ax = fig1.add_subplot(111, projection='3d')
        
            
        y_coords_ = np.arange(data.shape[0])
        x_coords_ = np.arange(data.shape[1])
        X_, Z_ = np.meshgrid(x_coords_ +20 , y_coords_+20)

        surf = ax.plot_surface(Z_, X_, data, 
                    cmap='viridis', 
                    rstride=1, cstride=1, 
                    antialiased=False)
        
        # fig1.colorbar(surf, shrink=0.6, aspect=20, label='Y-Wert')
        ax.set_xlabel('speed [km/h]')
        ax.set_zlabel('Optimization value')
        ax.set_ylabel('water mass [kg]')
        ax.set_title(data_names)
        plt.savefig(f"{data_names}.png")

        if self.plot_3D:
            plt.show()
            
     
    def turning_point(self,function):
        A_smooth = gaussian_filter(function, sigma=1.0)  
        # DroneCoopMath.file_output(self, [A_smooth, function], "LossesAll", "gaussian loss")

        Ay, Ax = np.gradient(A_smooth)    
        Ayy, _ = np.gradient(Ay)
        Axy, Axx = np.gradient(Ax)

        Laplacian = Axx + Ayy
        min_laplace_index = np.argmin(np.abs(Laplacian))
        min_row_laplace, min_col_laplace = np.unravel_index(min_laplace_index, Laplacian.shape)
        min_laplace_wert = Laplacian[min_row_laplace, min_col_laplace]
        # print("--- Basierend auf dem Laplace-Operator ---")
        # print(f"Minimal gekrümmter Ort (Laplacian ≈ 0) bei: ({min_row_laplace}, {min_col_laplace})")
        # print(f"Laplacian-Wert dort: {min_laplace_wert:.4f}")
        max_laplace_index =np.argmax(np.abs(Laplacian))
        max_row_laplace, max_col_laplace = np.unravel_index(max_laplace_index, Laplacian.shape)
        max_laplace_wert = Laplacian[max_row_laplace, max_col_laplace]
        # print("--- Basierend auf dem Laplace-Operator ---")
        # print(f"Maximal gekrümmter Ort (Laplacian ≈ 0) bei: ({max_row_laplace}, {max_col_laplace})")
        # print(f"Laplacian-Wert dort: {max_laplace_wert:.4f}")
        
        # tolerance = 0.05
        # turning_points = np.where(np.abs(Laplacian) < tolerance)      
        # print(f"Anzahl Laplace-Nulldurchgang Kandidaten: {len(turning_points[0])}")

        return min_row_laplace, min_col_laplace

    def plot_data_2D(self,data_names, data, title):
       
        
        for twoDarray, label in zip(data, data_names):
            i= 0
            j= 0
            for oneDarrray in twoDarray:
                mass = np.arange(20, len(oneDarrray)+20)
                i+=1
                labeli=label+"_"+str(i) 
                
                plt.plot(mass,oneDarrray, label=labeli)
            plt.xlabel("mass kg")
            plt.ylabel("achive (%)")
            plt.title(title)
            plt.legend()
            plt.grid(True)
            # plt.tight_layout()
            plt.savefig(f"mass_achive.png")
            i+=1
            if self.plot_2D:
                plt.show()


            for i in range(twoDarray.shape[1]):  # Wir iterieren über die Anzahl der Spalten
                column_data = twoDarray[:, i]     # Zugriff auf die i-te Spalte
                speed = np.arange(20, len(column_data) + 20)
                labeli=label+"_"+str(j) 
                j=+1

                plt.plot(speed,column_data, label=labeli)
            plt.xlabel("speed m/s")
            plt.ylabel("optimization value")
            plt.title(title)
            # plt.legend()
            plt.grid(True)
            # plt.tight_layout()
            plt.savefig(f"optimization_3d.png")
            if self.plot_2D:
                plt.show()

    def plot_data_2D_from_2d(self,data_names, data, threeD_list, title):
        if threeD_list:
            for twoDarray, label in zip(data, data_names):
                
                size= np.size(twoDarray)
                x = np.arange(20, size+20)
                plt.plot(x,twoDarray, label=label)

        else:         
            x = np.arange(20, len(data)+20)

            labeli="data"
            
            plt.plot(x, data, label=labeli)
        plt.xlabel("mass kg")
        plt.ylabel("achive (%)")
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{data_names}.png")
        if self.plot_2D:
            plt.show()


    def sum_array(self, all_data):
        if not all_data:
            print("No loss data provided.")
            return []
        sum_array=np.array(all_data)
        _sum=np.sum(sum_array, axis=0)

        # performance_vector = []
        # for losses in all_losses:  # Transponiert -> [(l1_1, l2_1, ..., ln_1), ..., (l1_n, ..., ln_n)]
            

        return _sum