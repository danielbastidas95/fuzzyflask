import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import csv

#OBJETIVO 1: GARANTIZAR LA SOSTENEBILIDAD ECONOMICA DE LA ORGANIZACION
# Generate universe variables
#   El rango de las iniciativas estrategicas es [0,10]
#   El rango del objetivo de salida es [0,10]
# Inic1 = Disminuir los pasivos a corto plazo
# Inic2 = Disminuir los pasivos a corto plazo

#universe
Inic1 = np.arange(0, 11, 1)
Inic2 = np.arange(0, 11, 1)
Obj1  = np.arange(0, 11, 1)

# Generate fuzzy membership functions
Inic1_Dmayor = fuzz.trapmf(Inic1, [-1, 0, 3, 5])
Inic1_Dmenor = fuzz.trapmf(Inic1, [3, 4, 5, 6])
Inic1_Fmenor = fuzz.trapmf(Inic1, [4, 6, 7, 8])
Inic1_Fmayor = fuzz.trapmf(Inic1, [7, 8, 11, 12])
Inic2_Dmayor = fuzz.trapmf(Inic2, [-1, 0, 2, 4])
Inic2_Dmenor = fuzz.trapmf(Inic2, [2, 2, 4, 6])
Inic2_Fmenor = fuzz.trapmf(Inic2, [5, 6, 7, 8])
Inic2_Fmayor = fuzz.trapmf(Inic2, [6, 8, 10, 11])
Obj1_Dmayor = fuzz.trapmf(Obj1, [-1, 0, 2, 3])
Obj1_Dmenor = fuzz.trapmf(Obj1, [1, 2, 4, 5])
Obj1_Fmenor = fuzz.trapmf(Obj1, [4, 6, 7, 8])
Obj1_Fmayor = fuzz.trapmf(Obj1, [7, 8, 10, 11])

# We need the activation of our fuzzy membership functions at these values.
# The exact values 6.5 and 9.8 do not exist on our universes...
# This is what fuzz.interp_membership exists for!
Inic1_level_Dmayor = fuzz.interp_membership(Inic1, Inic1_Dmayor, 6.5)
Inic1_level_Dmenor = fuzz.interp_membership(Inic1, Inic1_Dmenor, 6.5)
Inic1_level_Fmenor = fuzz.interp_membership(Inic1, Inic1_Fmenor, 6.5)
Inic1_level_Fmayor = fuzz.interp_membership(Inic1, Inic1_Fmayor, 6.5)

Inic2_level_Dmayor = fuzz.interp_membership(Inic2, Inic2_Dmayor, 9.8)
Inic2_level_Dmenor = fuzz.interp_membership(Inic2, Inic2_Dmenor, 9.8)
Inic2_level_Fmenor = fuzz.interp_membership(Inic2, Inic2_Fmenor, 9.8)
Inic2_level_Fmayor = fuzz.interp_membership(Inic2, Inic2_Fmayor, 9.8)

# Now we take our rules and apply them. Rule 1 concerns Dmayor Inic1 OR Dmayor Inic2
# The OR operator means we take the maximum of these two.
active_rule1 = np.fmax(Inic1_level_Dmayor, Inic2_level_Dmayor)

# Now we apply this by clipping the top off the corresponding output
# membership function with `np.fmin`
Obj1_activation_Dmayor = np.fmin(active_rule1, Obj1_Dmayor)  # removed entirely to 0

# For rule 2 we connect acceptable service to medium tipping
Obj1_activation_Dmenor = np.fmin(Inic2_level_Dmenor, Obj1_Dmenor)

# For rule 3 we connect high service OR high food with high tipping
active_rule3 = np.fmax(Inic1_level_Fmenor, Inic2_level_Fmenor)
Obj1_activation_Fmenor = np.fmin(active_rule3, Obj1_Fmenor)

# Now we take our rules and apply them. Rule 1 concerns Fmayor Inic1 OR Fmayor Inic2
# The OR operator means we take the maximum of these two.
active_rule4 = np.fmax(Inic1_level_Fmayor, Inic2_level_Fmayor)
Obj1_activation_Fmayor = np.fmin(active_rule4, Obj1_Fmayor)

# Aggregate all three output membership functions together
aggregated = np.fmax(Obj1_activation_Dmayor,
                     np.fmax(Obj1_activation_Dmenor, 
                             np.fmax(Obj1_activation_Fmenor, Obj1_activation_Fmayor)))

# Calculate defuzzified result
Obj1_result = fuzz.defuzz(Obj1, aggregated, 'centroid')
Obj1_result = Obj1_result*10

Obj2_result = 80
Obj3_result = 75
Obj4_result = 90
Obj5_result = 85
Obj6_result = 92
Obj7_result = 89


#create and write csv file
csvData = [['Objetivo', 'Valor'], 
            ['Objetivo 1', Obj1_result], 
            ['Objetivo 2', Obj2_result],
            ['Objetivo 3', Obj3_result],
            ['Objetivo 4', Obj4_result],
            ['Objetivo 5', Obj5_result],
            ['Objetivo 6', Obj6_result],
            ['Objetivo 7', Obj7_result]]

with open('../data/datamain.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()



