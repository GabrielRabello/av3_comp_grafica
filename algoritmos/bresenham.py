def linha(selected_cells, rendered_cells, parameters, grid):
    if len(selected_cells) != 2:
        raise ValueError("algoritmo requer dois pontos")

    x0 = selected_cells[0][0]
    y0 = selected_cells[0][1]
    x1 = selected_cells[1][0]
    y1 = selected_cells[1][1]
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    err = dx - dy

    while True:
        grid.render_cell((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy