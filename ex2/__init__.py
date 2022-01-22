from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        # put your code here
        def new_wrapper(*args, **kwargs):
            totalTime = 0
            for n in range(num):
                start = fetcher.time.time()
                func(*args, **kwargs)
                time = fetcher.time.time() - start
                totalTime += time
                print("time: " + str(time))

            print("avg: " + str(totalTime / num))

        return new_wrapper

    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
