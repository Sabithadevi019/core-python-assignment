import pandas as pd
import numpy as np
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:1234@localhost/eda')
df1 = pd.read_sql('SELECT * FROM Household_Energy_Consumption', engine)
df2 = pd.read_csv('panda.csv')
merge_df = pd.merge(df1, df2, on='household_id', how='outer')
merged_table_name = 'merged_household_data'
merge_df.to_sql(merged_table_name, con=engine, if_exists='replace', index=False)
merge= pd.read_sql(f'SELECT * FROM {merged_table_name}', engine)
pd.set_option('display.max_columns',None)
print("\nMerged Table Data:")
print(merge)
print(merge['household_id'].dtypes)
print(f'Memory Usage:{merge.memory_usage(deep=True)}')
merge_df['household_id']=merge_df['household_id'].astype(np.int16)
print(merge_df['household_id'].memory_usage(deep=True))
print(merge_df['household_id'].dtypes)
print(merge_df.dtypes)
merge_df['date']=merge_df['date'].astype('category')
print('object to category:',merge_df['date'].dtypes)
