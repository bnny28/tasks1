import itertools


def _fill_distance_matrix(points: tuple) -> list:
    """
    :param points: The tuple of coordinates of points on the plane
    :return: Matrix of distances between points
    """
    # Заполняем матрицу расстояний для переданных точек,
    # чтобы не пересчитывать каждый раз когда потребуется
    res = []
    length = len(points)
    row = [0] * length
    for i in range(length + 1):
        res.append(row[:])
    for i, i_pnt in enumerate(points):
        for j, j_pnt in enumerate(points):
            if i != j and res[i][j] == 0:
                res[i][j] = res[j][i] = ((i_pnt[0] - j_pnt[0]) ** 2 + (i_pnt[1] - j_pnt[1]) ** 2) ** 0.5
    return res


def get_short_path_points(points: tuple) -> str:
    """
    :param points: The tuple of coordinates of points on the plane
    :return: Description of the shortest path (TSP task)
    Use Python 3.8+
    """
    # Заполним матрицу расстояний между точками
    distance_matrix = _fill_distance_matrix(points)

    # Заведомо максимальное число для инициализации, чтобы любое было не больше
    min_length = 2147483647
    min_path = ''
    # Генерируем все возможные комбинации путей
    path_variation = itertools.permutations([i for i in range(1, len(points))], len(points) - 1)
    # Проходим в цикле по всем вариантам, подсчитывая длину путей и выясняя минимальный
    for num_points in path_variation:
        cur_length = 0
        # Формируем строку пути, вычисляя его расстояние (используем выражения присваивания PEP 572 (Python 3.8+))
        pred_point = 0
        cur_path = f'{points[pred_point]} '
        for num in num_points:
            cur_path += f'-> {points[num]}[{(cur_length := cur_length + distance_matrix[pred_point][num])}] '
            pred_point = num
        # Формируем строку пути в начальную точку, затем выводим весь путь
        cur_path += f'-> {points[0]}[{(cur_length := cur_length + distance_matrix[num_points[-1]][0])}] '
        cur_path += f'= {cur_length}'
        # Проверяем путь на минимальность
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

    tuple_points = (start_point, point1, point2, point3, point4)

    print(get_short_path_points(tuple_points))
