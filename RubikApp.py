from Rubik import *
import matplotlib.pyplot as plt

cube = Cube2x2x2()
histogram = {}
cn_sequence = []
cube_sequence = []
turn_sequence = []
skip = 100
N = 5000000
max_cn = 0
last = 10
for i in range(1, N + skip):
    turn = cube.random_turn()
    if i > skip:
        j = i - skip
        cn = cube.correct_neighbors()
        cn_sequence.append(cn)
        cube_sequence.append(cube.state.copy())
        turn_sequence.append(turn)
        if histogram.has_key(cn):
            histogram[cn] += 1
        else:
            histogram[cn] = 1
        if cn > max_cn:
            max_cn = cn
            if j - last > 0:
                max_cn_start = cube_sequence[j - last]
                max_cn_turn_sequence = turn_sequence[j - last:j]
                max_cn_cn_sequence = cn_sequence[j - last:j]
            else:
                max_cn_start = cube_sequence[0]
                max_cn_turn_sequence = turn_sequence[0:i]
                max_cn_cn_sequence = cn_sequence[0:i]
        if cn == 24:
            c = Cube2x2x2()
            c.state = max_cn_start
            print "Cube solved:"
            print c.print_state()
            print max_cn_turn_sequence

for key, value in histogram.iteritems():
    print key, value

plt.plot(max_cn_cn_sequence)
plt.show()








