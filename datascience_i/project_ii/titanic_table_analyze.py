import numpy as np
import pandas as pd

""" Geração de tabelas e outros elementos usando do Data Set do Titanic editado
oferencido no curso de fundamentos de Data Science I (Udacity).
"""

# Algumas analises não foram feitas devido ao banco de dados ser cortado, onde
# poderiamos verificar as informação familiares pelas colunas SibSp e Parch,
# existem informações de pessoas com acompanhantes mas não existem estes acompa-
# nhantes no banco de dados.

# Formata os ponto flutuantes para quatro casas decimais.
pd.set_option('display.float_format', '{:.4f}'.format)

df_titanic = pd.read_csv('titanic_edited.csv')

# Cabeçalho.
print(df_titanic.head(5))

# Nomes das colunas.
print('Colunas: ', *(x for x in df_titanic.columns[1:]), sep=' | ')
print()

# Tabela 1: Passageiros por classe social, total de indivíduos por categoria de
# idade e sobreviventes da categoria.
df_1 = df_titanic.query('survived == 1').groupby(
    ['passenger_class', 'age_category'])['survived'].count().reset_index()
class_sum = df_1['survived'].sum()
df_1.loc['total'] = np.array(['-','-',class_sum])
df_1['survived'] = df_1['survived'].astype(int)
df_1.to_csv('tables/t_1.csv', index=False)
print('Tabela1: Passageiros por classe social, total de indivíduos por categoria de idade e sobreviventes da categoria.')
print(df_1, '\n')

# Tabela 2: Passageiros por classe, total de indivíduos por sexo e
# sobrevivementes da categoria.
df_2 = df_titanic.groupby(['passenger_class', 'sex']).agg(
    {'name':'count', 'survived':'sum'}).rename(
    columns={'name':'total'})
df_2.to_csv('tables/t_2.csv')
print('Tabela 2: Passageiros por classe com total de indivíduos por classe e sobreviventes.')
print(df_2, '\n')

# Tablea 3: Contagem de passageiros por classe e sobreviventes.
df_3 = df_titanic.groupby('passenger_class').agg(
    {'name':'count', 'survived': 'sum'}).rename(
    columns={'name':'total'})
df_3.to_csv('tables/t_3.csv')
print('Tabela 3: Total de passageiros por classe e sobreviventes.')
print(df_3, '\n')

# Tabela 4: Total de indivíduos por gênero e sobreviventes.
df_4 = df_titanic.groupby('sex').agg(
    {'name':'count', 'survived':'sum'}).rename(columns={'name':'total'})
df_4.to_csv('tables/t_4.csv')
print('Tabela 4: Total de indivíduos por gênero e sobreviventes.')
print(df_4, '\n')

# Tabela 5: Contagem de pessoas por categoria de idade e sobreviventes.
df_5 = df_titanic.groupby('age_category').agg(
    {'name':'count', 'survived':'sum'}).rename(columns={'name':'total'})
df_5.to_csv('tables/t_5.csv')
print('Tabela 5: Contagem de pessoas por categoria de idade e sobreviventes.')
print(df_5, '\n')

# Tabela 6: Média da idade dos passageiros por categoria.
df_6 = df_titanic.groupby('age_category')['age'].mean().dropna()
df_6.to_csv('tables/t_6.csv')
print('Tabela 6: Média da idade dos passageiros por categoria.')
print(df_6, '\n')

# Tabela 7: Descritiva da categoria de idade dos passageiros.
df_7 = df_titanic.groupby('age_category')['age'].describe().dropna()
df_7.to_csv('tables/t_7.csv')
print('Tabela 7: Descritiva da categoria de idade dos passageiros.')
print(df_7, '\n')

# Tabela 8: Descritiva da categoria de idade dos passageiros por classe.
df_8 = df_titanic.groupby(
    ['age_category', 'passenger_class'])['age'].describe().dropna()
df_8.to_csv('tables/t_8.csv')
print('Tabela 8: Descritiva da categoria de idade dos passageiros por classe.')
print(df_8, '\n')

# Contagem de sobreviventes por classe.
df_total_survived = df_titanic.query(
    'survived == 1').groupby('passenger_class')['survived'].count()
df_total_survived.loc['total'] = df_total_survived.sum()
print('Contagem de sobreviventes por classe.')
print(df_total_survived, '\n')

# Totais das classes.
df_class_total = df_titanic.groupby('passenger_class').count()
df_class_total.loc['total'] = df_class_total.sum()
print('Totais das classes.')
print(df_class_total, '\n')

# Total de passageiros por classe.
print('Total de passageiros por classe:')
for n in range(1,4):
    print('Total de pessoas da {}(a) classe no titanic: {}.'.format(
        n, df_class_total.loc[n]['survived']))

print('Total de sobreviventes: {}.'.format(
    df_class_total.loc['total']['survived']), '\n')

# Porcentagem de sobreviventes por classe.
print('Porcentagem de sobreviventes por classe:')
for n in range(1,4):
    print('Porcentagem de sobreviventes da {}(a) classe: {:.2%}.'.format(n,
        df_total_survived.loc[n] / df_class_total.loc[n]['survived']))
print('Porcentagem de sobreviventes do naufrágio: {:.2%}.'.format(
    df_total_survived.loc['total'] / df_class_total.loc['total']['survived']), '\n')

# Porcentagem por classes de sobreviventes.
print('Porcentagem por classes de sobreviventes:')
for n in range(1,4):
    print('Porcentagem da {}(a) classe: {:.2%}.'
    .format(n, df_total_survived.loc[n]/df_total_survived.loc['total']))

print('Total de sobreviventes: {}.'.format(
    df_total_survived.loc['total']), '\n')

# Descritiva do valores de todas as passagens, incluindo outliers.
print('Descritiva do valores de todas as passagens, incluindo outliers:')
print(df_titanic['fare'].dropna().describe(), '\n')

# Descritiva dos valores de todas as passagens excluindo passagens com valor
# zero.
temp = df_titanic.query('fare != 0')
print('Descritiva dos valores de todas as passagens excluindo passagens com valor zero:')
print(temp['fare'].dropna().describe(), '\n')

# Descritiva de passageiros por passagem.
df_group = df_titanic.groupby(['ticket', 'passenger_class'])
# df_group.apply(lambda x: x.head()).head(20)
print('Descritiva de passageiros por passagem:')
print(df_group['name'].count().describe(), '\n')

# Passagens com maior número de passageiros da primeira classe.
df_titanic['freq'] = df_titanic.groupby('ticket')['ticket'].transform('count')
print('Passagens com maior número de passageiros da primeira classe:')
df_titanic_most_pc = df_titanic.sort_values(by=['freq', 'ticket'], ascending=False).query(
    'passenger_class == 1').head(10)
df_titanic_most_pc.to_csv('tables/t_10.csv', index=False)
print(df_titanic_most_pc, '\n')

# Passagens com maior número de passageiros da segunda classe.
df_titanic['freq'] = df_titanic.groupby('ticket')['ticket'].transform('count')
print('Passagens com maior número de passageiros da segunda classe:')
df_titanic_most_sc = df_titanic.sort_values(by=['freq', 'ticket'], ascending=False).query(
    'passenger_class == 2').head(10)
df_titanic_most_sc.to_csv('tables/t_11.csv', index=False)
print(df_titanic_most_sc, '\n')

# Passagens com maior número de passageiros da terceira classe.
df_titanic['freq'] = df_titanic.groupby('ticket')['ticket'].transform('count')
print('Passagens com maior número de passageiros da terceira classe:')
df_titanic_most_tc = df_titanic.sort_values(by=['freq', 'ticket'], ascending=False).query(
    'passenger_class == 3').head(10)
df_titanic_most_tc.to_csv('tables/t_12.csv', index=False)
print(df_titanic_most_tc, '\n')

# Descritiva da primeira classe.
df_group_first_class = df_titanic.query(
    'passenger_class == 1 & 20 < fare < 200').groupby(
    ['ticket','passenger_class'])
print('Descritiva da primeira classe:')
print(df_group_first_class.mean().describe(), '\n')

# Descritiva da segunda classe.
df_group_first_class = df_titanic.query(
    'passenger_class == 2 & 5 < fare < 100').groupby(
    ['ticket','passenger_class'])
print('Descritiva da segunda classe:')
print(df_group_first_class.mean().describe(), '\n')

# Descritiva da terceira classe.
df_group_first_class = df_titanic.query(
    'passenger_class == 3 & 4 < fare < 100').groupby(
    ['ticket','passenger_class'])
print('Descritiva da terceira classe:')
print(df_group_first_class.mean().describe(), '\n')

# Descritiva do custo da passagem na primeira classe
print('Descritiva do custo da passagem na x classe:')
print(df_titanic.query(
    'passenger_class == 3')['fare'].dropna().describe(), '\n')

# Descritiva do custo da passagem na segunda classe
print('Descritiva do custo da passagem na x classe:')
print(df_titanic.query(
    'passenger_class == 3')['fare'].dropna().describe(), '\n')

# Descritiva do custo da passagem na terceira classe
print('Descritiva do custo da passagem na x classe:')
print(df_titanic.query(
    'passenger_class == 3')['fare'].dropna().describe(), '\n')

# Tabela 9: Média de valor da passagem por local de embarque e sua classe.
df_9 = df_titanic.groupby(['passenger_class', 'embarked']).agg(
    {'fare':'mean', 'name':'count'}).rename(
    columns={'fare':'fare_mean','name':'total'})
df_9.to_csv('tables/t_9.csv')
print('Tabela 9: Média de valor da passagem por local de embarque e sua classe:')
print(df_9, '\n')