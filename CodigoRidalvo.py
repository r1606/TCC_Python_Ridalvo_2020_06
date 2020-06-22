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
bars = ('101 - ANESTESIOLOGIA','102 - ANESTESIOLOGIA','103 - AREA CIRURGICA BÁSICA','104 - CARDIOLOGIA','105 - CIRURGIA DO APARELHO DIGESTIVO','106 - CIRURGIA GERAL','107 - CIRURGIA VIDEOLAPAROSCÓPICA','108 - CLÍNICA MÉDICA','109 - DERMATOLOGIA','110 - ENDOCRINOLOGIA E METEBOLOGIA','111 - ENDOCRINOLOGIA PEDIÁTRICA','112 - ENDOSCOPIA DIGESTIVA','113 - ENDOSCOPIA GINECOLÓGICA','114 - GASTROENTEROLOGIA','115 - GASTROENTEROLOGIA PEDIÁTRICA','116 - GINECOLOGIA E OBSTETRÍCIA','117 - GINECOLOGIA E OBSTETRÍCIA','118 - INFECTOLOGIA','119 - MEDICINA DE FAMÍLIA E COMUNIDADE','120 - MEDICINA DE FAMÍLIA E COMUNIDADE','121 - MEDICINA INTENSIVA','122 - NEFROLOGIA','123 - NEONATOLOGIA','124 - NEUROCIRURGIA','125 - NEUROLOGIA','126 - OFTALMOLOGIA','127 - OTORRINOLARINGOLOGIA','128 - PATOLOGIA','129 - PEDIATRIA','130 - PEDIATRIA','131 - PSIQUIATRIA','132 - RADIOLOGIA','133 - REUMATOLOGIA','134 - UROLOGIA')

### Quantidades de candidatos de cada programa
height = [45,28,38,11,10,44,4,102,22,5,1,5,4,12,2,10,56,7,14,8,3,7,5,14,9,36,23,11,50,8,45,21,3,16] 

y_pos = np.arange(len(bars))
 
#################################################
# Formatação do gráfico 
#################################################

plt.title('Distribuição dos candidatos do processo seletivo para a Residência Médica') ### Título do gráfico
plt.xticks(y_pos, bars) ### Título do eixo horizontal


#Criar barras
plt.bar(y_pos, height)
 
 
# Rotação dos nomes das barras
plt.xticks(y_pos, bars, rotation=90)
 
# Personalizar o layout da subtrama
plt.subplots_adjust(bottom=0.4, top=0.99)

#Cores 
plt.bar(y_pos, height, color=[ 'red', 'green', 'red', 'red', 'red',  'blue', 'green', 'green', 'red', 'blue', 'green', 'green', 'yellow', 'green', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'yellow', 'red', 'yellow', 'yellow', 'green', 'blue', 'blue', 'yellow', 'yellow', 'yellow', 'red', 'yellow', 'yellow', 'blue',  'blue',  'blue',  'blue', 'Red',  'blue' ])
plt.xticks(y_pos, bars)
plt.show()

# Mostrar gráfico
#plt.show()

#"""**Gráfico Separado por Zona**"""

# Importa biblioteca
#import numpy as np
#import matplotlib.pyplot as plt
 
 # Titulo 
#plt.title('Ranking dos casos confirmados de Covid-19  separado por zona')

# Crie um conjunto de dados 
#height = [32.19, 31.85, 21.22, 14.7]
#bars = ('Zona Norte', 'Zona Sul', 'Zona Leste', 'Zona Oeste')
#y_pos = np.arange(len(bars))

# Separa as zonas por cores 
#plt.bar(y_pos, height, color=['red', 'green', 'blue', 'yellow'])
#plt.xticks(y_pos, bars)
#plt.show()

#"""**Os 5 bairros com mais casos confrimados de Covid-19**"""

# Importa biblioteca
#import numpy as np
#import matplotlib.pyplot as plt
 
 # Titulo 
#plt.title('Ranking dos  5 bairros com mais casos confirmados de Covid-19' )


# Crie um conjunto de dados 
#height = [11.30, 8.22, 7.88, 6.51, 6.16]
#bars = ('Potengi', 'Lagoa Nova', 'Nossa Senhora da Apresentação', 'Pajuçara', 'Tirol')
#y_pos = np.arange(len(bars))

# Rotação dos nomes das barras
#plt.xticks(y_pos, bars, rotation=90)
 
# Personalizar o layout da subtrama
#plt.subplots_adjust(bottom=0.4, top=0.99)

# Separa as zonas por cores 
#plt.bar(y_pos, height, color=['red', 'green', 'red', 'red','red'])
#plt.xticks(y_pos, bars)
#plt.show()
