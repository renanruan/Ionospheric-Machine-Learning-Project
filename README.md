## PO-233

### Ideia Inicial
A **sintilação** é um fenômeno da ionosfera que pode afetar certos tipos de radares de aviões. O objetivo deste projeto é classificar se esse fenômeno está ocorrendo ou não a partir de dados da ionosfera.

### Classificação
Este fenômeno pode ser identificado através do valor absoluto do parâmetro HANTS:
- abs(HANTS) < 400 → Fenômeno não está ocorrendo
- abs(HANTS) > 400 → Fenômeno está ocorrendo

### Hipótese
Através de um algoritmo de classificação, pretendemos utilizar um conjunto de parâmetros relevantes para classificar se o fenômeno está ocorrendo.

### Parâmetros Relevantes
- alpha
- gamma
- phi (e variações)
- s4 (e variações)

### Estrutura do Projeto
```
├─> Raw Data: Base de dados utilizada na produção do artigo
├─> Filtered Data: Base de dados após o tratamento
└─> Machine Learning: Arquivos relacionados ao aprendizado de máquina
```

### Passo-a-Passo
1. **Tratamento de Dados**
├─> 1.1. Identificar em quais arquivos estão os dados relevantes
├─> 1.2. Criar um algoritmo para extrair os dados do .mat e salvá-los em .csv
├─> 1.3. Remover atributos não necessários
├─> 1.4. Alterar o valor do atributo HANTS de contínuo para discreto 
└─>1.5. Aplicar outros métodos de tratamento conforme orientações da professora
2. **Criação do Algoritmo de Aprendizado de Máquina**
├─> 2.1. Estudar algoritmos de classificação capazes de trabalhar sobre uma base de dados temporal
└─> 2.2. Desenvolver o algoritmo
3. **Aprendizado de Máquina**
├─> 3.1. Definir de que forma serão realizados os testes
└─>3.2. Separar os arquivos de teste
4. **Escrita do Artigo**
├─> 4.1. Estudar o padrão do artigo indicado pela professora
└─>4.2. Escrever a Conclusão