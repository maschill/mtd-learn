from mtdlearn import MTD
import pytest
import numpy as np


def test_create_indexes():
    mtd = MTD(4, 3)
    assert len(mtd.indexes) == 256


def test_input_len_error():
    
    with pytest.raises(ValueError):
        mtd = MTD(4, 3, verbose=0)
        mtd.fit(np.array([1, 2, 3]))


def test_input_len_no_error():
    mtd = MTD(3, 2, verbose=0)
    mtd.fit(np.array([i for i in range(27)]))


def test_ex_max():

    for seed in range(100):
        np.random.seed(seed)
        mtd = MTD(3, 2, verbose=0, init_num=1)
        mtd.fit(np.random.randint(0, 100, 27, ))
        assert mtd.lambdas_.shape == (2, )
        assert np.isclose(sum(mtd.lambdas_), 1.0)
        assert max(mtd.lambdas_) <= 1
        assert min(mtd.lambdas_) >= 0
        assert np.isclose(sum(mtd.transition_matrices_[0, 0, :]), 1.0)
        assert mtd.transition_matrices_.shape == (2, 3, 3)
        assert mtd.transition_matrices_.min() >= 0
        assert mtd.transition_matrices_.max() <= 1


def test_create_markov():
    mtd = MTD(3, 2, verbose=0)
    mtd.fit(np.array([i for i in range(27)]))
    mtd.create_markov()
    assert mtd.transition_matrix_.max() <= 1.0
    assert mtd.transition_matrix_.min() >= 0.0
    assert np.isclose(mtd.transition_matrix_.sum(1).max(), 1.0)
    assert mtd.transition_matrix_.shape == (9, 3)


def test_aic():
    mtd1 = MTD(3, 2, verbose=0)
    mtd1.fit(np.array([i for i in range(27)]))
    mtd1._calculate_aic()
    mtd2 = MTD(3, 3, verbose=0)
    mtd2.fit(np.array([i for i in range(81)]))
    mtd2._calculate_aic()
    assert mtd1.aic < mtd2.aic


def test_criterion():
    n_dimensions = 2
    order = 3
    m1 = MTD(n_dimensions, order, verbose=0)
    x = np.array([[100, 900],
                  [100, 900],
                  [900, 100],
                  [900, 100],
                  [100, 900],
                  [100, 900],
                  [900, 100],
                  [900, 100]]).reshape(-1, 1).ravel()  # this is generated by MTD model with lambdas = [0, 1, 0]
    m1.fit(x)
    m1._calculate_aic()

    order = 2
    m2 = MTD(n_dimensions, order, verbose=0)
    x = x.reshape(2, -1).sum(0)
    m2.fit(x)
    m2._calculate_aic()

    order = 1
    m3 = MTD(n_dimensions, order, verbose=0)
    x = x.reshape(2, -1).sum(0)
    m3.fit(x)
    m3._calculate_aic()

    assert m3.aic > m1.aic > m2.aic


def test_one_fit_random():

    n_dimensions = 2
    order = 3
    mtd = MTD(n_dimensions, order, verbose=0)
    x = np.array([[100, 900],
                  [100, 900],
                  [900, 100],
                  [900, 100],
                  [100, 900],
                  [100, 900],
                  [900, 100],
                  [900, 100]]).reshape(-1, 1).ravel()

    n_direct = np.array([[[2000., 2000.],
                          [2000., 2000.]],
                          [[400., 3600.],
                          [3600.,  400.]],
                          [[2000., 2000.],
                          [2000., 2000.]]])

    log_likelihood, lambdas, transition_matrices = mtd.fit_one(x,
                                                               mtd.indexes,
                                                               order,
                                                               n_dimensions,
                                                               0.1,
                                                               100,
                                                               0,
                                                               'random',
                                                               n_direct)

    assert lambdas[0] < lambdas[1]
    assert lambdas[2] < lambdas[1]


def test_one_fit_flat():

    n_dimensions = 2
    order = 3
    mtd = MTD(n_dimensions, order, verbose=0)
    x = np.array([[100, 900],
                  [100, 900],
                  [900, 100],
                  [900, 100],
                  [100, 900],
                  [100, 900],
                  [900, 100],
                  [900, 100]]).reshape(-1, 1).ravel()

    n_direct = np.array([[[2000., 2000.],
                          [2000., 2000.]],
                          [[400., 3600.],
                          [3600.,  400.]],
                          [[2000., 2000.],
                          [2000., 2000.]]])

    log_likelihood, lambdas, transition_matrices = mtd.fit_one(x,
                                                               mtd.indexes,
                                                               order,
                                                               n_dimensions,
                                                               0.1,
                                                               100,
                                                               0,
                                                               'flat',
                                                               n_direct)

    assert lambdas[0] < lambdas[1]
    assert lambdas[2] < lambdas[1]

