from .bresenham import linha


def polilinha(selected_cells, rendered_cells, parameters, grid):
    if len(selected_cells) < 2:
        raise ValueError("algoritmo requer dois ou mais pontos")

    for i in range(len(selected_cells) - 1):
        linha([selected_cells[i], selected_cells[i + 1]], rendered_cells, parameters, grid)

    linha([selected_cells[-1], selected_cells[0]], rendered_cells, parameters, grid)
