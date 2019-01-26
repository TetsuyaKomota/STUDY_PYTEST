# coding utf-8
import sys
sys.path.append("/home/tetsuya_win10bash/STUDY_PYTEST")
from src.sample import func

def test_true():
    assert (1, 2, 3) == (1, 2, 3)

def test_sample_func():
    assert func(7) == 5040
