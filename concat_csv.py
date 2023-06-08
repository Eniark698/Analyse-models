def get():
    import pandas as pd
    from os import mkdir, listdir, getpid, stat, remove, getcwd


    # get the current working directory
    current_working_directory = getcwd()

    try:
        remove(current_working_directory+'/side_files/RESULT_csv.csv')
    except:
        pass


    list_first = listdir(current_working_directory+'/side_files/csv/first/')
    list_second = listdir(current_working_directory+'/side_files/csv/second/')
    list_third = listdir(current_working_directory+'/side_files/csv/third/')
    df = pd.DataFrame()


    for i in list_first:
        df1 = pd.read_csv(current_working_directory+'/side_files/csv/first/{}'.format(i))
        df1 = pd.DataFrame(df1)
        df1 = df1.drop(columns=['Report Name','Page Name','Selection Pane Name','QueryRefType','Data Element Count'])
        df = pd.concat([df, df1])

    for i in list_second:
        df1 = pd.read_csv(current_working_directory+'/side_files/csv/second/{}'.format(i))
        df1 = df1.drop(columns=['ReportName','Page Name','name','Page Filter Count'])
        df = pd.concat([df, df1])

    for i in list_third:
        df1 = pd.read_csv(current_working_directory+'/side_files/csv/third/{}'.format(i))
        df1 = df1.drop(columns=['Filter Name','Filter Type'])
        df = pd.concat([df, df1])

    

    #df = df.groupby(['Table','Col/Measure'])['Data Element Count'].count()
    
    df = pd.DataFrame(df)
    df = df.drop_duplicates()
    df = df.sort_values(['Table','Col/Measure'], ascending=True)

    df.to_csv(current_working_directory+'/side_files/RESULT_csv.csv',encoding='utf-16', sep='\t', index=False)
