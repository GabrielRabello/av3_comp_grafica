from grid import Grid
import algoritmos as algo

grid = Grid(extent=11, size=800)

grid.add_algorithm(name="Bresenham", parameters=None, algorithm=algo.linha)
grid.add_algorithm(name="Recorte", parameters=['x_min', 'x_max', 'y_min', 'y_max'], algorithm=algo.recorte_linha)
grid.add_algorithm(name="Recorte Poligono", parameters=['x_min', 'x_max', 'y_min', 'y_max'], algorithm=algo.recorte_poligono)
grid.add_algorithm(name="Polilinha", parameters=None, algorithm=algo.polilinha)
grid.add_algorithm(name="Circulo", parameters=['raio'], algorithm=algo.circulo)
grid.add_algorithm(name="Escala", parameters=['fator_x', 'fator_y', 'pivo'], algorithm=algo.escala)
grid.add_algorithm(name="Translação", parameters=['dx', 'dy'], algorithm=algo.translacao)
grid.add_algorithm(name="Rotação", parameters=['angulo', 'pivo'], algorithm=algo.rotacao)
grid.add_algorithm(name="Elipse", parameters=['raio_x', 'raio_y'], algorithm=algo.elipse)

grid.show()
