import numpy as np


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
        t = [0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 20, 21]
        f = [2, 0, 3, 1, 20, 21, 17, 16, 4, 5, 15, 14]
        for i, j in zip(t, f):
            r[i, [i, j]] = v
        return r

    @staticmethod
    def generate_di():
        r = np.identity(24, 'int')
        v = np.array([0, 1], 'int')
        t = [0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 20, 21]
        f = [1, 3, 0, 2, 16, 17, 21, 20, 15, 14, 4, 5]
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
