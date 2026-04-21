import numpy as np
# def exclude_systems(number_of_sys,comparative_data, row, coloumn):
#     ex_index=[]
#     data_array = np.array(comparative_data)
#     values = data_array[:, row, coloumn]
    
#     # Get the indices that would sort these values
#     sorted_indices = np.argsort(values)[::-1]
    
#     for exclude in range(number_of_sys):
#         ex_index.append(sorted_indices[exclude])
#     # print(f"The follwing drones with the system number {ex_index} can be removed form the fleet ")
#     print("Excluded System Indices:", end=" ")
#     print(*ex_index, sep=", ")
    
#     return ex_index

#     # exclude systems with highest loss form buttom to top
def exclude_systems(number_of_sys, comparative_data, row, coloumn):
    ex_index = []
    data_array = np.array(comparative_data)
    values = data_array[1:, row , coloumn]
    sorted_indices = np.argsort(values)[::-1]
    
    sorted_indices = sorted_indices + 1
    
    for exclude in range(number_of_sys):
        ex_index.append(sorted_indices[exclude])
    
    print("Excluded System Indices:", end=" ")
    print(*ex_index, sep=", ")
    
    return ex_index