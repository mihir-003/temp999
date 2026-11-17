import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('D:\\ML-R\\temp\\covid_toy.csv')

print(df.head(3))

le = LabelEncoder()

df['gender'] = le.fit_transform(df['gender'])
print(df['gender'])

print(df.head(3))
