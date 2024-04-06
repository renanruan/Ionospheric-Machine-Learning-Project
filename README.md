# PO-233

### Ideia Inicial
O **Gradiente Espacial** é uma parte importante da comunicação via satélite e está envolvido com diversos parâmentros de comunicação. 
***Cintilação***, ***Bolhas de Plasma Equatorial*** e a ***Posição Relativa do Satélite*** são capazes de alterar o **Gradiente Espacial**, por isso é importante para um satélite identificar quando essa alteração se torna relevante para seus parâmetros de comunicação. O objetivo deste projeto é classificar quando esse fenômeno é relevante ou não a partir de dados da ionosfera e da posição relativa de satélites.

### Classificação
Este fenômeno pode ser identificado através do valor absoluto do parâmetro HANTS:
- abs(HANTS) < 400 → Fenômeno não está ocorrendo
- abs(HANTS) > 400 → Fenômeno está ocorrendo

### Hipótese
Através de um algoritmo de classificação, pretendemos utilizar um conjunto de parâmetros relevantes para classificar se o fenômeno está ocorrendo.

### Parâmetros Relevantes
Possíveis candidatos de parâmetros relevantes para teste:
- alpha
- gamma
- phi (e variações)
- s4 (e variações)

### Estrutura do Projeto
├─> Raw Data: Base de dados utilizada na produção do artigo
<br>├─> Filtered Data: Base de dados após o tratamento
<br>├─> Machine Learning: Arquivos relacionados ao aprendizado de máquina
<br>└─> Articles: Pasta com os artigos relacionados à base de dados. Ela foi usada primeiramente o artigo "Strong Ionospheric..."


### Passo-a-Passo
#### **1. Tratamento de Dados**
1.1. Identificar em quais arquivos estão os dados relevantes
<br>1.2. Criar um algoritmo para extrair os dados do .mat e salvá-los em .csv
<br>1.3. Remover atributos não necessários
<br>1.4. Alterar o valor do atributo HANTS de contínuo para discreto 
<br>1.5. Aplicar outros métodos de tratamento conforme orientações da professora
#### **2. Criação do Algoritmo de Aprendizado de Máquina**
2.1. Estudar algoritmos de classificação capazes de trabalhar sobre uma base de dados temporal
<br>2.2. Desenvolver o algoritmo
#### **3. Aprendizado de Máquina**
3.1. Definir de que forma serão realizados os testes
<br>3.2. Separar os arquivos de teste
#### **4. Escrita do Artigo**
4.1. Estudar o padrão do artigo indicado pela professora
<br>4.2. Escrever a Conclusão


### Principais Informações do Artigo
- S4 -> Indice de Amplitude da Sintilação
- HANTS -> Algoritmo de superposição utilizado para preencher lacunas de medições que não foram possíveis de realizar
- SJCE -> Estação de medida primária em São José dos Campos
- SJCU -> Estação de medida secundária