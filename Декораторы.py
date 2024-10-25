def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # метод (Оптимизированная проверка делителей)
        if result <= 1:
            print('Составное')
            return result
        if result <= 3:
            print('Простое')
            return result
        if result % 2 == 0 or result % 3 == 0:
            print('Составное')
            return result
        i = 5
        while i * i <= result:
            if result % i == 0 or result % (i + 2) == 0:
                print('Составное')
                return result
            i += 6
        print('Простое')
        return result
    return wrapper

@is_prime
def sum_num(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


if __name__ == "__main__":
    """
    Немного оптимизировал данную задачу, вместо функции sum_three, сделал функцию sum_num.
    Функия sum_num теперь принимает не ограниченное количество чисел.
    """
    result = sum_num(2, 3, 6)
    print(result)