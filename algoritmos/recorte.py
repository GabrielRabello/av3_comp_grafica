from typing import Tuple
from enum import Enum
from .bresenham import linha


def recorte_linha(selected_cells, rendered_cells, parameters, grid):
    if len(selected_cells) != 2:
        raise ValueError("algoritmo requer seleção de dois pontos")

    try:
        x_min = int(parameters['x_min'])
        x_max = int(parameters['x_max'])
        y_min = int(parameters['y_min'])
        y_max = int(parameters['y_max'])
    except ValueError:
        raise ValueError("x_min, x_max, y_min e y_max devem ser fornecidos")

    p1 = selected_cells[0]
    p2 = selected_cells[1]

    c1 = _mk_codigo(p1, x_min, x_max, y_min, y_max)
    c2 = _mk_codigo(p2, x_min, x_max, y_min, y_max)

    if c1 & c2 != 0:
        raise ValueError("linha fora da janela")

    if c1 | c2 == 0:
        linha(selected_cells, rendered_cells, parameters, grid)
        return

    difBit = _findDifBit(c1, c2)  # Pega primeiro bit diferente

    # calcula a intersecção entre a reta e a borda do monitor (referente ao bit calculado acima)
    line = _find_Window_Line(difBit)
    pi = _intersecao_linha(line, p1, p2, x_min, x_max, y_min, y_max)

    # Usa o ponto que tem 0 nesse bit e a intersecção recursivamente
    if _getBit(c1, difBit) == 0:
        recorte_linha((p1, pi), rendered_cells, parameters, grid=grid)
    else:
        recorte_linha((pi, p2), rendered_cells, parameters, grid=grid)


class _Posicao(Enum):
    DENTRO = 0
    ESQUERDA = 1 << 0
    DIREITA = 1 << 1
    INFERIOR = 1 << 2
    SUPERIOR = 1 << 3


def _mk_codigo(p, x_min, x_max, y_min, y_max) -> int:
    code = _Posicao.DENTRO.value
    if p[0] < x_min:
        code |= _Posicao.ESQUERDA.value
    if p[0] > x_max:
        code |= _Posicao.DIREITA.value
    if p[1] < y_min:
        code |= _Posicao.INFERIOR.value
    if p[1] > y_max:
        code |= _Posicao.SUPERIOR.value
    return code


def _getBit(code, bit_position):
    """Checa se um bit específico está setado no código"""
    return (code >> bit_position) & 1


def _findDifBit(c1, c2):
    """Encontra o primeiro bit que se diferencia entre dois códigos."""
    return (c1 | c2).bit_length() - 1  # Returns the highest set bit in


def _find_Window_Line(bit) -> _Posicao:
    if bit == 0: return _Posicao.ESQUERDA
    if bit == 1: return _Posicao.DIREITA
    if bit == 2: return _Posicao.INFERIOR
    if bit == 3: return _Posicao.SUPERIOR


def _intersecao_linha(
        pos: _Posicao,
        p1: Tuple[int, int],
        p2: Tuple[int, int],
        x_min, x_max, y_min, y_max) -> Tuple[int, int]:
    """Calcula o ponto de interseção da linha com a fronteira"""
    # Determine the line equation parameters
    x1, y1 = p1
    x2, y2 = p2
    x = 0.0
    y = 0.0
    if pos == _Posicao.ESQUERDA:
        x = x_min
        y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    elif pos == _Posicao.DIREITA:
        x = x_max
        y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    elif pos == _Posicao.INFERIOR:
        y = y_min
        x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
    elif pos == _Posicao.SUPERIOR:
        y = y_max
        x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

    return round(x), round(y)
