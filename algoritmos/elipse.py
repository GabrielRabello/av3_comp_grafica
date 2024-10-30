def elipse(selected_cells, rendered_cells, parameters, grid):
    if len(selected_cells) != 1:
        raise ValueError("algoritmo requer seleção de um (único) centro")

    try:
        raio_x = int(parameters['raio_x'])
        raio_y = int(parameters['raio_y'])
    except ValueError:
        raise ValueError("raio_x e raio_y devem ser fornecidos")

    center_x = selected_cells[0][0]
    center_y = selected_cells[0][1]

    x = 0
    y = raio_y
    a2 = raio_x ** 2
    b2 = raio_y ** 2
    dx = 2 * b2 * x
    dy = 2 * a2 * y
    e = -raio_y * a2 + a2 * 0.25
    while dx < dy:
        _renderizar_pontos_elipse(x, y, center_x, center_y, grid)
        x += 1
        e += dx + b2
        dx += 2 * b2
        if e > 0:
            y -= 1
            e += a2 - dy
            dy -= 2 * a2

    e = b2 * ((x + 0.5) * (x + 0.5)) + a2 * y * y - a2 * b2
    while y >= 0:
        _renderizar_pontos_elipse(x, y, center_x, center_y, grid)
        y -= 1
        e += a2 - dy
        dy -= 2 * a2
        if e < 0:
            x += 1
            e += dx + b2
            dx += 2 * b2


def _renderizar_pontos_elipse(x, y, centro_x, centro_y, grid):
    grid.render_cell((centro_x + x, centro_y + y))
    grid.render_cell((centro_x - x, centro_y + y))
    grid.render_cell((centro_x + x, centro_y - y))
    grid.render_cell((centro_x - x, centro_y - y))
