import numpy as np

def loadParams(problem,number):
    if problem == "k1":
        params=np.loadtxt(f"k1/{number}params.txt",dtype=int)
        babuk=np.loadtxt(f"k1/{number}babuk.txt",dtype=int)
        return *params, babuk
    if problem == "k2":
        r=np.loadtxt(f"k2/{number}r.txt",dtype=int)
        m=np.loadtxt(f"k2/{number}m.txt",dtype=int)
        return r, m
    if problem == "k3":
        r=np.loadtxt(f"k3/{number}r.txt",dtype=int)
        l=np.loadtxt(f"k3/{number}l.txt",dtype=int)
        return r,l
    if problem == "kb":
        m=np.loadtxt(f"kb/{number}m.txt",dtype=float)
        return [m]
    if problem == "h1":
        r=np.loadtxt(f"h1/{number}r.txt",dtype=int)
        l=np.loadtxt(f"h1/{number}l.txt",dtype=int)
        return r,l
    if problem == "h2":
        params=np.loadtxt(f"h2/{number}params.txt",dtype=int)
        babuk=np.loadtxt(f"h2/{number}babuk.txt",dtype=int)
        return *params, babuk
    if problem == "h3":
        params=np.loadtxt(f"h3/{number}params.txt",dtype=int)
        dobozok=np.loadtxt(f"h3/{number}dob.txt",dtype=int)
        return *params, dobozok
    if problem == "hb":
        pin1=np.loadtxt(f"hb/{number}h1p.txt",dtype=int)
        if pin1.ndim == 0:
            pin1=pin1[np.newaxis]
        pin2=np.loadtxt(f"hb/{number}h2p.txt",dtype=int)
        if pin2.ndim == 0:
            pin2=pin2[np.newaxis]
        pin3=np.loadtxt(f"hb/{number}h3p.txt",dtype=int)
        if pin3.ndim == 0:
            pin3=pin3[np.newaxis]
        return [[pin1,pin2,pin3]]
def loadSol(problem,number):
    solution=np.loadtxt(f"{problem}/{number}sol.txt",dtype=int)
    return solution

def loadTimeLim(problem):
    timelim=np.loadtxt(f"{problem}/timelim.txt")
    return timelim