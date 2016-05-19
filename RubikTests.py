import unittest
from Rubik import *
import numpy as np


class Tests(unittest.TestCase):
    def test_R(self):
        R = Cube2x2x2.generate_r()
        Ri = Cube2x2x2.generate_ri()
        I = R.dot(Ri)
        self.assertTrue(np.array_equal(I, np.identity(24)))
        I = R.dot(R).dot(R).dot(R)
        self.assertTrue(np.array_equal(I, np.identity(24)))
        I = Ri.dot(Ri).dot(Ri).dot(Ri)
        self.assertTrue(np.array_equal(I, np.identity(24)))

    def test_U(self):
        U = Cube2x2x2.generate_u()
        Ui = Cube2x2x2.generate_ui()
        I = U.dot(Ui)
        self.assertTrue(np.array_equal(I, np.identity(24)))
        I = U.dot(U).dot(U).dot(U)
        self.assertTrue(np.array_equal(I, np.identity(24)))
        I = Ui.dot(Ui).dot(Ui).dot(Ui)
        self.assertTrue(np.array_equal(I, np.identity(24)))

    def test_L(self):
        L = Cube2x2x2.generate_l()
        Li = Cube2x2x2.generate_li()
        I = L.dot(Li)
        self.assertTrue(np.array_equal(I, np.identity(24)))
        I = L.dot(L).dot(L).dot(L)
        self.assertTrue(np.array_equal(I, np.identity(24)))
        I = Li.dot(Li).dot(Li).dot(Li)
        self.assertTrue(np.array_equal(I, np.identity(24)))

    def test_D(self):
        D = Cube2x2x2.generate_d()
        Di = Cube2x2x2.generate_di()
        I = D.dot(Di)
        self.assertTrue(np.array_equal(I, np.identity(24)))
        I = D.dot(D).dot(D).dot(D)
        self.assertTrue(np.array_equal(I, np.identity(24)))
        I = Di.dot(Di).dot(Di).dot(Di)
        self.assertTrue(np.array_equal(I, np.identity(24)))

    def test_URLDDiLiRiUi(self):
        U = Cube2x2x2.generate_u()
        R = Cube2x2x2.generate_r()
        L = Cube2x2x2.generate_l()
        D = Cube2x2x2.generate_d()
        Ui = Cube2x2x2.generate_ui()
        Ri = Cube2x2x2.generate_ri()
        Li = Cube2x2x2.generate_li()
        Di = Cube2x2x2.generate_di()
        I = U.dot(R).dot(L).dot(D).dot(Di).dot(Li).dot(Ri).dot(Ui)
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