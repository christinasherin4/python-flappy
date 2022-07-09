def search(mat, n, x):
    if (n == 0):
        return -1

    for i in range(n):
        for j in range(n):

            if (mat[i][j] == x):
                print("Element found at (", i, ",", j, ")")
                return 1

    print(" Element not found")
    return 0



mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
search(mat, 4, 29)
