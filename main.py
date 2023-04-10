import pandas as pd
from os import mkdir, listdir, getpid, stat, remove


list=listdir('./files/')


df = pd.DataFrame()


for i in list:
    df1= pd.read_csv('./files/{}'.format(i))
    df1=df1.drop(columns=['Report Name','Page Name','Selection Pane Name','QueryRefType'])
    df=pd.concat([df, df1])





df=df.groupby(['Table','Col/Measure'])['Data Element Count'].count()
df=pd.DataFrame(df)
df=df.sort_values('Data Element Count', ascending=False)


#.sort_values(by='Data Element Count', ascending=False)
df.to_csv('./RESULT.csv',encoding='utf-16', sep='\t')

