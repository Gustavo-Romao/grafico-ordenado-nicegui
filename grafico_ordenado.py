from nicegui import ui
import random

# Array inicial com 10 elementos aleatórios entre 0 e 100 desordenados
unsorted_data = random_numbers = random.sample(range(100), 10)

# Gráfico da bilbioteca niceGUI
echart = ui.chart({
    'title': False,
    'chart': {'type': 'bar'},
    'series': [
        {'name': 'Desordenado', 'data': unsorted_data},
    ],
})

# Algoritimo de ordenação dos elementos
def insert_sort_numbers(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Função que atualiza o gráfico
def update():
    sorted_data = insert_sort_numbers(unsorted_data)
    echart.options['series'][0]['data'] = sorted_data
    echart.options['series'][0]['name'] = 'Organizado!'
    echart.update()

# Botão com callback para a função de atualização
ui.button('Atualiza', on_click=update)

# Init da biblioteca
ui.run()
