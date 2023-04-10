import pandas as pd
from os import mkdir, listdir, getpid, stat, remove

list=listdir('./files/')
print(list)


df = pd.DataFrame()

for i in list:
    df1= pd.read_csv('./files/{}'.format(i))
    df=pd.concat([df, df1])

print(df)

print(df.groupby(['Table']))