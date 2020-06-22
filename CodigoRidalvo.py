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

df = pd.read_csv('ResMed.csv')
df


height = [11.30, 8.22, 7.88, 6.51, 6.16, 5.48, 5.14, 4.79, 4.45, 4.45, 4.11, 3.42, 3.42, 3.42, 3.08, 2.74, 2.40, 1.71, 1.37, 1.37, 1.37, 1.37, 1.03, 1.03, 0.68, 0.68, 0.68, 0.68, 0.34, 0.34, 0.34, 0, 0, 0, 0, 0]
bars = ('Potengi', 'Lagoa Nova', 'Nossa Senhora da Apresentação', 'Pajuçara', 'Tirol', 'Ponta Negra', 'Pitimbú', 'Lagoa Azul', 'Petrópolis', 'Capim Macio', 'Candelária', 'Quintas', 'Neópolis', 'Alecrim', 'Felipe Camarão', 'Barro Vermelho', 'Cidade Alta', 'Dix-Sepr Rosado', 'Planalto','Igapó', 'Cidade da Esperança','Bom Pastor', 'Nova Descoberta', 'Areia Preta', 'Rocas','Nordeste', 'Guarapes', 'Cidade Nova', 'Redinha', 'Nossa Senhora de Nazaré ', 'Lagoa Seca', 'Mãe Luiza', 'Praia do Meio', 'Ribeira', 'Salinas', 'Santos Reis')
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
plt.show()

"""**Gráfico Separado por Zona**"""

# Importa biblioteca
import numpy as np
import matplotlib.pyplot as plt
 
 # Titulo 
plt.title('Ranking dos casos confirmados de Covid-19  separado por zona')


# Crie um conjunto de dados 
height = [32.19, 31.85, 21.22, 14.7]
bars = ('Zona Norte', 'Zona Sul', 'Zona Leste', 'Zona Oeste')
y_pos = np.arange(len(bars))

# Separa as zonas por cores 
plt.bar(y_pos, height, color=['red', 'green', 'blue', 'yellow'])
plt.xticks(y_pos, bars)
plt.show()

"""**Os 5 bairros com mais casos confrimados de Covid-19**"""

# Importa biblioteca
import numpy as np
import matplotlib.pyplot as plt
 
 # Titulo 
plt.title('Ranking dos  5 bairros com mais casos confirmados de Covid-19' )


# Crie um conjunto de dados 
height = [11.30, 8.22, 7.88, 6.51, 6.16]
bars = ('Potengi', 'Lagoa Nova', 'Nossa Senhora da Apresentação', 'Pajuçara', 'Tirol')
y_pos = np.arange(len(bars))

# Rotação dos nomes das barras
plt.xticks(y_pos, bars, rotation=90)
 
# Personalizar o layout da subtrama
plt.subplots_adjust(bottom=0.4, top=0.99)

# Separa as zonas por cores 
plt.bar(y_pos, height, color=['red', 'green', 'red', 'red','red'])
plt.xticks(y_pos, bars)
plt.show()
