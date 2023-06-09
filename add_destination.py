def dest():    
    import numpy as np
    import pandas as pd
    import os

    current_working_directory = os.getcwd()

    try:
        os.remove(current_working_directory+'/output/result_with_dest.csv')
    except:
        pass

    df=pd.DataFrame()
    list_first = os.listdir(current_working_directory+'/side_files/csv/first/')
    list_second = os.listdir(current_working_directory+'/side_files/csv/second/')
    list_third = os.listdir(current_working_directory+'/side_files/csv/third/')

    for i in list_first:
        df1 = pd.read_csv(current_working_directory+'/side_files/csv/first/{}'.format(i))
        df1 = pd.DataFrame(df1)
        df1 = df1.drop(columns=['Page Name','Selection Pane Name','QueryRefType','Data Element Count'])
        df = pd.concat([df, df1])

    for i in list_second:
        df1 = pd.read_csv(current_working_directory+'/side_files/csv/second/{}'.format(i))
        df1 = df1.drop(columns=['Page Name','name','Page Filter Count'])
        df1=df1.rename(columns={'ReportName':"Report Name"})
        df = pd.concat([df, df1])

    for i in list_third:
        df1 = pd.read_csv(current_working_directory+'/side_files/csv/third/{}'.format(i))
        df1 = df1.drop(columns=['Filter Name','Filter Type'])
        df1['Report Name']=i[0:-3]+'pbix'
        df = pd.concat([df, df1])

    df['Concat']="'"+ df['Table']+"'[" + df['Col/Measure'] + ']'
    df=df.drop(columns=['Table', 'Col/Measure']).sort_values(by=['Concat'])
    df=df.drop_duplicates()
    df=df[['Concat', 'Report Name']]
    df.to_csv(current_working_directory+'/output/result_with_dest.csv',encoding='utf-16', sep='\t', index=False)