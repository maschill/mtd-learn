import numpy as np
from ..mtd import _ChainBaseEstimator
from itertools import product


class ChainGenerator(_ChainBaseEstimator):

    def __init__(self, values, sep, max_len, order):
        super().__init__(len(values), order)
        self.values = values
        self.sep = sep
        self.max_len = max_len
        self.order = order
        self.lambdas = None
        self.transition_matrices = None
        self._generate_mtd_model()
        self._create_markov()
        self._label_dict = {i: j for i, j in enumerate(values)}

    def generate_data(self, samples):

        x = []
        y = []
        cnt = 0
        while cnt < samples:
            cnt += 1
            seq_list = np.random.choice(list(self._label_dict.keys()), self.order)
            x.append(seq_list)

        x = np.array(x).reshape(-1, self.order)
        y = self.predict_random(x)

        return x, y

    def predict_random(self, x):
        prob = self.predict_proba(x)
        x_new = []
        for i in prob:
            x_new.append(np.random.choice(self.values, p=i))
        return x_new

    def _generate_mtd_model(self, lambdas=None, transition_matrices=None):
        if lambdas is None:
            lambdas = np.random.rand(self.order)
            self.lambdas = lambdas / lambdas.sum()
        if transition_matrices is None:
            transition_matrices = np.random.rand(self.order, self.n_dimensions, self.n_dimensions)
            self.transition_matrices = transition_matrices / transition_matrices.sum(2).reshape(self.order,
                                                                                                self.n_dimensions, 1)

    def _create_markov(self):

        array_coords = product(range(self.n_dimensions), repeat=self.order)

        transition_matrix_list = []
        for idx in array_coords:
            t_matrix_part = np.array([self.transition_matrices[i, idx[i], :] for i in range(self.order)]).T
            transition_matrix_list.append(np.dot(t_matrix_part,
                                                 self.lambdas))
        self.transition_matrix = np.array(transition_matrix_list)


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
