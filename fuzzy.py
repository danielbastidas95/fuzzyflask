
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import csv

def calculate_obj1(value_ini_11, value_ini_12):

    #OBJETIVO 1: GARANTIZAR LA SOSTENEBILIDAD ECONOMICA DE LA ORGANIZACION
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Disminuir los pasivos a corto plazo
    # Inic2 = Incrementar los ingresos

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions


    Inic_1_1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Disminuir los pasivos...')
    Inic_1_2 = ctrl.Antecedent(np.arange(0, 110, 1), 'Incrementar los ingresos')
    Obj1 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 1')

    # Generate fuzzy membership functions
    Inic_1_1['Dmayor'] = fuzz.trapmf(Inic_1_1.universe, [-1, 0, 20, 29])
    Inic_1_1['Dmenor'] = fuzz.trimf(Inic_1_1.universe, [12, 40, 46])
    Inic_1_1['Fmenor'] = fuzz.trimf(Inic_1_1.universe, [36, 60, 72])
    Inic_1_1['Fmayor'] = fuzz.trapmf(Inic_1_1.universe, [76, 80, 110, 120])

    Inic_1_2['Dmayor'] = fuzz.trapmf(Inic_1_2.universe, [-1, 0, 20, 35])
    Inic_1_2['Dmenor'] = fuzz.trimf(Inic_1_2.universe, [37, 40, 56])
    Inic_1_2['Fmenor'] = fuzz.trimf(Inic_1_2.universe, [56, 60, 75])
    Inic_1_2['Fmayor'] = fuzz.trapmf(Inic_1_2.universe, [72, 80, 110, 120])

    Obj1['Dmayor'] = fuzz.trapmf(Obj1.universe, [-1, 0, 20, 35])
    Obj1['Dmenor'] = fuzz.trimf(Obj1.universe, [30, 40, 55])
    Obj1['Fmenor'] = fuzz.trimf(Obj1.universe, [50, 60, 76])
    Obj1['Fmayor'] = fuzz.trapmf(Obj1.universe, [60, 80, 110, 120])

    # generate rules
    rule_1_1 = ctrl.Rule(Inic_1_1['Dmenor'] | Inic_1_2['Fmenor'], Obj1['Fmenor'])
    rule_1_2 = ctrl.Rule(Inic_1_1['Fmayor'], Obj1['Fmenor'])
    rule_1_3 = ctrl.Rule(Inic_1_1['Fmayor'] & Inic_1_2['Fmayor'], Obj1['Fmayor'])

    #create system control and simulation
    solving_ctrl_obj1 = ctrl.ControlSystem([rule_1_1, rule_1_2, rule_1_3])
    solving_obj1 = ctrl.ControlSystemSimulation(solving_ctrl_obj1)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving_obj1.input['Disminuir los pasivos...'] = value_ini_11
    solving_obj1.input['Incrementar los ingresos'] = value_ini_12
    # Crunch the numbers
    solving_obj1.compute()
    
    #value objetivo 1
    Obj1_result = solving_obj1.output['Objetivo 1']

     #update data
    n = 1

    data = [['Objetivo', 'Valor'], 
        ['Objetivo 1', 0], 
        ['Objetivo 2', 0],
        ['Objetivo 3', 0],
        ['Objetivo 4', 0],
        ['Objetivo 5', 0],
        ['Objetivo 6', 0],
        ['Objetivo 7', 0]]
 
    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
             
    data[1][1] = Obj1_result
 
 
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    csvFile.close()

def calculate_obj2(value_ini_21, value_ini_22, value_ini_23):

    #OBJETIVO 2: Crear experiencias gratamente memorables para posicionar la marca EMTEL en el corazón de los clientes
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Crear cultura basada en la experiencia
    # Inic2 = Alcanzar los tiempos promedio de instalacion y reparación requeridos
    # Inic3 = Garantizar los niveles de calidad establecidos en la prestación de los servicios TIC

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic1')
    Inic2 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic2')
    Inic3 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic3')
    Obj2 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 2')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 29])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [30, 40, 55])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [44, 60, 78])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [76, 80, 110, 120])

    Inic2['Dmayor'] = fuzz.trapmf(Inic2.universe, [-1, 0, 20, 29])
    Inic2['Dmenor'] = fuzz.trimf(Inic2.universe, [32, 40, 58])
    Inic2['Fmenor'] = fuzz.trimf(Inic2.universe, [36, 60, 69])
    Inic2['Fmayor'] = fuzz.trapmf(Inic2.universe, [75, 80, 110, 120])

    Inic3['Dmayor'] = fuzz.trapmf(Inic3.universe, [-1, 0, 20, 22])
    Inic3['Dmenor'] = fuzz.trimf(Inic3.universe, [31, 40, 55])
    Inic3['Fmenor'] = fuzz.trimf(Inic3.universe, [44, 60, 77])
    Inic3['Fmayor'] = fuzz.trapmf(Inic3.universe, [72, 80, 110, 120])

    Obj2['Dmayor'] = fuzz.trapmf(Obj2.universe, [-1, 0, 20, 35])
    Obj2['Dmenor'] = fuzz.trimf(Obj2.universe, [30, 40, 55])
    Obj2['Fmenor'] = fuzz.trimf(Obj2.universe, [50, 60, 76])
    Obj2['Fmayor'] = fuzz.trapmf(Obj2.universe, [60, 80, 110, 120])

    #generate rules membreship
    rule1 = ctrl.Rule(Inic1['Dmenor'] | Inic2['Fmenor'], Obj2['Fmenor'])
    rule2 = ctrl.Rule(Inic1['Fmayor'], Obj2['Fmenor'])
    rule3 = ctrl.Rule(Inic1['Fmayor'] & Inic2['Fmayor'], Obj2['Fmayor'])
    rule4 = ctrl.Rule(Inic1['Fmenor'] & Inic3['Fmenor'], Obj2['Fmenor'])
    rule5 = ctrl.Rule(Inic3['Fmayor'] | Inic2['Fmayor'] | Inic1['Fmayor'], Obj2['Fmenor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Inic1'] = value_ini_21
    solving.input['Inic2'] = value_ini_22
    solving.input['Inic3'] = value_ini_23
    # Crunch the numbers
    solving.compute()

    #value objetivo 2
    Obj2_result = solving.output['Objetivo 2']

    #update data
    n = 1
    data = [['Objetivo', 'Valor'], 
    ['Objetivo 1', 0], 
    ['Objetivo 2', 0],
    ['Objetivo 3', 0],
    ['Objetivo 4', 0],
    ['Objetivo 5', 0],
    ['Objetivo 6', 0],
    ['Objetivo 7', 0]]

    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
     
    #update table 
    data[2][1] = Obj2_result
    
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    csvFile.close()

def calculate_obj3(value_ini_31):
    #OBJETIVO 3: INCURSIONAR EN NUEVAS OPORTUNIDADES DE NEGOCIO
    # Generate universe variables
    #   El rango de las iniciativas estrategicas es [0,110]
    #   El rango del objetivo de salida es [0,110]
    # Inic1 = Generar nuevas oportunidades de negocio

    # New Antecedent/Consequent objects hold universe variables and membership
    # functions
    Inic1 = ctrl.Antecedent(np.arange(0, 110, 1), 'Inic1')
    Obj3 = ctrl.Consequent(np.arange(0, 110, 1), 'Objetivo 3')

    # Generate fuzzy membership functions
    Inic1['Dmayor'] = fuzz.trapmf(Inic1.universe, [-1, 0, 20, 26])
    Inic1['Dmenor'] = fuzz.trimf(Inic1.universe, [21, 40, 57])
    Inic1['Fmenor'] = fuzz.trimf(Inic1.universe, [55, 60, 79])
    Inic1['Fmayor'] = fuzz.trapmf(Inic1.universe, [72, 80, 110, 120])

    Obj3['Dmayor'] = fuzz.trapmf(Obj3.universe, [-1, 0, 20, 35])
    Obj3['Dmenor'] = fuzz.trimf(Obj3.universe, [30, 40, 55])
    Obj3['Fmenor'] = fuzz.trimf(Obj3.universe, [50, 60, 76])
    Obj3['Fmayor'] = fuzz.trapmf(Obj3.universe, [60, 80, 110, 120])

    #generate rules membreship
    rule1 = ctrl.Rule(Inic1['Dmayor'], Obj3['Dmayor'])
    rule2 = ctrl.Rule(Inic1['Dmenor'], Obj3['Dmenor'])
    rule3 = ctrl.Rule(Inic1['Fmenor'], Obj3['Fmenor'])
    rule4 = ctrl.Rule(Inic1['Fmayor'], Obj3['Fmayor'])

    #create system control and simulation
    solving_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    solving = ctrl.ControlSystemSimulation(solving_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
    solving.input['Inic1'] = value_ini_31
    # Crunch the numbers
    solving.compute()

    #value objetivo 3
    Obj3_result = solving.output['Objetivo 3']

    #update data
    n = 1
    data = [['Objetivo', 'Valor'], 
    ['Objetivo 1', 0], 
    ['Objetivo 2', 0],
    ['Objetivo 3', 0],
    ['Objetivo 4', 0],
    ['Objetivo 5', 0],
    ['Objetivo 6', 0],
    ['Objetivo 7', 0]]

    with open('static/data/datamain.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[n] = ['Objetivo', row['Valor']]
            n=n+1
     
    #update table 
    data[3][1] = Obj3_result
    
    with open('static/data/datamain.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    csvFile.close()


