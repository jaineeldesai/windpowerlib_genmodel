# Generation Modelling using 'windpowerlib'

## Introduction
The wind farm considered in this project for power generation is an onshore wind farm with a capacity of 40MW, and this system is modelled using Python and a modelling library known as 'windpowerlib'.

### Site Selection and Weather Data
To use windpowerlib, the first step is to acquire weather data for a particular location. For the wind farm site in this project, a plain open field is selected in the city of Nordhausen, Germany, at the coordinates (51.4919, 10.8757). The annual wind power output produced from the wind farm is dependent on the wind flowing at the site.

To acquire the weather data for this location to be used by the windpowerlib, POWER NASA API is used (https://power.larc.nasa.gov/).
On executing the API with the user-supplied parameters, the weather dataset in an hourly time-series is ready
and can be downloaded in a CSV file, which is [Raw_Wind_Data](https://github.com/jaineeldesai/windpowerlib_genmodel/blob/main/Raw_Wind_Data.csv).

### Cleaning the Weather Data

The weather dataset in the form of CSV file, Raw_Wind_Data, is imported by the windpowerlib to calculate the power output of a wind turbine. 
However, the weather data acquired from the API is not in the same units as required by the windpowerlib. 
The necessary changes to the weather dataset are made using Python along with the use of its packages and a new weather dataset is created in a CSV file, 
[Final Wind Data](https://github.com/jaineeldesai/windpowerlib_genmodel/blob/main/Final%20Wind%20Data.csv). 
The code for the cleaning is in [Sorting Wind Data](https://github.com/jaineeldesai/windpowerlib_genmodel/blob/main/Sorting%20Wind%20Data.py).

### Wind Turbine Selection and Initialization

The next step is the initialization of the wind turbine. Before the initialisation, the
wind turbine selection is to be done. The wind turbine generators (WTG) from Enercon,
Vestas, Nordex, Senvion and Siemens are frequently realised WTG in Germany.
In 2018, a total of 56 WTGs and 114 different configurations (type, output, rotor diameter
and hub height) were installed in Germany. The Enercon E-115 with a capacity of 3
MW was the most frequently installed, followed by Vestas V126 with 3.45 MW.

In this project, Enercon E-115 is selected as the WTG with a hub height of 122 m. The
windpowerlib’s oedb turbine library contains the data for the Enercon E-115 and using
the code for turbine initilaization, the wind turbine is initialized.

### Power Generation

The final step is getting the power output from the wind turbines for the imported
weather data. It is required to specify the capacity of the wind farm, since the total
number of turbines needed are calculated based on the total capacity. This project aims to
construct a wind farm of 40 MW capacity. A class called 'TurbineClusterModelChain' in
windpowerlib is used to calculate the power output of the wind farm. The power output
values along with the weather data are stored in a new CSV file, [Wind Onshore](https://github.com/jaineeldesai/windpowerlib_genmodel/blob/main/Wind%20Onshore.csv).

The complete code for the wind farm generation model is in [Wind Farm](https://github.com/jaineeldesai/windpowerlib_genmodel/blob/main/Wind%20Farm.py).
