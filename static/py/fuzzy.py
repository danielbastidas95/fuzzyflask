
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import csv

def fuzzy_system(value_ini_11, value_ini_12)

    #OBJETIVO 1: GARANTIZAR LA SOSTENEBILIDAD ECONOMICA DE LA ORGANIZACION
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Disminuir los pasivos a corto plazo
    # Inic2 = Incrementar los ingresos

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions


    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Disminuir los pasivos...')
    Inic2 = ctrl.Antecedent(np.arange(0, 110, 1), 'Incrementar los ingresos')
    Obj1 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 1')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 29])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [12, 40, 46])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [36, 60, 72])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [76, 80, 110, 120])

    Inic2['Dmayor'] = fuzz.trapmf(Inic2.universe, [-1, 0, 20, 35])
    Inic2['Dmenor'] = fuzz.trimf(Inic2.universe, [37, 40, 56])
    Inic2['Fmenor'] = fuzz.trimf(Inic2.universe, [56, 60, 75])
    Inic2['Fmayor'] = fuzz.trapmf(Inic2.universe, [72, 80, 110, 120])

    Obj1['Dmayor'] = fuzz.trapmf(Obj1.universe, [-1, 0, 20, 35])
    Obj1['Dmenor'] = fuzz.trimf(Obj1.universe, [30, 40, 55])
    Obj1['Fmenor'] = fuzz.trimf(Obj1.universe, [50, 60, 76])
    Obj1['Fmayor'] = fuzz.trapmf(Obj1.universe, [60, 80, 110, 120])

    # generate rules
    rule1 = ctrl.Rule(Inic1['Dmenor'] | Inic2['Fmenor'], Obj1['Fmenor'])
    rule2 = ctrl.Rule(Inic1['Fmayor'], Obj1['Fmenor'])
    rule3 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmayor'], Obj1['Fmayor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Disminuir los pasivos...'] = 50
    solving.input['Incrementar los ingresos'] = 60
    # Crunch the numbers
    solving.compute()

    Obj1_result = solving.output['Objetivo 1']

    Obj2_result = 80
    Obj3_result = 80
    Obj4_result = 80
    Obj5_result = 80
    Obj6_result = 80
    Obj7_result = 80


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

    return Obj1_result


