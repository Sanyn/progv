import numpy as np

def main(k,sz,f):
    maxk=np.sum(f[:,1])
    mins=np.full([sz,maxk],np.inf)
    mins[:,0] = np.full([sz],1)
    for i in range(f.shape[0]):
        c=f[i,0]
        alt=np.roll(mins[c],f[i,1])+1
        mins[c] = np.min([mins[c],alt],axis=0)
    solu=np.min(mins[:,k])
    if solu==np.inf:
        solu=-1
    return solu