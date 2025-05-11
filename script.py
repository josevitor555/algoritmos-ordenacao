from dataset import init_clients

# - Crie uma função que implementa o algoritmo de ordenação.
# - A função deve receber dois parâmetros: o dataset e o critério de ordenação (nome, idade ou valor)

# for client in init_clients():
#     print(client.get("nome"))

# Bubble Sort
def bubble_sort(dataset, key): # passando o dataset e o critério de ordenação
    """
        1 - Algoritmo de ordenação por bolha (Bubble Sort).
        2 - A chave representa o critério de ordenação.
    """
    n = len(dataset)
    # Percorre todos os elementos do array
    for i in range(n):
        # Os últimos i elementos já estão ordenados
        for j in range(0, n-i-1):
            # Percorre o array de 0 até n-i-1
            # Troca se o elemento encontrado for maior que o próximo elemento
            if dataset[j][key] > dataset[j+1][key]:
                dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
    return dataset

# Insertion Sort
def insertion_sort(dataset, key):
    """
        1 - Algoritmo de ordenação por inserção (Insertion Sort).
        2 - A chave representa o critério de ordenação.
    """
    for i in range(1, len(dataset)):
        key_item = dataset[i]
        j = i - 1
        # Move os elementos de dataset[0..i-1], que são maiores que key_item,
        # para uma posição à frente de sua posição atual
        while j >= 0 and key_item[key] < dataset[j][key]:
            dataset[j + 1] = dataset[j]
            j -= 1
        dataset[j + 1] = key_item
    return dataset

# Selection Sort
def selection_sort(dataset, key):
    """
        1 - Algoritmo de ordenação por seleção (Selection Sort).
        2 - A chave representa o critério de ordenação.
    """
    for i in range(len(dataset)):
        # Encontra o menor elemento no array não ordenado restante
        min_index = i
        for j in range(i + 1, len(dataset)):
            if dataset[j][key] < dataset[min_index][key]:
                min_index = j
        # Troca o menor elemento encontrado com o primeiro elemento da parte não ordenada. Ex: Troca o menor elemento 2 pelo primeiro índice 16.
        dataset[i], dataset[min_index] = dataset[min_index], dataset[i]
    return dataset

# Merge Sort
def merge_sort(dataset, key):
    """
        1 - Algoritmo de ordenação por mesclagem (Merge Sort) com base em uma chave definida.
        2 - A chave representa o critério de ordenação.
    """
    if len(dataset) > 1:
        mid = len(dataset) // 2  # Encontrando o meio do array
        L = dataset[:mid]  # Dividindo os elementos em 2 metades
        R = dataset[mid:] # Dividindo os elementos em 2 metades

        merge_sort(L, key)  # Ordenando a primeira metade
        merge_sort(R, key)  # Ordenando a segunda metade

        i = j = k = 0

        # Copia os dados para os arrays temporários L[] e R[]
        while i < len(L) and j < len(R):
            if L[i][key] < R[j][key]:
                dataset[k] = L[i] # Topo da sublista esquerda
                i += 1 # Avançar o topo da sublista esquerda
            else:
                dataset[k] = R[j] # Topo da sublista direita
                j += 1 # Avançar o topo da sublista direita
            k += 1

        # Verifica se algum elemento foi deixado
        while i < len(L):
            dataset[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            dataset[k] = R[j]
            j += 1
            k += 1

    return dataset

import random
# Rearranje a lista de forma que todos os elementos anteriores ao
# pivô sejam menores que ele, e todos os elementos posteriores ao pivô sejam maiores que ele.
def partition(dataset, low, high, key): # Passando o key, comparando os elementos usando dataset[j][key]
    
    # Escolha um pivo aleatorio
    # pivot = dataset[high] # Ultimo elemento da lista
    pivot_index = random.randint(low, high)
    dataset[high], dataset[pivot_index] = dataset[pivot_index], dataset[high]
    
    pivot = dataset[high][key]
    
    # Indice do elemento menor
    # Indica a posição correta do pivô encontrada até o momento
    i = low - 1
    
    # Percorrer dataset[low..high] e mover todos os elementos menores
    # Para o lado esquerdo
    # Os elementos de baixo para
    # i são menores após cada iteração
    
    for j in range(low, high):
        if dataset[j][key] < pivot:
            i += 1
            swap(dataset, i, j)
    
    # Mover o pivô após elementos menores e
    # retornar sua posição
    swap(dataset, i + 1, high)
    return i + 1

# Função de troca
def swap(dataset, i, j):
    dataset[i], dataset[j] = dataset[j], dataset[i]

# Método público que encapsula a recursiva para aceitar os parametros dataset e key
def quick_sort(dataset, key):
    # Faz uma cópia para nao alterar a lista original
    data_copy = dataset[:]
    _quick_sort(data_copy, 0, len(data_copy) - 1, key)
    return data_copy

# Mensurando o tempo de execução dos algoritmos
# Implementando o quick sort
def _quick_sort(dataset, low, high, key):
    if low < high:
        
        # pi é o índice de retorno da partição do pivô
        pi = partition(dataset, low, high, key)
        
        # Chamadas recursivas:
        # Recursão requer elementos menores
        # e elementos maiores ou iguais
        _quick_sort(dataset, low, pi - 1, key)
        _quick_sort(dataset, pi + 1, high, key)
def measure_time(algorithm, dataset, key):
    """
    Mede o tempo de execução de um algoritmo de ordenação.
    
    :param algorithm: Função do algoritmo de ordenação.
    :param dataset: Lista de dados a ser ordenada.
    :param key: Chave usada para ordenação.
    :return: Tempo de execução em segundos.
    """
    import time
    import copy

    # Cria uma cópia do dataset para evitar modificações no original
    dataset_copy = dataset.copy()

    # Marca o tempo de início
    started = time.perf_counter()

    # Executa o algoritmo de ordenação
    algorithm(dataset_copy, key)

    # Marca o tempo de término
    end = time.perf_counter()

    # Calcula o tempo de execução
    time_execute = end - started
    return f"{time_execute:.8f} segundos."
