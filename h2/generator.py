import numpy as np
import sol

testCasesN=10
Ws=np.array([5,10,20,30,40,50,60,70,100,100])
Hs=np.array([5,10,20,30,40,50,60,70,100,100])
Ns=np.array([2,3,4,2,10,20,60,10,20,20])
Ts=np.array([10,100,3,1000,200,200,200,100000,100000,100000])

for i in range(testCasesN):
    rng=np.random.default_rng()
    posx=rng.choice(Ws[i],size=Ns[i],replace=False)+1
    posy=rng.choice(Ws[i],size=Ns[i],replace=False)+1
    xory=np.random.randint(0,2,Ns[i])
    dirx=(np.random.randint(0,2,Ns[i])*2-1)*xory
    dirx[posx==1]=1
    dirx[posx==Ws[i]]=-1
    diry=(np.random.randint(0,2,Ns[i])*2-1)*np.logical_not(xory)
    diry[posy==1]=1
    diry[posy==Hs[i]]=-1
    babuk=np.stack([posx,posy,dirx,diry]).T
    solu=sol.main(Ws[i],Hs[i],Ts[i],babuk.copy())
    params=np.array([Ws[i],Hs[i],Ts[i]])
    print(f"Sollution {i+1}: {solu}")
    solution=np.array([solu])
    np.savetxt(f"h2/{i+1}params.txt",params)
    np.savetxt(f"h2/{i+1}babuk.txt",babuk)
    np.savetxt(f"h2/{i+1}sol.txt",solution)