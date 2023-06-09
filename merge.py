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
    Columns_table=Columns_table.rename(columns={'IsRowNumber':"'Table'[Column]"})




    Measure_table=pd.read_excel(io=current_working_directory+ '/side_files/model.xlsm', sheet_name='DAX Expressions')
    Measure_table=Measure_table[['Table', 'Name']]
    Measure_table = Measure_table.drop(index=0)

    Measure_table['Concat']="'"+ Measure_table['Table']+"'[" + Measure_table['Name'] + ']'
    Measure_table=Measure_table.drop(columns=['Table', 'Name'])
    Measure_table=Measure_table.rename(columns={'Concat':"'Table'[Column]"})


    result_model=pd.concat([Columns_table,Measure_table],ignore_index=True)
    result_model =pd.DataFrame(result_model)
    result_model=result_model.drop_duplicates()

    result_model["'Table'[Column]"].str.strip()
    result_model=result_model.sort_values(["'Table'[Column]"], ascending=True)

    del Columns_table,Measure_table
 

    


    Combined_csv=pd.read_csv(current_working_directory+'/side_files/RESULT_csv.csv', encoding='utf-16', sep='\t')
    result_reports=Combined_csv[['Table', 'Col/Measure']]

    result_reports['Concat']="'"+ result_reports['Table']+"'[" + result_reports['Col/Measure'] + ']'
    result_reports=result_reports.drop(columns=['Table', 'Col/Measure'])
    result_reports=result_reports.rename(columns={'Concat':"'Table'[Column]"})

    del Combined_csv
   
    result_reports["'Table'[Column]"].str.strip()
    


    
  
    


    InJOIN=result_model.merge(result_reports, on=["'Table'[Column]"], how='inner').sort_values(by=["'Table'[Column]"]).drop_duplicates()
    NotInJOIN=result_model[result_model["'Table'[Column]"].isin(InJOIN["'Table'[Column]"])==False]

    InJOIN.to_excel(current_working_directory+'/output/InJOIN.xlsx', index=False)
    NotInJOIN.to_excel(current_working_directory+'/output/NotInJOIN.xlsx',index=False)


    print('done')


