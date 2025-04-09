import numpy as np

def main (s1,s2):
    s1=s1.replace("A","1").replace("T","2").replace("G","3").replace("C","4")
    s2=s2.replace("A","1").replace("T","2").replace("G","3").replace("C","4")
    flip=False
    dif=len(s2) - len(s1)
    if dif==0:
        s1=np.array(list(s1),dtype=int)
        s2=np.array(list(s2),dtype=int)
        return np.count_nonzero(s1-s2)
    elif dif<0:
        temp=s1
        s1=s2
        s2=s1
        flip=True
        dif=-dif
    s1=("0"*dif)+s1
    s1=np.array(list(s1),dtype=int)
    s2=np.array(list(s2),dtype=int)
    difs=[]
    for i in range(dif+1):
        s1c=np.roll(s1,-i)
        h1=np.repeat(np.arange(s2.size)[np.newaxis,:],s1.size-dif+1,axis=0)
        h2=np.repeat(np.arange(s1.size-dif+1)[:,np.newaxis],s2.size,axis=1)
        h=(h1>=(h2+dif-i))*(h1<(s2.size-i))
        s1a=s1c*h
        s2a=s2*h
        difs.append(np.count_nonzero(s1a-s2a,axis=1))
    difs=np.array(difs)
    difdifs=difs[1:]-difs[:-1]
    print(difdifs)
    final=difdifs[0]
    for i in range(dif-1):
        final=np.triu(final[np.newaxis]+difdifs[i+1][:,np.newaxis])
        print(final)
    soli=np.argmin(final)
    converted=[]
    divisor=s1.size-dif+1
    for i in range(dif):
        b=soli//(divisor^i)
        converted.append(b%divisor)
    print(converted)

s1="AT"
s2="AGTC"
main(s1,s2)