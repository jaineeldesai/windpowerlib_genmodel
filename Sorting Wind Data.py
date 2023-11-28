import pandas as pd


"""Making Changes in the original wind data from the Power Nasa Api"""

open=pd.read_csv("Raw_Wind_Data.csv",skiprows=15)
df=open.copy()
df = df.rename(columns={'WSC':'WS150M','MO':'Month','DY':'Day','HR':'Hour','PS':'pressure','T2M':'temperature'})
df['DateTime']=pd.to_datetime(df[['YEAR', 'Month', 'Day','Hour']],format="%Y %m %d,, %H:%M:%S")
df=df.drop(columns=['YEAR','Month','Day','Hour'])
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df=df[cols]
df['temperature']=df['temperature'].apply(lambda x:x+273.15)
df['pressure']=df['pressure'].apply(lambda x:x*1000)

df.to_csv('Final Wind Data.csv',index=False,date_format='%Y-%m-%d  %H:%M:%S')
saved_csv=pd.read_csv('Final Wind Data.csv')






