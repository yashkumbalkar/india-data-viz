import pandas as pd

latlong = pd.read_csv('district wise centroids.csv')
latlong.head()

latlong.shape

latlong.isnull().sum()

latlong.duplicated().sum()

census = pd.read_csv('india-districts-census-2011.csv')
census.head()

census.shape

merge_df = latlong.merge(census,left_on='District',right_on='District name').drop(columns=['District name'])

merge_df.shape

merge_df.head()

cols = ['State','District','Latitude','Longitude','District code','Population','Male','Female','Literate','Households_with_Internet','Housholds_with_Electric_Lighting','Rural_Households','Urban_Households','Total_Power_Parity']

final_df = merge_df[cols]
final_df.head()

final_df['sex_ratio'] = round((final_df['Female']/final_df['Male'])*100)

final_df['literacy_rate'] = round((final_df['Literate']/final_df['Population'])*100)

final_df.shape

final_df.head()

final_df.to_csv('india.csv', index= False)

