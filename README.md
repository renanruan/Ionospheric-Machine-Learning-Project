# PO-233

### Ideia Inicial
O **Gradiente Espacial** é um fenômeno ionesférico relacionado ao cálculo de diversos parâmetros na comunicação via satélite. Para a manutenção da precisão de comunicação é importante identificar quando alterações no **Gradiente Espacial** podem impactar significativamente os parâmetros. 

O objetivo deste projeto é classificar quando essa alteração do **Gradiente Espacial** é relevante ou não a partir de dados da ionosfera e da posição relativa de satélites.

***Cintilação***, ***Bolhas de Plasma Equatorial*** e a ***Posição Relativa do Satélite*** são atributos canditos para serem utilizados na classificação, pois eles podem influenciar o **Gradiente Espacial**. 

### Atributo Meta
Este fenômeno pode ser identificado através do valor absoluto dos parâmetros: 
- (id94) Grand HANTS dt0
- (id95) Grand HANTS dt15
- (id96) Grand HANTS dt30
- (id97) Grand HANTS dt45

Através da classificação:
- abs(HANTS) < 400 → Fenômeno não está ocorrendo
- abs(HANTS) > 400 → Fenômeno está ocorrendo

### Atributos Candidatos
Possíveis candidatos de parâmetros relevantes para teste:
- (id77) Alpha : Orientação de propagação do sinal em relação a bolha de plasma no eixo horizontal
- (id78) Gamma : Orientação de propagação do sinal em relação a bolha de plasma no eixo vertical
- (id16) Phi60l1 : 
- (id10) S4 : Indice de Amplitude da Cintilação

### Principais Informações do Artigo
- ∇I : Atraso do Gradiente Ionosférico
- S4 : Indice de Amplitude da Cintilação
    - S4 < 0.3 : Não há ocorrência de Cintilação
    - S4 >= 0.3 : Indicação de ocorrência de Cintilação
    - S4 >= 0.7 : Indicação de ocorrência de forte Sitilação
- HANTS : Algoritmo de superposição utilizado para preencher lacunas de medições que não foram possíveis de realizar
    - abs(HANTS) < 400 : Fenômeno não está ocorrendo
    - abs(HANTS) > 400 : Fenômeno está ocorrendo
- SJCE : Estação de medida primária em São José dos Campos
- SJCU : Estação de medida secundária

### Estrutura do Projeto
├─> Raw Data: Base de dados utilizada na produção do artigo
<br>├─> Filtered Data: Base de dados após o tratamento
<br>├─> Machine Learning: Arquivos relacionados ao aprendizado de máquina
<br>└─> Articles: Pasta com os artigos relacionados à base de dados. Ela foi usada primeiramente o artigo "Strong Ionospheric..."

### Passo-a-Passo
#### **1. Tratamento de Dados**
~~1.1. Identificar em quais arquivos estão os dados relevantes~~
<br>~~1.2. Criar um algoritmo para extrair os dados do .mat e salvá-los em .csv~~
<br>~~1.3. Remover atributos não necessários~~
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


