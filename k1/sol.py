import numpy as np

def main(length, maxtime, babuk):
    dists1=babuk[np.newaxis,:,0]-babuk[:,np.newaxis,0]
    dists2=babuk[np.newaxis,:,0]+babuk[:,np.newaxis,0]
    dirs1 = babuk[np.newaxis,:,1]+babuk[:,np.newaxis,1]
    dirs2 = babuk[np.newaxis,:,1]-babuk[:,np.newaxis,1]
    dif1 = dists1/dirs2
    dif1p=dif1[dif1>0]
    dif1p=dif1p[np.logical_not(np.isinf(dif1p))]
    dif1n=dif1[dif1<0]
    dif1n=dif1n[np.logical_not(np.isinf(dif1n))]
    if dif1p.size==0:
        dif1p=-2*length
    if dif1n.size==0:
        dif1n=-2*length
    sol1=-np.max(dif1n)
    sol2=length-1-np.max(dif1p)
    dif2=dists2/dirs1*(dists1!=0)
    dif2p=dif2[dif2>0]
    dif2p=dif2p[np.logical_not(np.isinf(dif2p))]
    dif2n=dif2[dif2<0]
    dif2n=dif2n[np.logical_not(np.isinf(dif2n))]
    if dif2p.size==0:
        dif2p=-2*length
    if dif2n.size==0:
        dif2n=-2*length
    sol3=length-np.max(dif2p)
    sol4=-np.max(dif2n)-1
    sol=np.min(np.ceil(np.abs([sol1,sol2,sol3,sol4])))
    if sol>maxtime:
        return(-1)
    else:
        return int(sol)

def main2(length,maxtime,babuk):
    pos=babuk[:,0]
    dir=babuk[:,1]
    diffs=pos[np.newaxis,:]-pos[:,np.newaxis]
    for i in range(maxtime):
        prevdiffs=diffs
        pos +=dir
        dir*=(np.sign(pos-1)*2)-1
        dir*=(np.sign(length-pos)*2)-1
        diffs=pos[np.newaxis,:]-pos[:,np.newaxis]
        if np.sum(np.logical_not(diffs))>pos.size:
            return i+1
        if np.min(diffs*prevdiffs)<0:
            return i+1
    return -1

l=30
t=1000
b=np.array([[30 ,-1],
 [ 6 ,-1],
 [ 5 ,-1],
 [ 7 ,-1],
 [18 , 1]])

print(main2(l,t,b))