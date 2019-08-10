import pandas as pd

from datetime import datetime
from datetime import timedelta

import sys
sys.path.append('../')
from time_functions import *

# Read Files
df1 = pd.read_csv('renovar/2017-01-01-s.csv')
df2 = pd.read_csv('renovar/2017-01-02-s.csv')
df3 = pd.read_csv('renovar/2017-02-01-s.csv')
df4 = pd.read_csv('renovar/2017-02-02-s.csv')
df5 = pd.read_csv('renovar/201801-s.csv')
df6 = pd.read_csv('renovar/201802-s.csv')
df7 = pd.read_csv('renovar/201803-s.csv')
df8 = pd.read_csv('renovar/201804-s.csv')
df9 = pd.read_csv('renovar/201805-s.csv')
dfA = pd.read_csv('renovar/201806-s.csv')
dfB = pd.read_csv('renovar/201807-s.csv')
dfC = pd.read_csv('renovar/201808-s.csv')
dfD = pd.read_csv('renovar/201809-s.csv')
dfE = pd.read_csv('renovar/201810-s.csv')
dfF = pd.read_csv('renovar/201811-s.csv')
dfG = pd.read_csv('renovar/201812-s.csv')
dfH = pd.read_csv('renovar/201901-s.csv')
dfI = pd.read_csv('renovar/201902-s.csv')

# Append dataframes
df1 = df1.append(df2)
df1 = df1.append(df3)
df1 = df1.append(df4)
df1 = df1.append(df5)
df1 = df1.append(df6)
df1 = df1.append(df7)
df1 = df1.append(df8)
df1 = df1.append(df9)
df1 = df1.append(dfA)
df1 = df1.append(dfB)
df1 = df1.append(dfC)
df1 = df1.append(dfD)
df1 = df1.append(dfE)
df1 = df1.append(dfF)
df1 = df1.append(dfG)
df1 = df1.append(dfH)
df1 = df1.append(dfI)

del df2, df3, df4, df5, df6, df7, df8, df9, dfA, dfB, dfC, dfD, dfE, dfF, dfG, dfH, dfI

# Keep Only CM and CCR
df2 = df1.loc[df1.producto!='CRÉDITO INDIVIDUAL',:]
del df1
df1 = df2.loc[:,:]

# Extract fechaOperacion sorted
dfM = df1.loc[:, ['fechaOperacion', 'Contract_Id']]
dfM = dfM.sort_values('fechaOperacion')
m = dfM.fechaOperacion.unique().tolist()

# df1['unique_count'] = df1.groupby(['IdGrupo']).transform('count')['IdGrupo']

# must pop (last three to change parameter)
i = 0 
m = ['2017-01-31 00:00:00.000',
 '2017-02-28 00:00:00.000',
 '2017-03-31 00:00:00.000',
 '2017-04-30 00:00:00.000',
 '2017-05-31 00:00:00.000',
 '2017-06-30 00:00:00.000',
 '2017-07-31 00:00:00.000',
 '2017-08-31 00:00:00.000',
 '2017-09-30 00:00:00.000',
 '2017-10-31 00:00:00.000',
 '2017-11-30 00:00:00.000',
 '2017-12-31 00:00:00.000',
 '2018-01-31 00:00:00.000',
 '2018-02-28 00:00:00.000',
 '2018-03-31 00:00:00.000',
 '2018-04-30 00:00:00.000',
 '2018-05-31 00:00:00.000',
 '2018-06-30 00:00:00.000',
 '2018-07-31 00:00:00.000',
 '2018-08-31 00:00:00.000',
 '2018-09-30 00:00:00.000',
 '2018-10-31 00:00:00.000',
 '2018-11-30 00:00:00.000']


for each in m:
    str_time= each 
    datetimeObj = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S.%f')
    month_first_day = datetime(get_previous_year(datetimeObj.year,  datetimeObj.month)
                                    ,  get_previous_month(datetimeObj.month)
                                    , 1)
    next_two_month_first_day = datetime(get_next_year(get_next_year(datetimeObj.year, datetimeObj.month), get_next_month(datetimeObj.month))
                                        , get_next_month(get_next_month(datetimeObj.month))
                                        , 1)
    next_two_month_last_day = datetime(
                                        get_next_year(get_next_year(  get_next_year(datetimeObj.year, datetimeObj.month), get_next_month(datetimeObj.month)),get_next_month(get_next_month(datetimeObj.month)))
                                        , get_next_month(get_next_month(get_next_month(datetimeObj.month)))
                                        , get_last_day(get_next_month(get_next_month(get_next_month(datetimeObj.month)))))
    str_time2 = datetime.strptime(str(next_two_month_last_day)+'.000', '%Y-%m-%d %H:%M:%S.%f')
    previous_month_first_day = datetime(get_previous_year(str_time2.year, str_time2.month), get_previous_month(str_time2.month), 1)
    # last_day_current_date  = datetime(str_time2.year, str_time2.month, get_last_day(str_time2.month))
    
    # Desembolso
    dfT = df1.loc[ ((df1.fechaOperacion==str(next_two_month_last_day)+'.000') 
                    & ( df1.FechaDesembolsoA >= month_first_day.strftime('%Y-%m-%d')) 
                    & ( df1.FechaDesembolsoA < next_two_month_last_day.strftime('%Y-%m-%d')))    
                  ,['Contract_Id','IdPersona','producto', 'FechaDesembolsoA']]
    # print(len(dfT))
    dfT.columns = ['New_Contract_Id', 'IdPersona','New_producto', 'New_FechaDesembolsoA']

    # Fin Credito
    dfT2 = pd.merge(df1.loc[((df1.fechaOperacion==str_time) 
                             & ( df1.FechaFinCreditoA > datetimeObj.strftime('%Y-%m-%d')) 
                             & ( df1.FechaFinCreditoA < next_two_month_first_day.strftime('%Y-%m-%d'))) 
                           ], 
                    dfT, on='IdPersona',how='left')         

    dfT2.loc[dfT2.New_Contract_Id.isnull(),'New_Contract_Id'] = dfT2.Contract_Id
    dfT2.loc[(dfT2.Contract_Id!=dfT2.New_Contract_Id) ,"Churn"] = 0
    dfT2.loc[dfT2.Churn.isnull(),'Churn'] = 1
    dfT2.loc[:,"DiasDesembolso"] = pd.to_datetime(dfT2.New_FechaDesembolsoA)-pd.to_datetime(dfT2.FechaFinCreditoA)
    
    # print(dfT2.Churn.sum())
    dfT2.DiasDesembolso = dfT2['DiasDesembolso'].astype('timedelta64[D]')
    
    if i == 0:
        dfT2[['fechaOperacion','Contract_Id','IdPersona', 'producto','Churn', 'DiasDesembolso']].to_csv("ChurnTest20190813.csv",index=False)
        i=1
    else:
        dfT2[['fechaOperacion','Contract_Id','IdPersona', 'producto','Churn', 'DiasDesembolso']].to_csv("ChurnTest20190813.csv",index=False, mode='a', header=False)
    print(dfT2.groupby(['fechaOperacion','Churn'])['fechaOperacion'].count())
    print(len(dfT2) - len(df1.loc[((df1.fechaOperacion==str_time) 
                             & ( df1.FechaFinCreditoA > datetimeObj.strftime('%Y-%m-%d')) 
                             & ( df1.FechaFinCreditoA < next_two_month_first_day.strftime('%Y-%m-%d'))) 
                           ]))
    print(len(dfT2))


m = ['2018-12-31 00:00:00.000']


for each in m:
    str_time= each 
    datetimeObj = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S.%f')
    month_first_day = datetime(datetimeObj.year
                                    ,  datetimeObj.month
                                    , 1)
    next_two_month_first_day = datetime(get_next_year(get_next_year(datetimeObj.year, datetimeObj.month), get_next_month(datetimeObj.month))
                                        , get_next_month(get_next_month(datetimeObj.month))
                                        , 1)
    next_two_month_last_day = datetime(get_next_year(get_next_year(datetimeObj.year, datetimeObj.month), get_next_month(datetimeObj.month))
                                       , get_next_month(get_next_month(datetimeObj.month))
                                       , get_last_day(get_next_month(get_next_month(datetimeObj.month))))
    str_time2 = datetime.strptime(str(next_two_month_last_day)+'.000', '%Y-%m-%d %H:%M:%S.%f')
    previous_month_first_day = datetime(get_previous_year(str_time2.year, str_time2.month), get_previous_month(str_time2.month), 1)# last_day_current_date  = datetime(str_time2.year, str_time2.month, get_last_day(str_time2.month))
    
    # Desembolso
    dfT = df1.loc[ ((df1.fechaOperacion==str(next_two_month_last_day)+'.000') 
                    & ( df1.FechaDesembolsoA >= month_first_day.strftime('%Y-%m-%d')) 
                    & ( df1.FechaDesembolsoA < next_two_month_last_day.strftime('%Y-%m-%d')))    
                  ,['Contract_Id','IdPersona','producto', 'FechaDesembolsoA']]
    # print(len(dfT))
    dfT.columns = ['New_Contract_Id', 'IdPersona','New_producto', 'New_FechaDesembolsoA']

    # Fin Credito
    dfT2 = pd.merge(df1.loc[((df1.fechaOperacion==str_time) 
                             & ( df1.FechaFinCreditoA > datetimeObj.strftime('%Y-%m-%d')) 
                             & ( df1.FechaFinCreditoA < next_two_month_first_day.strftime('%Y-%m-%d'))) 
                           ], 
                    dfT, on='IdPersona',how='left')         

    dfT2.loc[dfT2.New_Contract_Id.isnull(),'New_Contract_Id'] = dfT2.Contract_Id
    dfT2.loc[(dfT2.Contract_Id!=dfT2.New_Contract_Id) ,"Churn"] = 0
    dfT2.loc[dfT2.Churn.isnull(),'Churn'] = 1
    dfT2.loc[:,"DiasDesembolso"] = pd.to_datetime(dfT2.New_FechaDesembolsoA)-pd.to_datetime(dfT2.FechaFinCreditoA)
    
    # print(dfT2.Churn.sum())
    dfT2.DiasDesembolso = dfT2['DiasDesembolso'].astype('timedelta64[D]')
    
    if i == 0:
        dfT2[['fechaOperacion','Contract_Id','IdPersona', 'producto','Churn', 'DiasDesembolso']].to_csv("ChurnTest20190813.csv",index=False)
        i=1
    else:
        dfT2[['fechaOperacion','Contract_Id','IdPersona', 'producto','Churn', 'DiasDesembolso']].to_csv("ChurnTest20190813.csv",index=False, mode='a', header=False)
    print(dfT2.groupby(['fechaOperacion','Churn'])['fechaOperacion'].count())
    print(len(dfT2) - len(df1.loc[((df1.fechaOperacion==str_time) 
                             & ( df1.FechaFinCreditoA > datetimeObj.strftime('%Y-%m-%d')) 
                             & ( df1.FechaFinCreditoA < next_two_month_first_day.strftime('%Y-%m-%d'))) 
                           ]))
    print(len(dfT2))
