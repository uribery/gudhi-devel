import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import pytest


def test_representations_examples():
    # Disable graphics for testing purposes
    plt.show = lambda: None
    here = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(here + "/../example")
    import diagram_vectorizations_distances_kernels

    return None


from gudhi.representations.metrics import *
from gudhi.representations.kernel_methods import *


def _n_diags(n):
    l = []
    for _ in range(n):
        a = np.random.rand(50, 2)
        a[:, 1] += a[:, 0]  # So that y >= x
        l.append(a)
    return l


def test_multiple():
    l1 = _n_diags(9)
    l2 = _n_diags(11)
    l1b = l1.copy()
    d1 = pairwise_persistence_diagram_distances(l1, e=0.00001, n_jobs=4)
    d2 = BottleneckDistance(epsilon=0.00001).fit_transform(l1)
    d3 = pairwise_persistence_diagram_distances(l1, l1b, e=0.00001, n_jobs=4)
    assert d1 == pytest.approx(d2)
    assert d3 == pytest.approx(d2, abs=1e-5) # Because of 0 entries (on the diagonal)
    d1 = pairwise_persistence_diagram_distances(l1, l2, metric="wasserstein", order=2, internal_p=2)
    d2 = WassersteinDistance(order=2, internal_p=2, n_jobs=4).fit(l2).transform(l1)
    print(d1.shape, d2.shape)
    assert d1 == pytest.approx(d2, rel=.02)
