import numpy as np

def main(width,height,maxtime):
    return 2, np.array([2,5])
    posx=babuk[:,0]
    posy=babuk[:,1]
    dirx=babuk[:,2]
    diry=babuk[:,3]
    diffsx=posx[np.newaxis,:]-posx[:,np.newaxis]
    diffsy =posy[np.newaxis,:]-posy[:,np.newaxis]
    for i in range(maxtime):
        prevdiffsx=diffsx
        prevdiffsy=diffsy
        posx+=dirx
        posy+=diry
        dirx*=(np.sign(posx-1)*2)-1
        dirx*=(np.sign(width-posx)*2)-1
        diry*=(np.sign(posy-1)*2)-1
        diry*=(np.sign(height-posy)*2)-1
        diffsx=posx[np.newaxis,:]-posx[:,np.newaxis]
        diffsy=posy[np.newaxis,:]-posy[:,np.newaxis]
        if np.sum(np.logical_not(np.abs(diffsx)+np.abs(diffsy)))>posx.size:
            return i+1
        if np.min(diffsx*prevdiffsx+diffsy*prevdiffsy)<0:
            return i+1
    return -1