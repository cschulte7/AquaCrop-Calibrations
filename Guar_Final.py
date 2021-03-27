# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:01:04 2020

@author: carol
"""

import sys
import csv
_=[sys.path.append(i) for i in ['.', '..']] # finds 'AquaCrop' file

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns # Visualization tool used for high-level interface for drawing attractive and informative stastical graphics
import numpy as np
import pandas as pd
from aquacrop.core import *
from aquacrop.classes_Guar import *
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
#import WINDSfunctionsandclasses13.py

#exec(open("WINDSfunctionsandclasses_July25.py").read())
pathprefix='/home/ecoslacker/Documents/WINDS_Data/'
# sys.path.append(pathprefix)

db=create_engine('mysql://UofABEWINDS:WINDSAWSPort2020@windsdatabase-1.cdzagwevzppe.us-west-1.rds.amazonaws.com:3306/winds_test')
Guar_data = pd.read_sql('SELECT * from Aquacrop_crop_table',con=db)  #Reads all data from mysql db

class plant_data:
    def __init__(self, Guar_data):
        self.Crop_name = Guar_data['Crop Name']
        self.Crop_type = int(Guar_data['Crop Type'])                             
        self.Plant_method= int(Guar_data['Plant Method'])                             
        self.Calendar_type = int(Guar_data['Calendar Type'])                           
        self.SwitchGDD = int(Guar_data['SwitchGDD'])                             
        self.Planting_date = Guar_data['Planting Date']                             
        self.Harvest_date = Guar_data['Harvest Date']                             
        self.Emergence = float(Guar_data['Emergence'])                             
        self.MaxRooting = float(Guar_data['Max Rooting'])                             
        self.Senescence = float(Guar_data['Senescence'])                             
        self.Maturity = float(Guar_data['Maturity'])                             
        self.HIstart = float(Guar_data['HIstart'])                             
        self.Flowering = float(Guar_data['Flowering'])                             
        self.YldForm = float(Guar_data['Yld Form'])                             
        self.GDDmethod = int(Guar_data['GDD Method'])                             
        self.Tbase = float(Guar_data['Tbase']); 
        self.Tupp =float(Guar_data['Tupp']); 
        self.PolHeatStress = int(Guar_data['PolHeatStress']); 
        self.Tmax_up = int(Guar_data['Tmax_up']); 
        self.Tmax_lo = int(Guar_data['Tmax_lo']); 
        self.PolColdStress = int(Guar_data['PolColdStress']); 
        self.Tmin_up = int(Guar_data['Tmin_up']); 
        self.Tmin_lo = int(Guar_data['Tmin_lo']); 
        self.TrColdStress = int(Guar_data['TrColdStress']);
        self.GDD_up = float(Guar_data['GDD_up']);
        self.GDD_lo = float(Guar_data['GDD_lo']);
        self.Zmin = float(Guar_data['Zmin']); 
        self.Zmax = float(Guar_data['Zmax']);
        self.fshape_r = float(Guar_data['fshape_r']); 
        self.SxTopQ = float(Guar_data['SxTopQ']);
        self.SxBotQ = float(Guar_data['SxBotQ']);
        self.SeedSize = float(Guar_data['SeedSize']); 
        self.PlantPop = float(Guar_data['PlantPop']); 
        self.CCx = float(Guar_data['CCx']);
        self.CDC = float(Guar_data['CDC']); 
        self.CGC = float(Guar_data['CGC']); 
        self.Kcb = float(Guar_data['Kcb']);
        self.fage = float(Guar_data['fage']); 
        self.WP = float(Guar_data['WP']); 
        self.WPy = float(Guar_data['Wpy']);
        self.fsink = float(Guar_data['fsink']);
        self.HI0 = float(Guar_data['HI0']);
        self.dHI_pre = float(Guar_data['dHI_pre']);
        self.a_HI = float(Guar_data['a_HI']); 
        self.b_HI = float(Guar_data['b_HI']); 
        self.dHI0 = float(Guar_data['dHI0']);
        self.Determinant = float(Guar_data['Determinant']); 
        self.exc = float(Guar_data['exc']); 
        self.p_up1 = float(Guar_data['p_up1']); 
        self.p_up2 = float(Guar_data['p_up2']); 
        self.p_up3 = float(Guar_data['p_up3']); 
        self.p_up4 = float(Guar_data['p_up4']);
        self.p_lo1 = float(Guar_data['p_lo1']); 
        self.p_lo2 = float(Guar_data['p_lo2']); 
        self.p_lo3 = float(Guar_data['p_lo3']); 
        self.p_lo4 = float(Guar_data['p_lo4']); 
        self.fshape_w1 = float(Guar_data['fshape_w1']);
        self.fshape_w2 = float(Guar_data['fshape_w2']);
        self.fshape_w3 = float(Guar_data['fshape_w3']);
        self.fshape_w4 = float(Guar_data['fshape_w4']);


P = plant_data(Guar_data)

print('Crop type', P.Crop_type)
# Reads in the weather data
weather = pd.read_csv('GuarWeather_Clovis_2018.csv') 
# Prepares the weather data that is in the csv to the format that the aquacrop code needs it in (ten spaces between each value)
with open('GuarWeather_Clovis_2018.txt', 'w') as f: weather.to_string(f, col_space = 10, index=False, justify = 'left') 
# Uses the function prepare weather to convert weather data
wdf = prepare_weather('GuarWeather_Clovis_2018.txt') 
# Grabs the soil class from the classes.py file
soil = SoilClass('ClayLoamGuar2018') 
# Prepares the crop class with the name of the crop, planting date, and harvest date
crop = CropClass('GuarGDD', P, PlantingDate='06/15',HarvestDate='11/16') 
# Initialize water content to be field capacity 
InitWC = InitWCClass(value=['FC']) 
# The model is run using SimStartTime, SimEndTime, weather data, soil, crop, initial water content
model = AquaCropModel('2018/06/15','2018/11/16', wdf,soil,crop, InitWC) 
model.initialize() 
model.step(till_termination=True)

# Allows for the outputs below to show all columns when printed
pd.set_option('max_columns', None) 
 # Daily Water Flux dataframe. The 'none' removes the limit from the output so all the data can be shown
FluxHead = model.Outputs.Flux.head(None)
# Soil-water content in each soil compartment dataframe
WaterHead = model.Outputs.Water.head(None) 
# Crop growth dataframe
GrowthHead = model.Outputs.Growth.head(None) 
# Final summary (seasonal total) dataframe
FinalHead = model.Outputs.Final.head(None) 


# Plotting canopy coverage over time (days after planting)
plt1 = GrowthHead.plot(x ='DAP', y='CC', kind='scatter', title = 'Canopy Coverage over Time')
plt1.set_ylabel("Canopy Coverage")
plt1.set_xlabel("Days After Planting (DAP)")

# Plotting biomass over time (days after planting)
plt2 = GrowthHead.plot(x ='DAP', y='B', kind='scatter', title = 'Biomass with Stress over Time')
plt2.set_ylabel("Biomass (kg/ha)")
plt2.set_xlabel("Days After Planting (DAP)")

# Plotting biomass with no stress conditions over time (days after planting)
plt3 = GrowthHead.plot(x ='DAP', y='B_NS', kind='scatter', title = 'Biomass without Stress over Time')
plt3.set_ylabel("Biomass (kg/ha)")
plt3.set_xlabel("Days After Planting (DAP)")

# The following are print statements to see different outputs
# Final summary (season total)
print('\n Final Summary = \n', FinalHead) 
# Daily water flux
print('\n Daily Water Flux = \n', FluxHead) 
 # Soil water content in each soil compartment
print('\n Soil Water Content = \n', WaterHead)
# Crop growth
print('\n Crop Growth = \n', GrowthHead) 

