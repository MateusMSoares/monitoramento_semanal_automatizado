import pandas as pd
import numpy as np

x = pd.read_excel(r'C:\Users\mateu\Desktop\Exercicios programação\Python\Projetos\Automatizando planilhas\disponibilidade.xls')
#Retira linhas com NaN(Vazias)
#x = x.dropna()
#Retira as colunas não nomedas, visto que tem colunas mescladas
#x = x.loc[:,~x.columns.str.contains('^Unnamed')]
print (x)