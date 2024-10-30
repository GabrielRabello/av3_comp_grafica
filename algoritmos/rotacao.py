import ast
import math


def rotacao(selected_cells, rendered_cells, parameters, grid):
    if len(selected_cells) < 2:
        raise ValueError("algoritmo requer seleção de pelo menos dois pontos")

    try:
        angulo = float(parameters["angulo"])
        pivo_x, pivo_y = ast.literal_eval(parameters["pivo"])
    except ValueError:
        raise ValueError("ângulo (graus) e pivô (formato: (x, y)) devem ser fornecidos")

    angulo = math.radians(angulo)

    for (x, y) in selected_cells:
        # Translada ponto para origem
        transladado_x = x - pivo_x
        transladado_y = y - pivo_y

        rotacionado_x = transladado_x * math.cos(angulo) - transladado_y * math.sin(angulo)
        rotacionado_y = transladado_x * math.sin(angulo) + transladado_y * math.cos(angulo)

        # Translada de volta
        final_x = rotacionado_x + pivo_x
        final_y = rotacionado_y + pivo_y

        grid.render_cell((round(final_x), round(final_y)))
