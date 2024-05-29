def sumatoria(num):
    if num == 1:
        return 1
    else:
        return num + sumatoria(num - 1)

print(sumatoria(5))