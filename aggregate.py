import pandas as pd

new = pd.read_csv("2023H2.csv",skiprows=7)
old = pd.read_csv("2023H1.csv",skiprows=7)
H2_2022=pd.read_csv("2022H2.csv",skiprows=7)
H1_2022=pd.read_csv("2022H1.csv",skiprows=7)
H4_2021=pd.read_csv("2021H4.csv",skiprows=7)
#H3_2021=pd.read_csv("2021H3.csv",skiprows=7)
#H2_2021=pd.read_csv("2021H2.csv",skiprows=7)
#H1_2021=pd.read_csv("2021H1.csv",skiprows=7)
#H4=pd.read_csv("2020H4.csv",skiprows=7)
#H3=pd.read_csv("2020H3.csv",skiprows=7)

"""
H3_2021['Ticker'] = H3_2021['Ticker'].str.replace("NYSE:", "")
H3_2021['Ticker'] = H3_2021['Ticker'].str.replace("NASDAQGS:", "")
H3_2021['Ticker'] = H3_2021['Ticker'].str.replace("NASDAQCM:", "")
H3_2021['Ticker'] = H3_2021['Ticker'].str.replace("NASDAQGM:", "")
H3_2021['Ticker'] = H3_2021['Ticker'].str.replace("TSX:", "")
"""


merge=pd.merge(new,old,on='Ticker',how='outer')
merge=merge.fillna(0)
merge['shares_differ']=merge['Shares_x']-merge['Shares_y']
merge['value_differ']=merge['Value_x']-merge['Value_y']
merge=merge.sort_values('value_differ',ascending=False)
merge.to_csv("Ray_dalio_2023H1to2023H2.csv")
