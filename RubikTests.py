import unittest
from Rubik import *
import numpy as np


class Tests(unittest.TestCase):
    def test_R_times_Ri(self):
        cube = Cube2x2x2()
        I = cube.R.dot(cube.Ri)
        self.assertTrue(np.array_equal(I, np.identity(24)))

    def test_U_times_Ui(self):
        cube = Cube2x2x2()
        I = cube.U.dot(cube.Ui)
        self.assertTrue(np.array_equal(I, np.identity(24)))

    def test_L_times_Li(self):
        cube = Cube2x2x2()
        I = cube.L.dot(cube.Li)
        self.assertTrue(np.array_equal(I, np.identity(24)))

    def test_6xRURiUi(self):
        cube = Cube2x2x2()
        initial_state = cube.state
        for i in range(0, 6):
            cube.r()
            cube.u()
            cube.ri()
            cube.ui()
        self.assertTrue(np.array_equal(initial_state, cube.state))

    def test_6xLiUiLU(self):
        cube = Cube2x2x2()
        initial_state = cube.state
        for i in range(0, 6):
            cube.li()
            cube.ui()
            cube.l()
            cube.u()
        self.assertTrue(np.array_equal(initial_state, cube.state))