import ast


def escala(selected_cells, rendered_cells, parameters, grid):
    if len(selected_cells) == 0:
        raise ValueError("algoritmo requer seleção de pelo menos um ponto")

    try:
        fator_x = int(parameters['fator_x'])
        fator_y = int(parameters['fator_y'])
        pivo_x, pivo_y = ast.literal_eval(parameters["pivo"])
    except ValueError:
        raise ValueError("fator_x, fator_y e pivô (formato: (x,y)) devem ser fornecidos")

    for (x, y) in selected_cells:
        transladado_x = x - pivo_x
        transladado_y = y - pivo_y

        escalado_x = transladado_x * fator_x
        escalado_y = transladado_y * fator_y

        final_x = escalado_x + pivo_x
        final_y = escalado_y + pivo_y

        grid.render_cell((round(final_x), round(final_y)))
