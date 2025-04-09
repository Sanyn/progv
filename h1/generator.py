import numpy as np
import sol

testCasesN=10

for i in range(testCasesN):
    r = np.loadtxt(f"h3/{i+1}r.txt")
    l = np.loadtxt(f"h3/{i+1}l.txt")
    solution=sol.main(r,l)
    print(f"Sollution for case {i+1}: {solution}")
    np.savetxt(f"h3/{i+1}sol.txt",[solution])