
def kill_zero(array):
    if array:
        """
        Читаем список с конца, выкидываем c помощью pop все элементы
        равные нулю.
        Функция pop() какраз убирает с конца элемент с асимптотикой О(1).
        """
        for i in range(len(array) - 1, -1, -1):
            if array[i] == 0:
                array.pop(i)

    return array


array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
print(kill_zero(array))
