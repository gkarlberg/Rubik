import unittest
from Rubik import *
import numpy as np


class Tests(unittest.TestCase):
    def test_R_times_Ri(self):
        cube = Cube2x2x2()
        I = cube.R.dot(cube.Ri)
        self.assertTrue(np.array_equal(I, np.identity(24)))
