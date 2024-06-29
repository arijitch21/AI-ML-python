import pandas as pd

def calculate_expance(exp):
    """
    This function took two argument
    and calculate the total
    """
    total = 0
    for item in exp:
        total = total + item
    return total;


toms_expence_list = [5,9,11,20]
joes_expance_list = [7,12,15,25]

toms_total_expence = calculate_expance(toms_expence_list)
joes_total_expance = calculate_expance(joes_expance_list)

print("Toms total expence: ",toms_total_expence)
print("Joes total expence: ",joes_total_expance)