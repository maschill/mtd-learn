import numpy as np


def generate_data(values, sep, min_len, max_len, order, samples, prob):
    x = []
    y = []
    cnt = 0
    while cnt < samples:
        cnt += 1
        seq_len = np.random.randint(min_len, max_len + 1)
        seq_list = np.random.choice(values, seq_len)
        if seq_len >= order and np.random.rand() < prob:
            y.append(seq_list[-order])
        else:
            y.append(np.random.choice(values))
        x.append(sep.join(seq_list))

    x = np.array(x).reshape(-1, 1)
    y = np.array(y)

    return x, y


data_values3_order2_full = dict()
data_values3_order2_full['x'] = np.array([['A>A>A'],
                                          ['A>A>B'],
                                          ['A>A>C'],
                                          ['A>B>A'],
                                          ['A>B>A'],
                                          ['A>B>A'],
                                          ['A>B>B'],
                                          ['A>B>B'],
                                          ['A>B>B'],
                                          ['A>B>C'],
                                          ['A>B>C'],
                                          ['A>B>C'],
                                          ['A>C>A'],
                                          ['A>C>A'],
                                          ['A>C>A'],
                                          ['A>C>B'],
                                          ['A>C>B'],
                                          ['A>C>B'],
                                          ['A>C>C'],
                                          ['A>C>C'],
                                          ['A>C>C'],
                                          ['B>A>A'],
                                          ['B>A>A'],
                                          ['B>A>A'],
                                          ['B>A>B'],
                                          ['B>A>B'],
                                          ['B>A>B'],
                                          ['B>A>C'],
                                          ['B>A>C'],
                                          ['B>A>C'],
                                          ['B>B>A'],
                                          ['B>B>A'],
                                          ['B>B>A'],
                                          ['B>B>B'],
                                          ['B>B>B'],
                                          ['B>B>B'],
                                          ['B>B>C'],
                                          ['B>B>C'],
                                          ['B>B>C'],
                                          ['B>C>A'],
                                          ['B>C>A'],
                                          ['B>C>A'],
                                          ['B>C>B'],
                                          ['B>C>B'],
                                          ['B>C>B'],
                                          ['B>C>C'],
                                          ['B>C>C'],
                                          ['B>C>C'],
                                          ['C>A>A'],
                                          ['C>A>A'],
                                          ['C>A>A'],
                                          ['C>A>B'],
                                          ['C>A>B'],
                                          ['C>A>B'],
                                          ['C>A>C'],
                                          ['C>A>C'],
                                          ['C>A>C'],
                                          ['C>B>A'],
                                          ['C>B>A'],
                                          ['C>B>A'],
                                          ['C>B>B'],
                                          ['C>B>B'],
                                          ['C>B>B'],
                                          ['C>B>C'],
                                          ['C>B>C'],
                                          ['C>B>C'],
                                          ['C>C>A'],
                                          ['C>C>A'],
                                          ['C>C>A'],
                                          ['C>C>B'],
                                          ['C>C>B'],
                                          ['C>C>B'],
                                          ['C>C>C'],
                                          ['C>C>C'],
                                          ['C>C>C']])

data_values3_order2_full['y'] = np.array(['A',
                                          'A',
                                          'A',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C',
                                          'A',
                                          'B',
                                          'C'])

data_values3_order2_full['sample_weight'] = np.array([1000,
                                                      1000,
                                                      1000,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      1000,
                                                      0,
                                                      0,
                                                      1000,
                                                      0,
                                                      0,
                                                      1000,
                                                      0,
                                                      0,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      1000,
                                                      0,
                                                      0,
                                                      1000,
                                                      0,
                                                      0,
                                                      1000,
                                                      0,
                                                      0,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100,
                                                      100])
