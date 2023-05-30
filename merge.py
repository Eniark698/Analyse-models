def merge():
    import numpy as np
    import pandas as pd
    from warnings import filterwarnings
    from os import getcwd, remove
    filterwarnings("ignore")
    current_working_directory = getcwd()

    try:
        remove(current_working_directory+'/output/InJOIN.xlsx')
        remove(current_working_directory+'/output/NotInJOIN.xlsx')
    except:
        pass


    Columns_table=pd.read_excel(io=current_working_directory+'/merging/readed_file.xlsm', sheet_name='Columns')
    Columns_table = Columns_table['IsRowNumber']
    Columns_table = Columns_table.drop(index=[0,1])
    Columns_table=pd.DataFrame(Columns_table)

    Measure_table=pd.read_excel(io=current_working_directory+ '/merging/readed_file.xlsm', sheet_name='DAX Expressions')
    Measure_table=Measure_table[['Table', 'Name']]
    Measure_table = Measure_table.drop(index=0)

    blank=np.empty(len(Measure_table),dtype="<U200")
    j=0



    for i, row in Measure_table.iterrows():

        if row['Name'] is None:
            continue
        text = str(row['Table'])
        text1 = str(row['Name'])
        res= "'"+ text + "'"+ "[" + text1 + "]"
        blank[j]= res
        j+=1



    Measure_table = pd.DataFrame(blank, columns = ['IsRowNumber'])
    frames = [Columns_table, Measure_table]

    result = pd.concat(frames)
    result =pd.DataFrame(result)


    del Columns_table,Measure_table







    Combined_csv=pd.read_csv(current_working_directory+'/merging/RESULT_csv.csv', encoding='utf-16', sep='\t')
    Combined_csv=Combined_csv[['Table', 'Col/Measure']]

    Combined_csv = Combined_csv.assign(CC=np.zeros(len(Combined_csv)))
    blank_2=np.empty(len(Combined_csv),dtype="<U200")
    j=0

    for i, row in Combined_csv.iterrows():
        text = row['Table']
        text1 = row['Col/Measure']
        res= "'"+ text + "'"+ "[" + text1 + "]"
        blank_2[j]= res
        j+=1


    result_model = pd.DataFrame(blank_2, columns = ['IsRowNumber'])


    #result['IsRowNumber']==result1['IsRowNumber']

    InJOIN=result.merge(result_model, on='IsRowNumber').sort_values(by=['IsRowNumber'])
    InJOIN.to_excel(current_working_directory+'/output/InJOIN.xlsx')
    NotInJOIN=result[~result['IsRowNumber'].isin(result_model['IsRowNumber'])].sort_values(by=['IsRowNumber'])
    NotInJOIN.to_excel(current_working_directory+'/output/NotInJOIN.xlsx')

    tlen=len(result)
    ilen=len(InJOIN)
    nilen=len(NotInJOIN)
    print(ilen + nilen)
    print(tlen)



