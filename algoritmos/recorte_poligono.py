from .polilinha import polilinha

def recorte_poligono(selected_cells, rendered_cells, parameters, grid):
    x_min = int(parameters["x_min"])
    y_min = int(parameters["y_min"])
    x_max = int(parameters["x_max"])
    y_max = int(parameters["y_max"])

    clip_polygon = [(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)]

    cp1 = clip_polygon[-1]
    output_list = selected_cells

    for clip_vertex in clip_polygon:
        cp2 = clip_vertex
        input_list = output_list
        output_list = []
        s = input_list[-1]

        for subject_vertex in input_list:
            e = subject_vertex
            if dentro(e, cp1, cp2):
                if not dentro(s, cp1, cp2):
                    output_list.append(intersecao(cp1, cp2, s, e))
                output_list.append(e)
            elif dentro(s, cp1, cp2):
                output_list.append(intersecao(cp1, cp2, s, e))
            s = e

        cp1 = cp2

    polilinha(output_list, rendered_cells, parameters=None, grid=grid)

def dentro(p, cp1, cp2):
    return (cp2[0] - cp1[0]) * (p[1] - cp1[1]) > (cp2[1] - cp1[1]) * (p[0] - cp1[0])


def intersecao(cp1, cp2, s, e):
    dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]
    dp = [s[0] - e[0], s[1] - e[1]]
    n1 = cp1[0] * cp2[1] - cp1[1] * cp2[0]
    n2 = s[0] * e[1] - s[1] * e[0]
    n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
    return [round((n1 * dp[0] - n2 * dc[0]) * n3), round((n1 * dp[1] - n2 * dc[1]) * n3)]
