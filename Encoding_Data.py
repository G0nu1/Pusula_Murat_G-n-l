"""**Encoding Data**"""

from sklearn.preprocessing import LabelEncoder
from datetime import datetime
import pandas as pd


df = pd.read_excel('C:\\Users\\mrtgn\\Desktop\\pusula\\Pusula_Murat_Gönül\\side_effect_data.xlsx')

le = LabelEncoder()

df['Cinsiyet'] = le.fit_transform(df['Cinsiyet'])
df['Uyruk'] = le.fit_transform(df['Uyruk'])
df['Il'] = le.fit_transform(df['Il'])
df['Alerjilerim'] = le.fit_transform(df['Alerjilerim'])
df['Kronik Hastaliklarim'] = le.fit_transform(df['Kronik Hastaliklarim'])
df['Baba Kronik Hastaliklari'] = le.fit_transform(df['Baba Kronik Hastaliklari'])
df['Anne Kronik Hastaliklari'] = le.fit_transform(df['Anne Kronik Hastaliklari'])
df['Kiz Kardes Kronik Hastaliklari'] = le.fit_transform(df['Kiz Kardes Kronik Hastaliklari'])
df['Erkek Kardes Kronik Hastaliklari'] = le.fit_transform(df['Erkek Kardes Kronik Hastaliklari'])
df['Kan Grubu'] = le.fit_transform(df['Kan Grubu'])
df['Ilac_Adi'] = le.fit_transform(df['Ilac_Adi'])
df['Yan_Etki'] = le.fit_transform(df['Yan_Etki'])

# Create new columns
today = datetime.today()
df['Age'] = df['Dogum_Tarihi'].apply(lambda x: today.year - x.year - ((today.month, today.day) < (x.month, x.day)))

df['Ilac_Suresi'] = (df['Ilac_Bitis_Tarihi'] - df['Ilac_Baslangic_Tarihi']).dt.days

df['Ilac_Baslangic_Tarihi'] = pd.to_datetime(df['Ilac_Baslangic_Tarihi'])
df['Yan_Etki_Bildirim_Tarihi'] = pd.to_datetime(df['Yan_Etki_Bildirim_Tarihi'])

df['Yan_Etki_Ortaya_Cikma_Suresi'] = (df['Yan_Etki_Bildirim_Tarihi'] - df['Ilac_Baslangic_Tarihi']).dt.days

df.loc[df['Yan_Etki_Ortaya_Cikma_Suresi'] < 0, 'Yan_Etki_Ortaya_Cikma_Suresi'] = None


# Delete unrequired columns
df = df.drop(['Ilac_Baslangic_Tarihi',	'Ilac_Bitis_Tarihi',	'Yan_Etki_Bildirim_Tarihi'], axis=1)


# Create a summary DataFrame
summary_df = pd.DataFrame({
    'Data Type': df.dtypes,
    'Variety Count': df.nunique(),
    'Data Count': df.count(),
    'Missing Count': df.isnull().sum(),
    'Missing Percentage': (df.isnull().sum() / len(df)) * 100
})

df.to_excel('Encoding_Data.xlsx', index=False)
print(summary_df)