def max_min_select(arr, inicio, fim):
    """
    Encontra simultaneamente os elementos máximo e mínimo em um array usando a abordagem de divisão e conquista.
    
    Args:
        arr (list): Array de números de entrada
        inicio (int): Índice inicial do subarray atual
        fim (int): Índice final do subarray atual
    
    Returns:
        tuple: Um par contendo (elemento mínimo, elemento máximo)
    """
    # Caso base: Se há apenas um elemento
    if inicio == fim:
        return arr[inicio], arr[inicio]
    
    # Caso base: Se há dois elementos
    if fim == inicio + 1:
        if arr[inicio] < arr[fim]:
            return arr[inicio], arr[fim]
        else:
            return arr[fim], arr[inicio]
    
    # Caso recursivo: Divide o array em duas metades
    meio = (inicio + fim) // 2
    min_esq, max_esq = max_min_select(arr, inicio, meio)
    min_dir, max_dir = max_min_select(arr, meio + 1, fim)
    
    # Combina os resultados
    return min(min_esq, min_dir), max(max_esq, max_dir)

def encontrar_max_min(arr):
    """
    Função auxiliar para encontrar os elementos máximo e mínimo em um array.
    
    Args:
        arr (list): Array de números de entrada
    
    Returns:
        tuple: Um par contendo (elemento mínimo, elemento máximo)
    """
    if not arr:
        raise ValueError("O array não pode estar vazio")
    return max_min_select(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arrays_teste = [
        [1, 5, 2, 8, 3, 9, 7],
        [10],
        [4, 2],
        [1, 2, 3, 4, 5],
        [-5, 0, 8, -2, 10]
    ]
    
    for arr in arrays_teste:
        minimo, maximo = encontrar_max_min(arr)
        print(f"\nArray: {arr}")
        print(f"Mínimo: {minimo}")
        print(f"Máximo: {maximo}") 