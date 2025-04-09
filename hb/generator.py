import numpy as np

Ns=[3,4,5,6,7,8,10,20,30,50]

for i in range(10):
    rng=np.random.default_rng()
    blocks=np.arange(Ns[i])+1
    pin=np.random.randint(0,3,Ns[i])
    pin1=blocks[pin==0]
    pin2=blocks[pin==1]
    pin3=blocks[pin==2]
    rng.shuffle(pin1)
    rng.shuffle(pin2)
    rng.shuffle(pin3)
    np.savetxt(f"hb/{i+1}h1p.txt",pin1)
    np.savetxt(f"hb/{i+1}h2p.txt",pin2)
    np.savetxt(f"hb/{i+1}h3p.txt",pin3)
    np.savetxt(f"hb/{i+1}sol.txt",[0])
