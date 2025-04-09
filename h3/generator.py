import numpy as np
import sol

ksz=[15,50,100,200,400,1000,2000,5000,10000,10000]
fd=[7,50,100,200,400,1000,2000,5000,10000,10000]
dobozmax=[7,20,40,60,80,100,100,100,100,100]
msz=[3,5,5,10,10,10,10,20,20,20]

for i in range(10):
    sz=np.random.randint(0,msz[i],[fd[i]])
    tart=np.random.randint(1,dobozmax[i]+1,[fd[i]])
    dobz=np.stack([sz,tart]).T
    solu=sol.main(ksz[i],msz[i],dobz)
    print(f"Solution {i+1}: {solu}")
    np.savetxt(f"h3/{i+1}dob.txt",dobz)
    np.savetxt(f"h3/{i+1}params.txt",[ksz[i],msz[i]])
    np.savetxt(f"h3/{i+1}sol.txt",[solu])
