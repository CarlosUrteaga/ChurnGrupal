# import modin.pandas as pd
import pandas as pd
strDates = ['2017-01-01', '2017-01-02','2017-02-01', '2017-02-02','201801', '201802', '201803', '201804', '201805', '201806', '201807', '201808', '201809', '201810', '201811', '201812', '201901', '201902', ]
arrayProduct = ['CRÉDITO MUJER', 'COMERCIANTE','CRÉDITO INDIVIDUAL']
for strData in strDates:
	print(strData)
	df1 = pd.read_csv(strData+'.csv')
	df1 = df1[df1.producto.isin(arrayProduct)]
	df1[['fechaOperacion','Contract_Id','IdPersona','IdGrupo','CicloCuentaA','Num_integrantes','Contract_Party_Role_Desc','ciclopersona','ciclopersonapadres','ciclopersonaCM','ciclopersonaCCR','ImportePrestadoA','FrecPagoA','DiasAtraso','TasaInteres','FechaDesembolsoA','FechaFinCreditoA','producto','MaxAtraso','Centro_Beneficios','Sucursal','numNomina','edad','genero','escolaridad','hijos','dependientes',]].to_csv('padres/'+strData+'-s.csv', index=False)
	df1[['fechaOperacion','Contract_Id','IdPersona','FechaDesembolsoA','FechaFinCreditoA','producto']].to_csv('renovar/'+strData+'-s.csv', index=False)
	del df1