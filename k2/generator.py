import numpy as np
import sol


tests = 10
maxd=[7,10,10,10,2,4,10,10,10,10]
perd=[3,1,7,4,1,1,2,3,2,6]
N=[6,6,6,100,100,100,200,200,200,200]
M=[7,7,7,200,200,200,500,500,500,500]

for i in range(tests):
    p=perd[0]
    map=np.random.randint(0,maxd[i]+1,[N[i],M[i]])
    solutions=sol.main(p,map)
    print(f"Case1 sol: {solutions}")
    np.savetxt(f"k2/{i+1}r.txt",[p])
    np.savetxt(f"k2/{i+1}m.txt",map)
    np.savetxt(f"k2/{i+1}sol.txt",[solutions[0]])
    