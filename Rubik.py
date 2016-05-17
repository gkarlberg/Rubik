import numpy as np


class Cube2x2x2:

    def __init__(self):
        self.state = Cube2x2x2.create_solved_cube()
        self.R = Cube2x2x2.generate_r()
        self.Ri = Cube2x2x2.generate_ri()

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
    def create_solved_cube():
        return np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5], 'int')

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
            if item == 0:
                c.append("W")
            if item == 1:
                c.append("B")
            if item == 2:
                c.append("Y")
            if item == 3:
                c.append("G")
            if item == 4:
                c.append("R")
            if item == 5:
                c.append("O")

        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2}".format("", "", c[0], c[1], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2}".format("", "", c[2], c[3], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2}".format(c[16], c[18], c[4], c[5], c[20], c[21])
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2}".format(c[17], c[19], c[6], c[7], c[22], c[23])
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2}".format("", "", c[8], c[9], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2}".format("", "", c[10], c[11], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2}".format("", "", c[12], c[13], "", "")
        print "{0:2}{1:2}{2:2}{3:2}{4:2}{5:2}".format("", "", c[14], c[15], "", "")

    def r(self):
        self.state = self.R.dot(self.state)

    def ri(self):
        self.state = self.Ri.dot(self.state)
