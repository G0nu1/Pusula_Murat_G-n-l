'''Filling in Missing Data'''
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer

df = pd.read_excel('C:\\Users\\mrtgn\\Desktop\\pusula\\Pusula_Murat_Gönül\\SED.xlsx')

current_year = datetime.now().year
df['Age'] = current_year - pd.to_datetime(df['Dogum_Tarihi']).dt.year


cinsiyet_oranlari = df['Cinsiyet'].value_counts(normalize=True)
df['Cinsiyet'] = df['Cinsiyet'].apply(lambda x: np.random.choice(cinsiyet_oranlari.index, p=cinsiyet_oranlari) if pd.isnull(x) else x)


sehir_oranlari = df['Il'].value_counts(normalize=True)
df['Il'] = df['Il'].apply(lambda x: np.random.choice(sehir_oranlari.index, p=sehir_oranlari) if pd.isnull(x) else x)


le_cinsiyet = LabelEncoder()
df['Cinsiyet'] = le_cinsiyet.fit_transform(df['Cinsiyet'])

le_il = LabelEncoder()
df['Il'] = le_il.fit_transform(df['Il'])

imputer = KNNImputer(n_neighbors=5)

# apply KNN
df[['Cinsiyet', 'Il', 'Age', 'Kilo', 'Boy']] = imputer.fit_transform(df[['Cinsiyet', 'Il', 'Age', 'Kilo', 'Boy']])

# apply label encoder
le_Kangrubu = LabelEncoder()
df['Kan Grubu'] = le_Kangrubu.fit_transform(df['Kan Grubu'].astype(str))

df['Alerjilerim'] = df['Alerjilerim'].fillna('Yok')
df['Kronik Hastaliklarim'] = df['Kronik Hastaliklarim'].fillna('Yok')
df['Baba Kronik Hastaliklari'] = df['Baba Kronik Hastaliklari'].fillna('Yok')
df['Anne Kronik Hastaliklari'] = df['Anne Kronik Hastaliklari'].fillna('Yok')
df['Kiz Kardes Kronik Hastaliklari'] = df['Kiz Kardes Kronik Hastaliklari'].fillna('Yok')
df['Erkek Kardes Kronik Hastaliklari'] = df['Erkek Kardes Kronik Hastaliklari'].fillna('Yok')

le = LabelEncoder()
df['Alerjilerim'] = le.fit_transform(df['Alerjilerim'])
df['Kronik Hastaliklarim'] = le.fit_transform(df['Kronik Hastaliklarim'])
df['Baba Kronik Hastaliklari'] = le.fit_transform(df['Baba Kronik Hastaliklari'])
df['Anne Kronik Hastaliklari'] = le.fit_transform(df['Anne Kronik Hastaliklari'])
df['Kiz Kardes Kronik Hastaliklari'] = le.fit_transform(df['Kiz Kardes Kronik Hastaliklari'])
df['Erkek Kardes Kronik Hastaliklari'] = le.fit_transform(df['Erkek Kardes Kronik Hastaliklari'])


df[['Alerjilerim', 'Kronik Hastaliklarim', 'Baba Kronik Hastaliklari', 'Anne Kronik Hastaliklari', 'Kiz Kardes Kronik Hastaliklari', 'Erkek Kardes Kronik Hastaliklari', 'Kan Grubu']] = imputer.fit_transform(df[['Alerjilerim', 'Kronik Hastaliklarim', 'Baba Kronik Hastaliklari', 'Anne Kronik Hastaliklari', 'Kiz Kardes Kronik Hastaliklari', 'Erkek Kardes Kronik Hastaliklari', 'Kan Grubu']])


# Create a summary DataFrame
summary_df = pd.DataFrame({
    'Data Type': df.dtypes,
    'Variety Count': df.nunique(),
    'Data Count': df.count(),
    'Missing Count': df.isnull().sum(),
    'Missing Percentage': (df.isnull().sum() / len(df)) * 100
})

df.to_excel('fill_data.xlsx', index=False)
print(summary_df)
