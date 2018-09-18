import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Algumas configurações visuais do seaborn.
sns.set_style("whitegrid")

df_titanic = pd.read_csv('titanic-data-6.csv')

# 10 primeiros itens do dataset.
df_titanic.head(10)

# pd.plotting.scatter_matrix(df_titanic, figsize=(15,15))
sns.pairplot(df_titanic)
sns.despine(left=True)

idade_crianca = np.repeat('Criança', df_titanic.shape[0])
df_criancas = df_titanic.query('Age <= 12')
df_adolescente = df_titanic.query('12 > Age <= 18')  