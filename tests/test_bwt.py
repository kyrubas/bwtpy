import pytest
import numpy as np
import pickle
from lib.utils import rotate_array, sort_array, final_btw_transform, reverse_bwt_transform

with open("tests/data/rotations.pkl", 'rb') as fi:
    rotation_data = pickle.load(fi)
with open("tests/data/sorted_array.pkl", 'rb') as fi:
    sorted_data = pickle.load(fi)
with open("tests/data/final_bwt.pkl", "rb") as fi:
    final_transform = pickle.load(fi)

@pytest.mark.parametrize("test_input,expected",[
    ("ATTAGAGGAGGAGGACAGAAAACCATTTCCCCATATTATAACC", rotation_data)
    ]
)
def test_rotation(test_input,expected):
    assert np.all(rotate_array(test_input) == expected)

@pytest.mark.parametrize("test_input,expected",[
    (rotation_data, sorted_data)
    ]
)
def test_sortedrotation(test_input,expected):
    assert np.all(sort_array(test_input) == expected)

@pytest.mark.parametrize("test_input,expected",[
    (sorted_data, final_transform)
    ]
)
def test_final_bwt_transform(test_input, expected):
    assert np.all(final_btw_transform(test_input) == expected)
    
@pytest.mark.parametrize("test_input,expected", [
    (final_transform, "ATTAGAGGAGGAGGACAGAAAACCATTTCCCCATATTATAACC")
    ]
)
def test_reverse_bwt(test_input,expected):
    assert reverse_bwt_transform(test_input) == expected