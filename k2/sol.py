import numpy as np

def main(consumption, beer_map):
    beer_map = np.array(beer_map)
    rows, cols = beer_map.shape

    memo_beer = -np.ones((rows, cols)) * np.inf
    memo_path = np.empty((rows, cols), dtype=object)

    def get_best_path(i, j):
        # ne fussunk ki
        if i >= rows or j >= cols:
            return -np.inf, ""

        # ha m´r kiszámoltuk csak dobjuk vissza (ez a lényeg xd)
        if memo_path[i, j] is not None:
            return memo_beer[i, j], memo_path[i, j]

        # Base case: jobb alsó cella
        if i == rows - 1 and j == cols - 1:
            memo_beer[i, j] = beer_map[i, j]
            memo_path[i, j] = ""
            return memo_beer[i, j], memo_path[i, j]

        best_beer = -np.inf
        best_path = ""

        # jobbra csekkolás
        if j + 1 < cols:
            beer_right, path_right = get_best_path(i, j + 1)
            if beer_right - consumption >= 0:
                new_beer = beer_right - consumption + beer_map[i, j]
                if new_beer > best_beer:
                    best_beer = new_beer
                    best_path = "J" + path_right

        # lefele csekkolás
        if i + 1 < rows:
            beer_down, path_down = get_best_path(i + 1, j)
            if beer_down - consumption >= 0:
                new_beer = beer_down - consumption + beer_map[i, j]
                if new_beer > best_beer:
                    best_beer = new_beer
                    best_path = "I" + path_down

        memo_beer[i, j] = best_beer
        memo_path[i, j] = best_path
        return best_beer, best_path

    # kezdés fentrol
    max_beer, path = get_best_path(0, 0)

    # ha a max_beer -inf akkor nincs legjobb út // irjon ki valamit?????
    if max_beer == -np.inf:
        return [-1,-1]
    else:
        return [max_beer,path]