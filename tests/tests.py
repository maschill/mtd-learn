from mtdlearn.mtd import MTD
from mtdlearn.preprocessing import PathEncoder, ChainAggregator
from mtdlearn.datasets import data_values3_order2_full as data
from mtdlearn.datasets import generate_data
import pytest
import numpy as np
import logging

logger = logging.getLogger(__name__)

x = data['x']
y = data['y']
sample_weight = data['sample_weight']


def test_dataset():
    assert x.shape[0] == y.shape[0]
    assert x.shape[0] == sample_weight.shape[0]


def test_generate_data1():
    x_gen, y_gen = generate_data(('A', 'B', 'C'), '>', 1, 10, 3, 1000, 0.95)
    assert x_gen.shape[0] == y_gen.shape[0]
    assert y_gen.shape[0] == 1000
    assert max([len(i[0].split('>')) for i in x_gen]) <= 10
    assert min([len(i[0].split('>')) for i in x_gen]) >= 1


def test_generate_data2():
    x_gen, y_gen = generate_data(('A', 'B', 'C', 'D'), '*', 5, 5, 5, 100, 1.0)
    assert x_gen.shape[0] == y_gen.shape[0]
    assert y_gen.shape[0] == 100
    assert max([len(i[0].split('*')) for i in x_gen]) == 5
    assert min([len(i[0].split('*')) for i in x_gen]) == 5
    for i, row in enumerate(x_gen):
        assert row[0].split('*')[0] == y_gen[i]


def test_path_encoder1():
    x_gen, y_gen = generate_data(('A', 'B', 'C'), '*', 1, 3, 3, 100, 0.95)
    pe = PathEncoder(3, '*', 'X')
    pe.fit(x_gen, y_gen)
    x_tr, y_tr = pe.transform(x_gen, y_gen)
    x_gen_rep, y_gen_rep = pe.inverse_transform(x_tr, y_tr)

    assert list(pe.label_dict.keys()) == ['A', 'B', 'C', 'X']
    assert list(pe.label_dict.values()) == [0, 1, 2, 3]
    assert list(pe.label_dict_inverse.values()) == ['A', 'B', 'C', 'X']
    assert list(pe.label_dict_inverse.keys()) == [0, 1, 2, 3]
    assert x_tr.shape[0] == x_gen.shape[0]
    assert y_tr.shape[0] == y_gen.shape[0]
    assert x_tr.shape[1] == 3
    assert list(np.unique(x_tr)) == [0, 1, 2, 3]
    assert list(np.unique(y_tr)) == [0, 1, 2]
    assert x_gen.shape == x_gen_rep.shape
    assert y_gen.shape == y_gen_rep.shape
    assert list(np.unique(y_gen_rep)) == ['A', 'B', 'C']
    assert len(list(set(x_gen_rep[0][0].split('*')) & {'A', 'B', 'C', 'X'})) > 0


def test_path_encoder2():
    x_gen, y_gen = generate_data(('A', 'B', 'C', 'D'), '>', 1, 10, 3, 300, 0.95)
    pe = PathEncoder(5, '>', 'X')
    pe.fit(x_gen, y_gen)
    x_tr, y_tr = pe.transform(x_gen, y_gen)
    x_gen_rep, y_gen_rep = pe.inverse_transform(x_tr, y_tr)

    assert list(pe.label_dict.keys()) == ['A', 'B', 'C', 'D', 'X']
    assert list(pe.label_dict.values()) == [0, 1, 2, 3, 4]
    assert list(pe.label_dict_inverse.values()) == ['A', 'B', 'C', 'D', 'X']
    assert list(pe.label_dict_inverse.keys()) == [0, 1, 2, 3, 4]
    assert x_tr.shape[0] == x_gen.shape[0]
    assert y_tr.shape[0] == y_gen.shape[0]
    assert x_tr.shape[1] == 5
    assert list(np.unique(x_tr)) == [0, 1, 2, 3, 4]
    assert list(np.unique(y_tr)) == [0, 1, 2, 3]
    assert x_gen.shape == x_gen_rep.shape
    assert y_gen.shape == y_gen_rep.shape
    assert list(np.unique(y_gen_rep)) == ['A', 'B', 'C', 'D']
    assert len(list(set(x_gen_rep[0][0].split('>')) & {'A', 'B', 'C', 'D', 'X'})) > 0


def test_chain_aggregator1():
    x_gen = np.array([[0, 0], [0, 1]])
    y_gen = np.array([0, 1])
    ca = ChainAggregator()
    result = ca.aggregate_chain(x_gen, y_gen)
    assert np.array_equal(result, np.array([1, 0, 0, 1, 0, 0, 0, 0]))


def test_chain_aggregator2():
    x_gen = np.array([[1, 0, 0], [2, 2, 2]])
    y_gen = np.array([1, 2])
    sample_weight_gen = np.array([100, 99])
    ca = ChainAggregator()
    result = ca.aggregate_chain(x_gen, y_gen, sample_weight_gen)
    assert result[28] == 100
    assert result[80] == 99
    assert result.shape == (81,)
    assert result.sum() == 199


def test_create_indexes():
    mtd = MTD(4, 3)
    assert len(mtd.indexes_) == 256


def test_manual_exp_max():
    transition_matrices = np.array([[[0.4, 0.6],
                                     [0.7, 0.3]],
                                    [[0.1, 0.9],
                                     [0.5, 0.5]]])

    lambdas = np.array([0.4, 0.6])

    indexes = [(0, 0, 0),
               (0, 0, 1),
               (0, 1, 0),
               (0, 1, 1),
               (1, 0, 0),
               (1, 0, 1),
               (1, 1, 0),
               (1, 1, 1)]

    expected_array = np.array([[8 / 11, 3 / 11],
                               [12 / 39, 27 / 39],
                               [8 / 23, 15 / 23],
                               [12 / 27, 15 / 27],
                               [14 / 17, 3 / 17],
                               [2 / 11, 9 / 11],
                               [14 / 29, 15 / 29],
                               [2 / 7, 5 / 7]])

    mtd = MTD(2, 2)

    expectation_matrix = mtd._expectation_step(2, 2, indexes, transition_matrices, lambdas)[0]

    assert np.isclose((expectation_matrix - expected_array), np.zeros((8, 2))).min()


def test_ex_max():

    for seed in range(20):
        np.random.seed(seed)
        pe = PathEncoder(2)
        pe.fit(x, y)
        x_tr, y_tr = pe.transform(x, y)
        mtd = MTD(3, 2, verbose=0, number_of_initiations=1)
        mtd.fit(x_tr, y_tr)
        assert mtd.lambdas.shape == (2,)
        assert np.isclose(sum(mtd.lambdas), 1.0)
        assert max(mtd.lambdas) <= 1
        assert min(mtd.lambdas) >= 0
        assert np.isclose(sum(mtd.transition_matrices[0, 0, :]), 1.0)
        assert mtd.transition_matrices.shape == (2, 3, 3)
        assert mtd.transition_matrices.min() >= 0
        assert mtd.transition_matrices.max() <= 1


def test_create_markov():
    pe = PathEncoder(2)
    pe.fit(x, y)
    x_tr, y_tr = pe.transform(x, y)
    mtd = MTD(3, 2, verbose=0)
    mtd.fit(x_tr, y_tr)
    assert mtd.transition_matrix.max() <= 1.0
    assert mtd.transition_matrix.min() >= 0.0
    assert np.isclose(mtd.transition_matrix.sum(1).max(), 1.0)
    assert mtd.transition_matrix.shape == (9, 3)


def test_init_method_error():

    with pytest.raises(ValueError):
        mtd = MTD(4, 3, init_method='a')
