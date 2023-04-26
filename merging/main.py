import numpy as np
import pandas as pd
import re
import warnings
import os
warnings.filterwarnings("ignore")
try:
    os.remove('./InJOIN.xlsx')
    os.remove('./NotInJOIN.xlsx')
except:
    pass


data=pd.read_excel(io='./VertiPaq Analyzer 2.10.xlsm', sheet_name='Columns')
dat=pd.read_excel(io='./VertiPaq Analyzer 2.10.xlsm', sheet_name='DAX Expressions')
data = data['IsRowNumber']
data = data.drop(index=[0,1,322])
data=pd.DataFrame(data)
dat=dat[['Table', 'Name']]
dat = dat.drop(index=0)
dat2=np.empty(len(dat),dtype="<U200")
j=0

for i, row in dat.iterrows():
    text = row['Table']
    text1 = row['Name']
    res= "'"+ text + "'"+ "[" + text1 + "]"
    dat2[j]= res
    j+=1

    
df1 = pd.DataFrame(dat2, columns = ['IsRowNumber'])
frames = [df1, data]

result = pd.concat(frames)
result=pd.DataFrame(result)










data1=pd.read_excel(io='./result.xlsx', sheet_name='RESULT')
data1=data1[['Table', 'Col/Measure']]

data1 = data1.assign(CC=np.zeros(len(data1)))
data2=np.empty(len(data1),dtype="<U200")
j=0

for i, row in data1.iterrows():
    text = row['Table']
    text1 = row['Col/Measure']
    res= "'"+ text + "'"+ "[" + text1 + "]"
    data2[j]= res
    j+=1

    
result1 = pd.DataFrame(data2, columns = ['IsRowNumber'])


#result['IsRowNumber']==result1['IsRowNumber']

InJOIN=result.merge(result1, on='IsRowNumber')
InJOIN.to_excel('./InJOIN.xlsx')
NotInJOIN=result[~result['IsRowNumber'].isin(result1['IsRowNumber'])]
NotInJOIN.to_excel('./NotInJOIN.xlsx')

tlen=len(result)
ilen=len(InJOIN)
nilen=len(NotInJOIN)
print(ilen + nilen)
print(tlen)



