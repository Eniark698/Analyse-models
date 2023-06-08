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


    Columns_table=pd.read_excel(io=current_working_directory+'/side_files/model.xlsm', sheet_name='Columns')
    Columns_table = Columns_table['IsRowNumber']
    l=len(Columns_table)
    Columns_table = Columns_table.drop(index=[0,1,l-1])
    Columns_table=pd.DataFrame(Columns_table)
    temp_pd=pd.DataFrame(columns=['Table', 'Name'])
   
    for i,row in Columns_table.iterrows():
        a=row[0].find('[')
        item=row[0]
        Table=item[1:a-1]
        Column=item[a+1:-1]
        temp_pd.loc[i] = [Table, Column]

    Measure_table=pd.read_excel(io=current_working_directory+ '/side_files/model.xlsm', sheet_name='DAX Expressions')
    Measure_table=Measure_table[['Table', 'Name']]
    Measure_table = Measure_table.drop(index=0)

    

    result=pd.concat([temp_pd,Measure_table])
    result =pd.DataFrame(result)
    result=result.drop_duplicates()
    result=result.sort_values(['Table','Name'], ascending=True)
    result=result.rename(columns={'Name':'Col/Measure'})


    del Columns_table,Measure_table
 




    Combined_csv=pd.read_csv(current_working_directory+'/side_files/RESULT_csv.csv', encoding='utf-16', sep='\t')
    result_model=Combined_csv[['Table', 'Col/Measure']]
   
    del Combined_csv
   




    #result['IsRowNumber']==result1['IsRowNumber']

    InJOIN=result.merge(result_model, on=['Table', 'Col/Measure']).sort_values(by=['Table', 'Col/Measure']).drop_duplicates()
    NotInJOIN=result[~result[['Table', 'Col/Measure']].isin(result_model[['Table', 'Col/Measure']])].sort_values(by=['Table', 'Col/Measure']).drop_duplicates()
    InJOIN.rename(columns={"IsRowNumber": "Name"})
    NotInJOIN.rename(columns={"IsRowNumber": "Name"})
    InJOIN.to_excel(current_working_directory+'/output/InJOIN.xlsx', index=False)
    NotInJOIN.to_excel(current_working_directory+'/output/NotInJOIN.xlsx',index=False)


    print('done')


