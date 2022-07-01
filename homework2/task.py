import itertools


def _fill_distance_matrix(points: tuple) -> list:
    """
    :param points: The tuple of coordinates of 5 points on the plane
    :return: Matrix (5x5) of distances between points
    """
    # Заполняем матрицу расстояний для переданных точек,
    # чтобы не пересчитывать каждый раз когда потребуется
    res = [[0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5]
    for i, i_pnt in enumerate(points):
        for j, j_pnt in enumerate(points):
            if i != j and res[i][j] == 0:
                res[i][j] = res[j][i] = ((i_pnt[0] - j_pnt[0]) ** 2 + (i_pnt[1] - j_pnt[1]) ** 2) ** 0.5
    return res


def get_short_path_5_points(points: tuple) -> str:
    """
    :param points: The tuple of coordinates of 5 points on the plane
    :return: Description of the shortest path (TSP task)
    Use Python 3.8+
    """
    # Заполним матрицу расстояний между точками
    distance_matrix = _fill_distance_matrix(points)

    # Заведомо максимальное число для инициализации, чтобы любое было не больше
    min_length = 2147483647
    min_path = ''
    # Генерируем все возможные комбинации путей
    path_variation = itertools.permutations((1, 2, 3, 4), 4)
    # Проходим в цикле по всем вариантам, подсчитывая длину путей и выясняя минимальный
    for p1, p2, p3, p4 in path_variation:
        cur_length = 0
        # Формируем строку пути, вычисляя его расстояние (используем выражения присваивания PEP 572 (Python 3.8+))
        cur_path = f'{points[0]} ' \
                   f'-> {points[p1]}[{(cur_length := cur_length + distance_matrix[0][p1])}] ' \
                   f'-> {points[p2]}[{(cur_length := cur_length + distance_matrix[p1][p2])}] ' \
                   f'-> {points[p3]}[{(cur_length := cur_length + distance_matrix[p2][p3])}] ' \
                   f'-> {points[p4]}[{(cur_length := cur_length + distance_matrix[p3][p4])}] ' \
                   f'-> {points[0]}[{(cur_length := cur_length + distance_matrix[p4][0])}] ' \
                   f'= {cur_length}'
        if cur_length < min_length:
            min_length = cur_length
            min_path = cur_path
    return min_path


if __name__ == '__main__':
    start_point = (0, 2)
    point1 = (2, 5)
    point2 = (5, 2)
    point3 = (6, 6)
    point4 = (8, 3)

    tuple_5_points = (start_point, point1, point2, point3, point4)

    print(get_short_path_5_points(tuple_5_points))
