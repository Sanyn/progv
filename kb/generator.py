import sol
import numpy as np

#i=0
#N=[5,10,20,30,40,50,100]
#while i < 7:
#    stop = True
#    M=np.zeros(N[i])
#    while stop:
#        M=np.random.random([N[i],N[i]])*0.1+0.9
#        M=M-np.diag(np.diag(M))+np.diag([1]*N[i])
#        solu=sol.main(M)
#        print(f"Solution: {solu}")
#        inp=input("Accept: ")
#        if inp=="y":
#            stop=False
#    np.savetxt(f"kb/{i+4}m.txt",M)
#    i+=1

for i in range(10):
    m=np.loadtxt(f"kb/{i+1}m.txt")
    solu=sol.main(m)
    print(f"Solution: {solu}")
    np.savetxt(f"kb/{i+1}sol.txt",solu)
    