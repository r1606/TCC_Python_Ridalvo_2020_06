#################################################
# Introdução à Programação com Python	
# Professor: Carlos Artur Guimarães
# Aluno: Ridalvo Medeiros Alves de Oliveira
#################################################

#################################################
# Importações do NUNPY, do PANDAS e do MATPOTLIB 
#################################################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#################################################
# Carga do arquivo de dados ResMed.csv 
#################################################

# df = pd.read_csv('ResMed.csv')
# df

### Programas da Residência Médica
programas = ('101 - ANESTESIOLOGIA','102 - ANESTESIOLOGIA','103 - AREA CIRURGICA BÁSICA','104 - CARDIOLOGIA','105 - CIRURGIA DO APARELHO DIGESTIVO','106 - CIRURGIA GERAL','107 - CIRURGIA VIDEOLAPAROSCÓPICA','108 - CLÍNICA MÉDICA','109 - DERMATOLOGIA','110 - ENDOCRINOLOGIA E METEBOLOGIA','111 - ENDOCRINOLOGIA PEDIÁTRICA','112 - ENDOSCOPIA DIGESTIVA','113 - ENDOSCOPIA GINECOLÓGICA','114 - GASTROENTEROLOGIA','115 - GASTROENTEROLOGIA PEDIÁTRICA','116 - GINECOLOGIA E OBSTETRÍCIA','117 - GINECOLOGIA E OBSTETRÍCIA','118 - INFECTOLOGIA','119 - MEDICINA DE FAMÍLIA E COMUNIDADE','120 - MEDICINA DE FAMÍLIA E COMUNIDADE','121 - MEDICINA INTENSIVA','122 - NEFROLOGIA','123 - NEONATOLOGIA','124 - NEUROCIRURGIA','125 - NEUROLOGIA','126 - OFTALMOLOGIA','127 - OTORRINOLARINGOLOGIA','128 - PATOLOGIA','129 - PEDIATRIA','130 - PEDIATRIA','131 - PSIQUIATRIA','132 - RADIOLOGIA','133 - REUMATOLOGIA','134 - UROLOGIA')

### Quantidades de candidatos de cada programa
qtcand = [45,28,38,11,10,44,4,102,22,5,1,5,4,12,2,10,56,7,14,8,3,7,5,14,9,36,23,11,50,8,45,21,3,16] 

#################################################
# Formatação do gráfico 
#################################################

### Título do gráfico
plt.title('UFRN/COMPERVE \n Distribuição dos candidatos do processo seletivo para a Residência Médica 2020 \n Por ordem de código de programa') 

### Título do eixo vertical
plt.ylabel('Quant. de candidatos')

### Título do eixo horizontal
plt.xlabel('Programas') 

# Monta a lista de programas no eixo horizontal
pos_prog = np.arange(len(programas))
plt.xticks(pos_prog, programas) 

# Rotaciona os nomes das barras em 90 graus
plt.xticks(pos_prog, programas, rotation=90)

#Cria as barras do gráfico com as quantidades de candidatos, na sequência dos programas
plt.bar(pos_prog, qtcand, width=0.3)
  
# Define a cor das barras como sendo verde
plt.bar(pos_prog, qtcand, color=['green'])

# Exibe o gráfico de barras
plt.show()
