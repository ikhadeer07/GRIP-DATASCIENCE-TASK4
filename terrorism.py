import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load the dataset
df = pd.read_csv('globalterrorismdb_0718dist.csv', encoding='ISO-8859-1', low_memory=False)

# print the first 5 rows of the dataframe
print(df.head())

# print the shape of the dataframe
print(df.shape)

# print the column names
print(df.columns)

# print the summary statistics of the numerical columns
print(df.describe())

# check for missing values
print(df.isnull().sum())

# drop unnecessary columns
df.drop(['eventid', 'approxdate', 'extended', 'resolution', 'country', 'region', 'vicinity', 'crit1', 'crit2', 'crit3', 'doubtterr', 'alternative', 'alternative_txt', 'multiple', 'success', 'suicide', 'attacktype1', 'attacktype2', 'attacktype3', 'targtype1', 'targsubtype1', 'corp1', 'target1', 'natlty1', 'natlty2', 'natlty3', 'guncertain1', 'guncertain2', 'guncertain3', 'claimed', 'claimmode', 'claimmode_txt', 'claim2', 'claimmode2', 'claimmode2_txt', 'claim3', 'claimmode3', 'claimmode3_txt', 'compclaim', 'weaptype1', 'weapsubtype1', 'weaptype2', 'weapsubtype2', 'weaptype3', 'weapsubtype3', 'weaptype4', 'weapsubtype4', 'nkillus', 'nkillter', 'nwoundus', 'nwoundte', 'property', 'propextent', 'propextent_txt', 'propvalue', 'ishostkid', 'nhostkid', 'nhostkidus', 'nhours', 'ndays', 'divert', 'kidhijcountry', 'ransom', 'ransomamt', 'ransomamtus', 'ransompaid', 'ransompaidus', 'hostkidoutcome', 'hostkidoutcome_txt', 'nreleased', 'INT_LOG', 'INT_IDEO', 'INT_MISC', 'INT_ANY'], axis=1, inplace=True)

# rename the columns for easier understanding
df.rename(columns={'iyear':'Year', 'imonth':'Month', 'iday':'Day', 'country_txt':'Country', 'region_txt':'Region', 'city':'City', 'latitude':'Latitude', 'longitude':'Longitude', 'specificity':'Specificity', 'attacktype1_txt':'AttackType', 'targtype1_txt':'TargetType', 'gname':'Group', 'nperps':'NumPerps', 'nperpcap':'NumPerpsCaptured', 'claimed':'Claimed', 'weaptype1_txt':'WeaponType', 'nkill':'NumKilled', 'nwound':'NumWounded', 'summary':'Summary', 'motive':'Motive'}, inplace=True)

# check the top 10 countries with the highest number of attacks
country_attacks = df['Country'].value_counts().head(10)
print(country_attacks)

# plot a countplot to visualize the top 10 countries with the highest number of attacks
sns.countplot(y='Country', data=df, order=country_attacks.index, palette='rocket')
plt.title('Top 10 Countries with Highest Number of Terrorist Attacks')
plt.xlabel('Number of Attacks')
plt.ylabel('Country')
plt.show()
