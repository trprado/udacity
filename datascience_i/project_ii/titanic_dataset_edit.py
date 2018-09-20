import numpy as np
import pandas as pd

""" Transformação do Data Set do Titanic oferencido no curso de fundamentos de
Data Science I (Udacity).
"""
df_titanic = pd.read_csv('titanic-data-6.csv')

# print(df_titanic.head(1))
# print(df_titanic.info())
# print(df_titanic_novo.nunique())

# Coluna de id de passageiros removida, pois é igual ao index.
# Cabines não tem importancia, então estão sendo removidas.
# Nome está sendo mantido apenas para estudo de parentesco, ao se agrupar os 
# tickets retornar
# o nome das pessoas que possuem mesmo valor, assim é possível estudar se os 
# passageiros tinham
# relações de parentesco ou possívelmente trabalho.
df_titanic.drop(columns=['PassengerId', 'Cabin'], inplace=True)

# Renomeia Pclass para Passenger Class.
df_titanic.rename(columns={'Pclass':'Passenger Class'}, inplace=True)

# Renomeia colunas.
df_titanic.rename(
    columns=lambda x: x.strip().lower().replace(' ', '_'), inplace=True)

# df_titanic.columns

# Cria nova coluna com categoria de idade.
# 
df_criancas = df_titanic.query('age <= 12').copy()
df_adolescente = df_titanic.query('12 < age <= 18').copy()
df_adulto = df_titanic.query('age > 18').copy()
df_sem_idade = df_titanic[df_titanic['age'].isnull()].copy()

idade_crianca = np.repeat('Criança', df_criancas.shape[0])
idade_adolescente = np.repeat('Adolescente', df_adolescente.shape[0])
idade_adulto = np.repeat('Adulto', df_adulto.shape[0])
idade_desconhecido = np.repeat('Desconhecido', df_sem_idade.shape[0])

df_criancas['age_category'] = idade_crianca
df_adolescente['age_category'] = idade_adolescente
df_adulto['age_category'] = idade_adulto
df_sem_idade['age_category'] = idade_desconhecido

df_titanic_edited = df_criancas.append(
    [df_adolescente, df_adulto, df_sem_idade])
df_titanic_edited.sort_index(inplace=True)

# Idade das pessoas esta sendo removido ao fazer o calculo, como não é possível 
# definir se a pessoa se encontra entre um
# grupo de idade para realizar a média, foi preferido não colocar a media das 
# idades a esses indivíduos.
# Local de embarque esta sendo removido os nulos para calculos, pois como são 
# letras, não é possível ter uma média.
# Ambos teriam de ser utilizados modelos de predição para um valor mais próximo 
# do correto.

df_titanic_edited.to_csv('titanic_edited.csv', index=False)