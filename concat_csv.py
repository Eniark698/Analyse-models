def get():
    import pandas as pd
    from os import mkdir, listdir, getpid, stat, remove, getcwd


    # get the current working directory
    current_working_directory = getcwd()

    try:
        remove(current_working_directory+'/merging/RESULT_csv.csv')
    except:
        pass


    list=listdir(current_working_directory+'/csv')


    df = pd.DataFrame()


    for i in list:
        df1= pd.read_csv(current_working_directory + '/csv/{}'.format(i))
        df1=df1.drop(columns=['Report Name','Page Name','Selection Pane Name','QueryRefType'])
        df=pd.concat([df, df1])


    df=df.groupby(['Table','Col/Measure'])['Data Element Count'].count()
    df=pd.DataFrame(df)
    df=df.sort_values('Data Element Count', ascending=False)

    df.to_csv(current_working_directory+'/merging/RESULT_csv.csv',encoding='utf-16', sep='\t')

