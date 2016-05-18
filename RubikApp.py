from Rubik import *

print "Solved cube"
cube = Cube2x2x2()
cube.print_state()
print
print "After R"
cube.r()
cube.print_state()
print
print "After Ri"
cube.ri()
cube.print_state()
print
print "R"
Cube2x2x2.print_rotation_matrix(cube.R)
print
print "Ri"
Cube2x2x2.print_rotation_matrix(cube.Ri)
print
print "R*R"
print Cube2x2x2.print_rotation_matrix(cube.R.dot(cube.R))
print
print "R*R*R"
print Cube2x2x2.print_rotation_matrix(cube.R.dot(cube.R).dot(cube.R))
print
print "R*R*R*R"
print Cube2x2x2.print_rotation_matrix(cube.R.dot(cube.R).dot(cube.R).dot(cube.R))
print
print "original state"
print cube.state
cube.r()
print "after R"
print cube.state
cube.ri()
print "after Ri"
print cube.state
cube.ri()
print "after another Ri"
print cube.state
