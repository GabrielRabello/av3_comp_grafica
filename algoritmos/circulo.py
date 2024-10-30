def circulo(selected_cells, rendered_cells, parameters, grid):
    if len(selected_cells) != 1:
        raise ValueError("algoritmo requer seleção de um (único) centro")

    try:
        raio = int(parameters['raio'])
    except ValueError:
        raise ValueError("raio deve ser fornecido")

    center_x = selected_cells[0][0]
    center_y = selected_cells[0][1]

    err = -raio
    x = 0
    y = raio

    _renderizar_pontos_circulo(x, y, center_x, center_y, grid)

    while x <= y:
        err += 2 * x + 1
        x += 1
        if err >= 0:
            err += x - 2 * y
            y -= 1
        _renderizar_pontos_circulo(x, y, center_x, center_y, grid)


def _renderizar_pontos_circulo(x, y, centro_x, centro_y, grid):
    grid.render_cell((centro_x + x, centro_y + y))
    grid.render_cell((centro_x + y, centro_y + x))
    grid.render_cell((centro_x + y, centro_y - x))
    grid.render_cell((centro_x + x, centro_y - y))
    grid.render_cell((centro_x - x, centro_y - y))
    grid.render_cell((centro_x - y, centro_y - x))
    grid.render_cell((centro_x - y, centro_y + x))
    grid.render_cell((centro_x - x, centro_y + y))
