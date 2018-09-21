import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

""" Geração do gráficos usando nas alaises do Data Set do Titanic editado
oferencido no curso de fundamentos de Data Science I (Udacity).
"""

# Grid para fundo branco.
# sns.set_style("whitegrid")

df_titanic = pd.read_csv('titanic_edited.csv')

# Gráfico de Sobreviventes por classe e categoria de idade.
# Existe um warning nesse gráfico, mas não entendi como resolver.
g1 = sns.catplot(data=df_titanic, x='passenger_class', y='survived',
    kind='bar', hue='age_category')
g1._legend.set_title('Categoria de Idade')
plt.xlabel('Classe')
plt.ylabel('Sobreviventes')
plt.title('Sobreviventes por classe e categoria de idade')
sns.despine(offset=5, trim=True)
g1.savefig('imgs/g1-survived-class-by-age-cotegory.png')

# Gráfico de contagem de passageiros por classe e categoria de idade.
g2 = sns.catplot(data=df_titanic, x='passenger_class',
    kind='count', hue='age_category')
g2._legend.set_title('Categoria de Idade')
plt.xlabel('Classe')
plt.ylabel('Contagem')
plt.title('Contagem por classe e categoria de idade')
sns.despine(offset=5, trim=True)
g2.savefig('imgs/g2-count-class-by-age-cotegory.png')

# Gráfico de caixa de categoria de idade por classe.
g3 = sns.catplot(y="age_category", x="age", row="passenger_class",
                 orient="h", height=2, aspect=4, kind="box",
                 data=df_titanic.query('age_category != "Desconhecido"'))
g3.set_ylabels('Categoria de Idade')
g3.set_xlabels('Idade')
g3.set_titles("{row_name}(a) classe")
sns.despine(offset=5, trim=True)
g3.savefig('imgs/g3-box-class-by-age-cotegory.png')

# Gráfico de contagem de passageiros por classe e gênero.
g4 = sns.catplot(data=df_titanic, x='passenger_class', kind='count', hue='sex')
g4._legend.set_title('Gênero')
plt.xlabel('Classe')
plt.ylabel('Contagem')
plt.title('Contagem de pessoas por classe e gênero')
sns.despine(offset=5, trim=True)
g4.savefig('imgs/g4-count-passengers-class.png')

# Contagem de passageiros por classe.
g5 = sns.catplot(data=df_titanic, x='passenger_class', kind='count')
plt.xlabel('Classe')
plt.ylabel('Contagem')
plt.title('Contagem de passageiros por classe social.')
sns.despine(offset=5, trim=True)
g5.savefig('imgs/g5-count-passenger-class.png')

# Contagem de pessoas por gênero.
g6 = sns.catplot(data=df_titanic, x='sex', kind='count')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.title('Contagem de pessoas por gênero')
sns.despine(offset=5, trim=True)
g6.savefig('imgs/g6-count-people-by-gender.png')

# Contagem de pessoas por categoria de idade.
g7 = sns.catplot(data=df_titanic, x='age_category', kind='count')
plt.xlabel('Categoria de Idade')
plt.ylabel('Contagem')
plt.title('Contagem de pessoas por categoria de idade')
sns.despine(offset=5, trim=True)
g7.savefig('imgs/g7-count-pearson-by-age-category.png')

# Gráfico de caixa entre idade de passageiros adultos e classe social.
f, g8 = plt.subplots(figsize=(6, 6))
sns.boxplot(x="passenger_class", y="age",
            data=df_titanic.query('age_category != "Desconhecido" & age > 18'))
plt.ylabel('Idade')
plt.xlabel('Classe')
plt.title("Idade dos adultos por classe")
sns.despine(offset=5, trim=True);
g8.figure.savefig('imgs/g8-box-adult-age-by-social.png')

# Gráfico de caixa entre classe de passageiros e taxa da passagem.
f, g9 = plt.subplots(figsize=(6, 6))
sns.boxplot(x="passenger_class", y="fare", data=df_titanic)
plt.ylabel('Preço Passagem')
plt.xlabel('Classe')
plt.title("Classe do passageiro por preço da passagem")
sns.despine(offset=5, trim=True)
g9.figure.savefig('imgs/g9-box-class-by-ticket-fare.png')

# Gráfico de barra com local de embarque e classe do passageiro.
g10 = sns.catplot(data=df_titanic, x='passenger_class',
    y='fare', kind='bar', hue='embarked')
g10._legend.set_title('Locais de Embarque')
plt.xlabel('Classe')
plt.ylabel('Tarifa Passagem')
plt.title('Tarifa da passagem por local de embarque e classe social.')
sns.despine(offset=5, trim=True)
g10.savefig('imgs/g10-bar-embarked-by-class.png')

# Histograma idade por classe social
# Gráfico de primeira classe.
f, g11 = plt.subplots(figsize=(6, 6))
sns.distplot(df_titanic.query(
    'passenger_class == 1')['age'].astype(int), kde=False,
    hist_kws=dict(edgecolor="k", linewidth=2))
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Frequência de passageiros da primeira classe por idade')
g11.set_xticks(np.arange(0, 80, 5), minor=True)
sns.despine(ax=g11, offset=5, trim=True)
g11.figure.savefig('imgs/g11-hist-age-first-class.png')

# Gráfico de segunda classe.
f, g12 = plt.subplots(figsize=(6, 6))
sns.distplot(df_titanic.query(
    'passenger_class == 2')['age'].astype(int), kde=False,
    label='age_category', hist_kws=dict(edgecolor="k", linewidth=2))
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Frequência de passageiros da segunda classe por idade')
g12.set_xticks(np.arange(0, 70, 5), minor=True)
sns.despine(ax=g12, offset=5, trim=True)
g12.figure.savefig('imgs/g12-hist-age-second-class.png')

# Gráfico de terceira classe.
f, g13 = plt.subplots(figsize=(6, 6))
sns.distplot(df_titanic.query(
    'passenger_class == 3')['age'].astype(int), kde=False,
    label='age_category', hist_kws=dict(edgecolor="k", linewidth=2))
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Frequência de passageiros da terceira classe por idade')
g13.set_xticks(np.arange(0, 85, 5), minor=True)
sns.despine(ax=g13, offset=5, trim=True)
g13.figure.savefig('imgs/g13-hist-age-third-class.png')