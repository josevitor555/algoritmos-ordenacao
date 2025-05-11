# Inicialização
# import dataset
from script import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, measure_time
from dataset import init_clients

clients = init_clients()

# 1 - Usando o algoritmo de ordenação por bolha (Bubble Sort)

# Ordenação por nome
clients_sorted_by_name = bubble_sort(clients, "nome")
print("\nSorted by name: ")
for client in clients_sorted_by_name:
    print(client["nome"])
    
# Ordenação por idade
clients_sorted_by_age = bubble_sort(clients, "idade")
print("\nSorted by age: ")
for client in clients_sorted_by_age:
    print(client["idade"])

# Ordenação por valor de compra (Por ordem decrescente)
clients_sorted_by_value = bubble_sort(clients, "valor_compra")
print("\nSorted by value: ")
for client in clients_sorted_by_value[::-1]:  # Lista revsersa usando slicing
    print(client["valor_compra"])

# 2 - Usando o algoritmo de ordenação por inserção (Insertion Sort)

# Ordenação por nome
clients_sorted_by_name = insertion_sort(clients, "nome")
print("\nSorted by name: ")
for client in clients_sorted_by_name:
    print(client["nome"])

# Ordenação por idade
clients_sorted_by_age = insertion_sort(clients, "idade")
print("\nSorted by age: ")
for client in clients_sorted_by_age:
    print(client["idade"])

# # Ordenação por valor de compra (Por ordem decrescente)
clients_sorted_by_value = insertion_sort(clients, "valor_compra")
print("\nSorted by value: ")
for client in clients_sorted_by_value[::-1]:  # Lista revsersa usando slicing
    print(client["valor_compra"])

# 3 - Usando o algoritmo de ordenação por seleção (Selection Sort)

# Ordenação por nome
clients_sorted_by_name = selection_sort(clients, "nome")
print("\nSorted by name: ")
for client in clients_sorted_by_name:
    print(client["nome"])

# Ordenação por idade
clients_sorted_by_age = selection_sort(clients, "idade")
print("\nSorted by age: ")
for client in clients_sorted_by_age:
    print(client["idade"])

# Ordenação por valor de compra (Por ordem decrescente)
clients_sorted_by_value = selection_sort(clients, "valor_compra")
print("\nSorted by value: ")
for client in clients_sorted_by_value[::-1]:  # Lista revsersa usando slicing
    print(client["valor_compra"])

# 4 - Usando o algoritmo de ordenação por mesclagem (Merge Sort)
# Ordenação por nome
clients_sorted_by_name = merge_sort(clients, "nome")
print("\nSorted by name: ")
for client in clients_sorted_by_name:
    print(client["nome"])

# Ordenação por idade
clients_sorted_by_age = merge_sort(clients, "idade")
print("\nSorted by age: ")
for client in clients_sorted_by_age:
    print(client["idade"])

# Ordenação por valor de compra (Por ordem decrescente)
clients_sorted_by_value = merge_sort(clients, "valor_compra")
print("\nSorted by value: ")
for client in clients_sorted_by_value[::-1]:  # Lista revsersa usando slicing
    print(client["valor_compra"])

# 5 Quick Sort - Algoritmo de ordenação rápida (Quick Sort)
# # Ordenação por nome
clients_sorted_by_name = quick_sort(clients, "nome")
print("\nSorted by name: ")
for client in clients_sorted_by_name:
    print(client["nome"])
    
# Ordenação por idade
clients_sorted_by_age = quick_sort(clients, "idade")
print("\nSorted by age: ")
for client in clients_sorted_by_age:
    print(client["idade"])

# Ordenação por valor de compra (Por ordem decrescente)
clients_sorted_by_value = quick_sort(clients, "valor_compra")
print("\nSorted by value: ")
for client in clients_sorted_by_value[::-1]:  # Lista revsersa usando slicing
    print(client["valor_compra"])

# Tempo de execução de cada algoritmo:
# 1 - Bubble sort
time_bubble_sort = measure_time(bubble_sort, clients, "nome")
print(f"\nTempo de execução do Bubble Sort por nome: {time_bubble_sort}")
time_bubble_sort = measure_time(bubble_sort, clients, "idade")
print(f"Tempo de execução do Bubble Sort por idade: {time_bubble_sort}")
time_bubble_sort = measure_time(bubble_sort, clients, "valor_compra")
print(f"Tempo de execução do Bubble Sort por valor de compra: {time_bubble_sort}")

# 2 - Insertion Sort
time_insertion_sort = measure_time(insertion_sort, clients, "nome")
print(f"\nTempo de execução do Insertion Sort por nome: {time_insertion_sort}")
time_insertion_sort = measure_time(insertion_sort, clients, "idade")
print(f"Tempo de execução do Insertion Sort por idade: {time_insertion_sort}")
time_insertion_sort = measure_time(insertion_sort, clients, "valor_compra")
print(f"Tempo de execução do Insertion Sort por valor de compra: {time_insertion_sort}")

# 3 - Selection Sort
time_selection_sort = measure_time(selection_sort, clients, "nome")
print(f"\nTempo de execução do Selection Sort por nome: {time_selection_sort}")
time_selection_sort = measure_time(selection_sort, clients, "idade")
print(f"Tempo de execução do Selection Sort por idade: {time_selection_sort}")
time_selection_sort = measure_time(selection_sort, clients, "valor_compra")
print(f"Tempo de execução do Selection Sort por valor de compra: {time_selection_sort}")

# 4 - Merge Sort
time_merge_sort = measure_time(merge_sort, clients, "nome")
print(f"\nTempo de execução do Merge Sort por nome: {time_merge_sort}")
time_merge_sort = measure_time(merge_sort, clients, "idade")
print(f"Tempo de execução do Merge Sort por idade: {time_merge_sort}")
time_merge_sort = measure_time(merge_sort, clients, "valor_compra")
print(f"Tempo de execução do Merge Sort por valor de compra: {time_merge_sort}")

# 5 - Quick Sort
time_quick_sort = measure_time(quick_sort, clients, "nome")
print(f"\nTempo de execução do Quick Sort por nome: {time_quick_sort}")
time_quick_sort = measure_time(quick_sort, clients, "idade")
print(f"Tempo de execução do Quick Sort por idade: {time_quick_sort}")
time_quick_sort = measure_time(quick_sort, clients, "valor_compra")
print(f"Tempo de execução do Quick Sort por valor de compra: {time_quick_sort}")
