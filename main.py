import numpy as np


def random(name):
    # random_num_a = np.random.randint(-3, 3, 1000)
    # random_num_b = np.random.rand(1000)
    # result = random_num_b + random_num_a

    a = -3
    b = 3
    result = (b-a) * np.random.rand(1000) + a

    print(f'{result}')


if __name__ == '__main__':
    random('d')