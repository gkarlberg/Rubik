from Rubik import *

print "Solved cube"
cube = Cube2x2x2()
cube.print_state()
print
print "After LiUiLU"
cube.li()
cube.ui()
cube.l()
cube.u()
cube.print_state()

