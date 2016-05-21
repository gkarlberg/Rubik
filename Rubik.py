import numpy as np
import random


class Cube2x2x2:

    def __init__(self):
        self.state = Cube2x2x2.create_solved_cube()
        self.R = Cube2x2x2.generate_r()
        self.Ri = Cube2x2x2.generate_ri()
        self.L = Cube2x2x2.generate_l()
        self.Li = Cube2x2x2.generate_li()
        self.U = Cube2x2x2.generate_u()
        self.Ui = Cube2x2x2.generate_ui()
        self.D = Cube2x2x2.generate_d()
        self.Di = Cube2x2x2.generate_di()
        self.Y = self.U.dot(self.Di)
        self.Yi = self.Ui.dot(self.D)
        self.X = self.R.dot(self.Li)
        self.Xi = self.Ri.dot(self.L)
        self.Z = self.Yi.dot(self.Xi).dot(self.Y)
        self.Zi = self.Y.dot(self.Xi).dot(self.Yi)
        self.F = self.Yi.dot(self.L).dot(self.Y)
        self.Fi = self.Yi.dot(self.Li).dot(self.Y)

    @staticmethod
    def generate_ri():
        r = np.identity(24, 'int')
        v = np.array([0, 1], 'int')
        t = [1, 3, 5, 7, 9, 11, 13, 15, 20, 21, 22, 23]
        f = [13, 15, 1, 3, 5, 7, 9, 11, 21, 23, 20, 22]
        for i, j in zip(t, f):
            r[i, [i, j]] = v
        return r

    @staticmethod
    def generate_r():
        r = np.identity(24, 'int')
        v = np.array([0, 1], 'int')
        t = [1, 3, 5, 7, 9, 11, 13, 15, 20, 21, 22, 23]
        f = [5, 7, 9, 11, 13, 15, 1, 3, 22, 20, 23, 21]
        for i, j in zip(t, f):
            r[i, [i, j]] = v
        return r

    @staticmethod
    def generate_l():
        r = np.identity(24, 'int')
        v = np.array([0, 1], 'int')
        t = [0, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 19]
        f = [12, 14, 0, 2, 4, 6, 8, 10, 18, 16, 19, 17]
        for i, j in zip(t, f):
            r[i, [i, j]] = v
        return r

    @staticmethod
    def generate_li():
        r = np.identity(24, 'int')
        v = np.array([0, 1], 'int')
        t = [0, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 19]
        f = [4, 6, 8, 10, 12, 14, 0, 2, 17, 19, 16, 18]
        for i, j in zip(t, f):
            r[i, [i, j]] = v
        return r

    @staticmethod
    def generate_u():
        r = np.identity(24, 'int')
        v = np.array([0, 1], 'int')
        t = [0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 20, 21]
        f = [2, 0, 3, 1, 20, 21, 17, 16, 4, 5, 15, 14]
        for i, j in zip(t, f):
            r[i, [i, j]] = v
        return r

    @staticmethod
    def generate_ui():
        r = np.identity(24, 'int')
        v = np.array([0, 1], 'int')
        t = [0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 20, 21]
        f = [1, 3, 0, 2, 16, 17, 21, 20, 15, 14, 4, 5]
        for i, j in zip(t, f):
            r[i, [i, j]] = v
        return r

    @staticmethod
    def generate_d():
        r = np.identity(24, 'int')
        v = np.array([0, 1], 'int')
        t = [6, 7, 8, 9, 10, 11, 12, 13, 18, 19, 22, 23]
        f = [18, 19, 10, 8, 11, 9, 23, 22, 13, 12, 6, 7]
        for i, j in zip(t, f):
            r[i, [i, j]] = v
        return r

    @staticmethod
    def generate_di():
        r = np.identity(24, 'int')
        v = np.array([0, 1], 'int')
        t = [6, 7, 8, 9, 10, 11, 12, 13, 18, 19, 22, 23]
        f = [22, 23, 9, 11, 8, 10, 19, 18, 6, 7, 13, 12]
        for i, j in zip(t, f):
            r[i, [i, j]] = v
        return r

    @staticmethod
    def create_solved_cube():
        return np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], 'int')

    @staticmethod
    def print_rotation_matrix(r):
        for i in range(0, 24):
            print "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19}" \
                  " {20} {21} {22} {23}"\
                .format(r[i, 0], r[i, 1], r[i, 2], r[i, 3], r[i, 4], r[i, 5], r[i, 6], r[i, 7], r[i, 8],
                        r[i, 9], r[i, 10], r[i, 11], r[i, 12], r[i, 13], r[i, 14], r[i, 15], r[i, 16], r[i, 17],
                        r[i, 18], r[i, 19], r[i, 20], r[i, 21], r[i, 22], r[i, 23])

    @staticmethod
    def color(item):
        if item < 4:
            return 'W'
        elif item < 8:
            return 'B'
        elif item < 12:
            return 'Y'
        elif item < 16:
            return 'G'
        elif item < 20:
            return 'R'
        else:
            return 'O'

    def correct_neighbors(self):
        neighbors = 0
        for i in range(0, 6):
            c0 = Cube2x2x2.color(self.state[i*4 + 0])
            c1 = Cube2x2x2.color(self.state[i*4 + 1])
            c2 = Cube2x2x2.color(self.state[i*4 + 2])
            c3 = Cube2x2x2.color(self.state[i*4 + 3])
            if c0 == c1 and c0 == c2 and c3 == c2 and c3 == c1:
                neighbors += 4
            elif (c0 == c1 and c0 == c2) or (c3 == c2 and c3 == c1) or (c0 == c1 and c2 == c3) or (c0 == c2 and c3 == c1):
                neighbors += 2
            elif c0 == c1 or c1 == c3 or c3 == c2 or c2 == c1:
                neighbors += 1
        return neighbors

    def is_same_state(self, state):
        # First side
        self_initial = self.state.copy()
        if np.array_equal(self.state, state):
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        self.x()
        # Second side
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        # Third side
        self.y()
        self.x()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        # Fourth side
        self.y()
        self.x()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        # Fifth side
        self.y()
        self.x()
        self.z()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        # Sixth side
        self.y()
        self.z()
        self.z()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.y()
        if np.array_equal(self.state, state):
            self.state = self_initial
            return True
        self.state = self_initial
        return False

    def state_to_string(self):
        state_as_string = ""
        for i in range(0, 24):
            state_as_string += str(self.state) + " "
        return state_as_string

    def print_state(self):
        c = []
        for item in self.state:
            if item < 4:
                c.append("W")
            elif item < 8:
                c.append("B")
            elif item < 12:
                c.append("Y")
            elif item < 16:
                c.append("G")
            elif item < 20:
                c.append("R")
            else:
                c.append("O")

        print "    Cube           Coordinates in vector      "
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2} <-> {6:3}{7:3}{8:3}{9:3}{10:3}{11:3}"\
            .format("", "", c[0], c[1], "", "","", "", self.state[0], self.state[1], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2} <-> {6:3}{7:3}{8:3}{9:3}{10:3}{11:3}"\
            .format("", "", c[2], c[3], "", "","", "", self.state[2], self.state[3], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2} <-> {6:3}{7:3}{8:3}{9:3}{10:3}{11:3}"\
            .format(c[16], c[17], c[4], c[5], c[20], c[21], self.state[16], self.state[17],
                    self.state[4], self.state[5], self.state[20], self.state[21])
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2} <-> {6:3}{7:3}{8:3}{9:3}{10:3}{11:3}"\
            .format(c[18], c[19], c[6], c[7], c[22], c[23], self.state[18], self.state[19],
                    self.state[6], self.state[7], self.state[22], self.state[23])
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2} <-> {6:3}{7:3}{8:3}{9:3}{10:3}{11:3}"\
            .format("", "", c[8], c[9], "", "", "", "", self.state[8], self.state[9], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2} <-> {6:3}{7:3}{8:3}{9:3}{10:3}{11:3}"\
            .format("", "", c[10], c[11], "", "", "", "", self.state[10], self.state[11], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2} <-> {6:3}{7:3}{8:3}{9:3}{10:3}{11:3}"\
            .format("", "", c[12], c[13], "", "", "", "", self.state[12], self.state[13], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2} <-> {6:3}{7:3}{8:3}{9:3}{10:3}{11:3}"\
            .format("", "", c[14], c[15], "", "", "", "", self.state[14], self.state[15], "", "")

    def r(self):
        self.state = self.R.dot(self.state)

    def ri(self):
        self.state = self.Ri.dot(self.state)

    def l(self):
        self.state = self.L.dot(self.state)

    def li(self):
        self.state = self.Li.dot(self.state)

    def u(self):
        self.state = self.U.dot(self.state)

    def ui(self):
        self.state = self.Ui.dot(self.state)

    def d(self):
        self.state = self.D.dot(self.state)

    def di(self):
        self.state = self.Di.dot(self.state)

    def f(self):
        self.state = self.F.dot(self.state)

    def fi(self):
        self.state = self.Fi.dot(self.state)

    def y(self):
        self.state = self.Y.dot(self.state)

    def yi(self):
        self.state = self.Yi.dot(self.state)

    def x(self):
        self.state = self.X.dot(self.state)

    def xi(self):
        self.state = self.Xi.dot(self.state)

    def z(self):
        self.state = self.Z.dot(self.state)

    def zi(self):
        self.state = self.Zi.dot(self.state)

    def random_turn(self):
        method = random.randint(1, 10)
        if method == 1:
            self.r()
            return "R"
        if method == 2:
            self.ri()
            return "Ri"
        if method == 3:
            self.l()
            return "L"
        if method == 4:
            self.li()
            return "Li"
        if method == 5:
            self.u()
            return "U"
        if method == 6:
            self.ui()
            return "Ui"
        if method == 7:
            self.d()
            return "D"
        if method == 8:
            self.di()
            return "Di"
        if method == 9:
            self.f()
            return "F"
        if method == 10:
            self.fi()
            return "Fi"






