# Aprendizado de máquina como ferramenta de aprimoramento da Navegação Aérea em baixas latitudes

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



### Estrutura do Projeto
├─> Articles: Pasta com os artigos relacionados à base de dados. Ela foi usada primeiramente o artigo "Strong Ionospheric...". Outros artigos relevantes podem ser adicionados.
 Raw Data: Base de dados utilizada na produção do artigo
<br>├─> Data: Base de dados utilizada e os algoritmos de tratamento.
<br>├───> Filtered: Base de dados após os tratamentos necessários.
<br>├─────> Classification: Base de dados após os tratamentos necessários adaptada para o algoritmo de classificação.
<br>├─────> Regression: Base de dados após os tratamentos necessários adaptada para o algoritmo de regressão.
<br>└─────> Deep_Learning: Base de dados após os tratamentos necessários adaptada para o algoritmo de aprendizado profundo.
<br>└───> Raw: Base de dados original, sem nenhum tratamento.
<br>└─> Machine Learning: Arquivos relacionados à implementação dos algoritmos

### Passo-a-Passo
#### **1. Tratamento de Dados**
~~1.1. Identificar em quais arquivos estão os dados relevantes~~
<br>~~1.2. Criar um algoritmo para extrair os dados do .mat e salvá-los em .csv~~
<br>~~1.3. Remover atributos não necessários~~
<br>~~1.4. Se alguma linha tiver todos os atributos HANTS em NAN, retirar a linha, os outros NAN serão a media da coluna~~
<br>~~1.5. Tratas os multíplos atributos meta~~
<br>~~1.5.1. Para classificação: Se algum atributo HANTS for >400, valor 1, se não, 0~~ ---> POUCOS VALORES MAIORES QUE 400 NAS COLUNAS HANS
<br>~~1.5.2. Para regressão: Valor meta é o maior dos atributos HANS~~
<br>~~1.5.3. Para aprendizado profundo: Valor meta é o maior dos atributos HANS~~
<br>~~1.6. Remover ruidos~~
<br>1.7. Balancear classe majoritária para fica maj/min < 3
<br>~~1.8. Normalizar dados~~
<br>~~1.8.1. Para classificação: Normalizar tudo menos o rótulo meta
<br>~~1.8.2. Para regressão: Normalizar todas as colunas
<br>~~1.8.3. Para aprendizado profundo: Normalizar todas as colunas
<br>~~1.9. Para classificação e regressão: aplicar janela deslizante~~
#### **2. Criação do Algoritmo de Aprendizado de Máquina**
~~2.1. Estudar algoritmos de classificação capazes de trabalhar sobre uma base de dados temporal~~
<br>2.2. Para classificação: Desenvolver o algoritmo SVM
<br>2.3. Para regressão: Desenvolver o algoritmo Regressão Linear
<br>2.4. Para aprendizado profundo: Desenvolver o algoritmo RNN
#### **3. Aprendizado de Máquina**
3.1. Definir de que forma serão realizados os testes e quais métodos usar
<br>3.2. Separar conjuntos
<br>3.3. Fazer validação
<br>3.4. Fazer ajustes de hiperparâmetros
<br>3.5. Colher dados finais
#### **4. Escrita do Artigo**
4.1. Estudar o padrão do artigo indicado pela professora
<br>4.2. Escrever a Conclusão