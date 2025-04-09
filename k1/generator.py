import numpy as np
import sol

testCasesN=10
Ls=np.array([5,10,20,30,40,50,60,70,100,100])
Ns=np.array([2,3,4,2,10,2,8,10,2,2])
Ts=np.array([10,100,3,1000,200,200,200,20,100000,20])

for i in range(testCasesN):
    rng=np.random.default_rng()
    pos=rng.choice(Ls[i],size=Ns[i],replace=False)+1
    dir=np.random.randint(0,2,Ns[i])*2-1
    dir[pos==1]=1
    dir[pos==Ls[i]]=-1
    babuk=np.stack([pos,dir]).T
    solu1=sol.main(Ls[i],Ts[i],babuk.copy())
    solu2=sol.main2(Ls[i],Ts[i],babuk.copy())
    params=np.array([Ls[i],Ts[i]])
    if(solu1!=solu2):
        print("SOLLUTION MISMATCH")
        print(params)
        print(babuk)
        break
    print(f"Sollution {i+1}: {solu1}")
    solution=np.array([solu1])
    np.savetxt(f"k1/{i+1}params.txt",params)
    np.savetxt(f"k1/{i+1}babuk.txt",babuk)
    np.savetxt(f"k1/{i+1}sol.txt",solution)