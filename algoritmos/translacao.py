def translacao(selected_cells, rendered_cells, parameters, grid):
    if len(selected_cells) == 0:
        raise ValueError("algoritmo requer seleção de pelo menos um ponto")

    try:
        dx = int(parameters['dx'])
        dy = int(parameters['dy'])
    except ValueError:
        raise ValueError("dx e dy devem ser fornecidos")

    for cell in selected_cells:
        x = cell[0] + dx
        y = cell[1] + dy
        grid.render_cell((x, y))