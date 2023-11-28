
import pandas as pd
import os
from windpowerlib import get_turbine_types
from windpowerlib import WindFarm,wind_farm
from windpowerlib import WindTurbine
from windpowerlib import TurbineClusterModelChain


"""1. Read Weather Data """

filename = os.path.join(os.path.dirname("__file__"), 'Final Wind Data.csv')
weather = pd.read_csv(filename, index_col=0, header=[0, 1])


#weather.index = pd.to_datetime(weather.index).tz_convert('Europe/Berlin')


l0 = [_[0] for _ in weather.columns]
l1 = [int(_[1]) for _ in weather.columns]
weather.columns = [l0, l1]

"""2. Adding a new temperature column with linear gradient at hub height and a roughness length column"""

hub_height=122
temperature_height=2
weather['temperature_hub','122']=weather['temperature'].apply(lambda x: x-0.0065*(hub_height-temperature_height))
weather=weather.rename(columns={'temperature_hub':'temperature'})

weather['roughness_length','0']=0.15



"""3. Initializing Wind Turbine """

turbine_types=pd.DataFrame(get_turbine_types(turbine_library='local', print_out=False, filter_=True))
turbine_types2=pd.DataFrame(get_turbine_types(turbine_library='oedb', print_out=False, filter_=True))


enercon_115= {
        'hub_height':122,
        'turbine_type':'E-115/3000'}

ener_115=WindTurbine(**enercon_115)

#vestas_117=WindTurbine(150, turbine_type='V117/3600')




""" 4. Wind Farm Calculations """


wind_farm_data = {
    'name': 'wind_farm',
    'wind_turbine_fleet': [ener_115.to_group(total_capacity=40000000)],
    'efficiency': 0.9}
print(wind_farm_data)

wind_farm=WindFarm(**wind_farm_data)


onshore_wind_farm=TurbineClusterModelChain(wind_farm).run_model(weather)
power_output=onshore_wind_farm.power_output
weather['power_output']=power_output


""" 5. Weather data with the power output to a CSV file"""

df = pd.DataFrame(data=weather)
s = df.to_csv('Wind Onshore.csv')




""" 6. Plot Turbine Power Output """


power_output.index=pd.to_datetime(power_output.index)


try:
    from matplotlib import pyplot as plt
  
except ImportError:
    plt = None
    
if plt:
    power_output.plot(color='magenta')
    plt.xlabel('Time')
    plt.ylabel('Power in W')
    plt.savefig('anplot.png', bbox_inches="tight",dpi=800)
    plt.show()
    plt.close()


if plt:
    if ener_115.power_coefficient_curve is not None:
        ener_115.power_coefficient_curve.plot(
            x='wind_speed', y='value', legend=None, marker='.')
            
        plt.xlabel('Wind speed in m/s')
        plt.ylabel('Power in W')
        plt.savefig('epcc.png', bbox_inches="tight",dpi=800)
        plt.show()
        plt.close()
        
    if ener_115.power_curve is not None:
        ener_115.power_curve.plot(x='wind_speed',y='value',legend=None,marker='.')
        
        plt.xlabel('Wind speed in m/s')
        plt.ylabel('Power in W')
        plt.savefig('epc.png', bbox_inches="tight",dpi=800)
        plt.show()
        plt.close()



