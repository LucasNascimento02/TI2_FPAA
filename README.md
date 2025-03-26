# Projeto MaxMin Select

O **MaxMin Select** é um projeto desenvolvido para implementar um algoritmo eficiente de busca simultânea do maior e menor elementos em uma sequência de números. Este projeto utiliza a técnica de divisão e conquista para reduzir o número de comparações necessárias em relação a uma abordagem linear simples.

## Divisão e Conquista

A técnica de **Divisão e Conquista** é uma estratégia algorítmica que resolve um problema dividindo-o em subproblemas menores, resolvendo esses subproblemas e então combinando as soluções. No caso do MaxMin Select, o array é dividido recursivamente até que tenhamos subarrays de tamanho 1 ou 2, onde a comparação é trivial.

### Processo de Divisão

O algoritmo divide o array recursivamente seguindo estas etapas:

1. **Divisão Inicial**:
   - Recebe um array de tamanho n
   - Calcula o ponto médio: `meio = (inicio + fim) // 2`
   - Divide o array em duas metades: `[inicio...meio]` e `[meio+1...fim]`

2. **Casos Base**:
   - Para um elemento: retorna o próprio elemento como mínimo e máximo
   - Para dois elementos: compara-os diretamente
     ```python
     if arr[inicio] < arr[fim]:
         return arr[inicio], arr[fim]  # (min, max)
     else:
         return arr[fim], arr[inicio]  # (min, max)
     ```

3. **Recursão**:
   - Chama recursivamente para a metade esquerda: `min_esq, max_esq = max_min_select(arr, inicio, meio)`
   - Chama recursivamente para a metade direita: `min_dir, max_dir = max_min_select(arr, meio + 1, fim)`

### Processo de Combinação (Merge)

Após a divisão, o algoritmo combina os resultados da seguinte forma:

1. **Combinação dos Resultados**:
   - Recebe dois pares de (min, max) das chamadas recursivas
   - Compara os mínimos: `min_final = min(min_esq, min_dir)`
   - Compara os máximos: `max_final = max(max_esq, max_dir)`
   - Retorna o par `(min_final, max_final)`

2. **Exemplo de Combinação**:
   ```python
   # Subarray esquerdo retorna: (2, 5)
   # Subarray direito retorna: (1, 8)
   min_final = min(2, 1) = 1
   max_final = max(5, 8) = 8
   resultado = (1, 8)
   ```

3. **Número de Comparações**:
   - Cada nível de combinação requer exatamente 2 comparações:
     - Uma para encontrar o mínimo global
     - Uma para encontrar o máximo global

### Exemplo Completo

Para o array `[5, 2, 8, 1]`:

1. **Primeira Divisão**:
   - Metade esquerda: `[5, 2]`
   - Metade direita: `[8, 1]`

2. **Processamento das Metades**:
   - Para `[5, 2]`: compara diretamente → `(2, 5)`
   - Para `[8, 1]`: compara diretamente → `(1, 8)`

3. **Combinação Final**:
   - Mínimo: `min(2, 1) = 1`
   - Máximo: `max(5, 8) = 8`
   - Resultado: `(1, 8)`

### Visualização do Algoritmo

O diagrama abaixo ilustra o processo de divisão e conquista do algoritmo MaxMin Select:

![Diagrama do Algoritmo MaxMin Select](assets/maxmin_select_diagram.drawio)

O diagrama mostra:
1. A divisão do array original em subarrays menores
2. O processo recursivo de divisão até atingir pares de elementos
3. A combinação dos resultados para obter o mínimo e máximo globais
4. O número de comparações em cada nível da recursão

## Complexidade do Algoritmo

O algoritmo MaxMin Select possui as seguintes características de complexidade:

- **Tempo**: O(n) - onde n é o número de elementos no array
- **Espaço**: O(log n) - devido à pilha de recursão
- **Número de Comparações**: 3n/2 - 2 no pior caso

## Dependências

Este projeto requer apenas Python instalado, sem dependências externas.

## Ambiente Virtual

### Passo 1: Criar e ativar o ambiente virtual

1. Crie um ambiente virtual:
```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual:
   - No macOS e Linux:
   ```bash
   source .venv/bin/activate
   ```
   - No Windows:
   ```bash
   .venv\Scripts\activate
   ```

### Passo 2: Executar o script

Após ativar o ambiente virtual, execute o script principal:
```bash
python main.py
```

## Versão do Python

Este projeto foi desenvolvido e testado na versão **3.x** do Python.

## Explicação das funções

### Arquivo: main.py

#### `max_min_select(arr, inicio, fim)`
- **Objetivo**: Implementa a lógica principal do algoritmo de divisão e conquista
- **Parâmetros**:
  - `arr`: Lista de números
  - `inicio`: Índice inicial do subarray atual
  - `fim`: Índice final do subarray atual
- **Retorno**: Tupla (mínimo, máximo)
- **Complexidade**: O(n)

#### `encontrar_max_min(arr)`
- **Objetivo**: Função auxiliar que inicializa a busca
- **Parâmetros**:
  - `arr`: Lista de números
- **Retorno**: Tupla (mínimo, máximo)
- **Validações**: Verifica se o array não está vazio

## Saída da Execução

```
Array: [1, 5, 2, 8, 3, 9, 7]
Mínimo: 1
Máximo: 9

Array: [10]
Mínimo: 10
Máximo: 10

Array: [4, 2]
Mínimo: 2
Máximo: 4

Array: [1, 2, 3, 4, 5]
Mínimo: 1
Máximo: 5

Array: [-5, 0, 8, -2, 10]
Mínimo: -5
Máximo: 10
```

## Análise da Complexidade

### Análise por Contagem de Operações

1. **Divisão**: O(1) para cada nível
   - Cálculo do ponto médio: 1 operação

2. **Conquista**: 
   - T(n) = 2T(n/2) + 2
   - Duas chamadas recursivas para arrays de tamanho n/2
   - Duas comparações para combinar resultados

3. **Total de Comparações**:
   - C(n) = 2C(n/2) + 2, para n > 2
   - C(2) = 1
   - C(1) = 0
   - Solução: C(n) = 3n/2 - 2

### Análise pelo Teorema Mestre

1. **Forma da Recorrência**: T(n) = 2T(n/2) + O(1)
   - a = 2 (subproblemas)
   - b = 2 (fator de divisão)
   - f(n) = O(1)

2. **Aplicação do Teorema**:
   - log₂2 = 1
   - f(n) = O(n^0)
   - Caso 2: T(n) = Θ(n)
