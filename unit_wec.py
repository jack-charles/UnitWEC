"""
@author: Jack Charles   jack@jackcharlesconsulting.com
"""






import math
import json

class UnitSystemClass():
    def __init__(self, name, angle, area, capacity, concentration, density_g, density_l, density_s, 
                 diameter, force, length, linear_mass, mass, mass_rate, permeability, pressure, 
                 pressure_gradient, temperature, velocity, volume, volumeteric_rate): 
        self.name = name
        self.angle = angle
        self.area = area
        self.capacity = capacity
        self.concentration = concentration
        self.density_g = density_g
        self.density_l = density_l
        self.density_s = density_s
        self.diameter = diameter
        self.force = force
        self.length = length
        self.linear_mass = linear_mass
        self.mass = mass
        self.mass_rate = mass_rate
        self.permeability = permeability
        self.pressure = pressure
        self.pressure_gradient = pressure_gradient
        self.temperature = temperature
        self.velocity = velocity
        self.volume = volume
        self.volumetric_rate = volumeteric_rate

def import_units_json(data_filename):
    with open(data_filename, 'r',) as file:
        json_data = json.load(file)
    #unit_class = UnitSystemClass(**json_data)      #this would work if the class names were identical to the dictionary
    unit_class = UnitSystemClass(json_data["Unit System Name"], json_data["Angle"], json_data["Area"], json_data["Capacity"],
                                 json_data["Concentration"], json_data["Gas Density"], json_data["Liquid Density"], json_data["Solid Density"], 
                                 json_data["Diameter"], json_data["Force"], json_data["Length"], json_data["Linear Mass"], json_data["Mass"],
                                 json_data["Mass Rate"], json_data["Permeability"], json_data["Pressure"], json_data["Pressure Gradient"], 
                                 json_data["Temperature"], json_data["Velocity"], json_data["Volume"], json_data["Volumetric Rate"])
    return unit_class

def export_units_json(unit_class, data_filename):
    json_data = {"Unit System Name": unit_class.name, "Angle": unit_class.angle, "Area": unit_class.area, "Capacity": unit_class.capacity,
                 "Concentration": unit_class.concentration, "Gas Density": unit_class.density_g, "Liquid Density": unit_class.density_l, "Solid Density": unit_class.density_s, 
                 "Diameter": unit_class.diameter, "Force": unit_class.force, "Length": unit_class.length, "Linear Mass": unit_class.linear_mass, "Mass": unit_class.mass,
                 "Mass Rate": unit_class.mass_rate, "Permeability": unit_class.permeability, "Pressure": unit_class.pressure, "Pressure Gradient": unit_class.pressure_gradient, 
                 "Temperature": unit_class.temperature, "Velocity": unit_class.velocity, "Volume": unit_class.volume, "Volumetric Rate": unit_class.volumetric_rate}
    
    with open(data_filename, 'w',) as file:
        json.dump(json_data, file)
    return

def write_sieve_data_json(unit, datalist, data_filename = 'sanddata.json'):
    datadictionary = {}
    srtdictionary = {}
    datadictionary['Sieve Units'] = unit
    for i in range(len(datalist)):
        srtdictionary["Sample "+str(i)] = {'Name':datalist[i].name, 'Depth':datalist[i].depth, 'Sieve Sizes':datalist[i].sieve_sizes, 
                                            'Retained Weight':datalist[i].retained,                                           
                                            }
    with open(data_filename, 'w',) as file:
        json.dump(datadictionary, file)
    return

def convert(value, x_unit, y_unit):   #value, original unit, new unit
    #converts input unit to the top (usually SI) unit in each category, and will convert output unit from SI unit to output unit
    #when units are inverted (1/x) simply switch x_unit and y_unit when calling function
    x = value   #avoids function accidentally changing the variable in other parts of the program

    #Multiplying variable by key-value to convert units to internal SI system. Inverse of dictionary will be used to convert back     
    unit_dictionary = {
        #Angle
        'degree': x,
        'radian': x / math.pi * 180,
        #Area
        'ft2': x,
        'in2': x / 144,
        'acre': x * 43560,
        #Capacity
        'm3/m': x,
        'l/m': x / 1000,
        'bbl/ft': x * 0.5216,
        'bbl/m': x * 0.159,
        'gal/ft': x * 0.0124,
        'gal/m': x * 0.0038,
        'liter/m': x / 1000,
        #Concentration
        'pptg': x,
        'gpml': x / 0.0001198,
        #Density
        'liquid sg': x,
        'sg': x,
        #'gas sg': x,
        'ppg': x / 8.345,
        'ppga': x / 8.345,
        'API': 141.5 / (x + 131.5),
        'kg/m3': x / 1000,
        'lb/gal': x / 8.345,
        'lbs/gal': x / 8.345,
        'lb/ft3': x / 62.39431984,
        #Force
        'N': x,
        'kN': x * 1000,
        'lbf': x * 4.448,
        'klbf': x * 4.448 * 1000,
        #Length
        'm': x,
        'cm': x / 100,
        'mm': x / 1000,
        'ft': x * 0.3048,
        'in': x / 12 * 0.3048,
        'inch': x / 12 * 0.3048,
        'inches': x / 12 * 0.3048,
        #Linear mass
        'kg/m': x,
        'lbm/ft': x * 1.488,
        #Mass
        'kg': x,
        'g': x / 1000,
        'lbm': x / 2.205,
        'oz': x / 2.205 / 16,
        #Permeability
        'D': x,
        'mD': x / 1000,
        'md': x / 1000,
        #Pressure
        'kPa': x,
        'MPa': x * 1000,
        'psi': x / 0.145037744,
        'bar': x * 100,
        #Pressure Gradient
        'kPa/m': x,
        'psi/ft': x / 0.145037744 * 0.3048,
        'ppg_ECD': x * 1.1751,
        #Temperature
        'C': x,
        'K': x - 273,
        'F': (x - 32) * 5 / 9,
        'R': (x - 459.67 - 32) * 5 / 9,
        'deg C': x,
        'deg F': (x - 32) * 5 / 9,
        #Velocity
        'm/s': x,
        'ft/s': x * 0.3048,
        #Viscosity
        'cP': x,
        'poise': x * 100,
        'lbm/ft-s': x * 1488.1639,
        'lbf-s/ft2': x * 47880.259,
        'Pa-s': x * 1000,
        #Volume
        'm3': x,
        'bbl': x * 0.1589698,
        'ft3': x * 0.3048 ** 3,
        'stb': x * 0.1589698,
        'scf': x * 0.3048 ** 3,
        'Mscf': x * 0.3048 ** 3 * 1000,
        'MMscf': x * 0.3048 ** 3 * 1000000,
        'gal': x * 0.003785,
        'liter': x * 0.001,
        'Mgal': x * 3.785,
        #Volumetric Rate
        'm3/day': x,
        'm3/min': x * 1.44 * 10 ** 3,
        'bbl/day': x * 0.15897,
        'bpd': x * 0.15897,
        'bbl/min': x * 228.942,
        'bpm': x * 228.942,
        'stb/day': x * 0.15897,
        'stb/min': x * 228.942,
        'ft3/day': x * 0.028317,
        'scf/day': x * 0.028317,
        'ft3/min': x * 0.028317 * 24 * 60,
        'Mscf/day': x * 28.317,
        'MMscf/day': x * 28.317 * 10 ** 3,
        'gal/min': x * 5.451,
        'gpm': x * 5.451,
        'bbls/min': x * 228.942,
        'liter/min': x * 1.44,
    }
    
    #print(unit_dictionary[x_unit])
    #print(unit_dictionary[y_unit])
    unit = value * unit_dictionary[x_unit] / unit_dictionary[y_unit]
    return unit