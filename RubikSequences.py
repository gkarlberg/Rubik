# coding: utf-8
from Rubik import *

cube = Cube2x2x2()
U = cube.U
R = cube.R
Ui = cube.Ui
Ri = cube.Ri
L = cube.L
Li = cube.Li
D = cube.D
Di = cube.Di
F = cube.F
Fi = cube.Fi
Y = cube.Y
Yi = cube.Yi

lower_layer_ind = [6, 7, 8, 9, 10, 11, 12, 13, 18, 19, 22, 23]
upper_layer_ind = [0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 20, 21]
R = [U, Ui, R, Ri, L, Li, D, Di, F, Fi, Y, Yi]
S = ["U", "Ui", "R", "Ri", "L", "Li", "D", "Di", "F", "Fi", "Y", "Yi"]
solved_state = cube.create_solved_cube()
i = 0
for R1, S1 in zip(R, S):
    for R2, S2 in zip(R, S):
        for R3, S3 in zip(R, S):
            for R4, S4 in zip(R, S):
                for R5, S5 in zip(R, S):
                    for R6, S6 in zip(R, S):
                        for R7, S7 in zip(R, S):
                            for R8, S8 in zip(R, S):
                                T = R1.dot(R2.dot(R3.dot(R4.dot(R5.dot(R6.dot(R7.dot(R8)))))))
                                TU = T.dot(U)
                                T2U = TU.dot(U)
                                T3U = T2U.dot(U)
                                p1 = np.prod(T[lower_layer_ind, lower_layer_ind])
                                p2 = np.prod(T[upper_layer_ind, upper_layer_ind])
                                p3 = np.prod(TU[upper_layer_ind, upper_layer_ind])
                                p4 = np.prod(T2U[upper_layer_ind, upper_layer_ind])
                                p5 = np.prod(T3U[upper_layer_ind, upper_layer_ind])
                                if p1 == 1 and not (p2 == 1 or p3 == 1 or p4 == 1 or p5 == 1):
                                    cube.state = T.dot(solved_state)
                                    cube.print_state()
                                    print S8, S7, S6, S5, S4, S3, S2, S1

print "Done"
