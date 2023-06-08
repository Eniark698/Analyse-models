import numpy as np
import pandas as pd
from os import mkdir, listdir, getpid, stat, remove, getcwd


df_org=pd.read_excel('./output/InJOIN.xlsx', index_col='Unnamed: 0')
df=df_org.copy(deep=False)
df_org['checking'] =np.empty(len(df_org),dtype="<U200")



current_working_directory = getcwd()
list=listdir(current_working_directory + '/csv/')


for file in list:
    df_new=pd.read_csv(current_working_directory+'/csv/'+file)
    df_new=df_new[['Table', 'Col/Measure']]
    blank=np.empty(len(df_new),dtype="<U200")
    j=0
    for i, row in df_new.iterrows():

        if row['Col/Measure'] is None:
            continue
        text = str(row['Table'])
        text1 = str(row['Col/Measure'])
        res= "'"+ text + "'"+ "[" + text1 + "]"
        blank[j]= res
        j+=1
    blank=pd.DataFrame(blank,columns=["IsRowNumber"])
    for i1, row in df.iterrows():
        print('NEW\n'+row)
        for i1, row_1 in df_new.iterrows():
            print('NEW\n'+row_1)
            quit()



    