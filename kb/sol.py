import numpy as np

def main(M):
    start = np.zeros(M.shape[0])
    start[0] = 1
    sol = recursion(start,M,0)
    if sol[0] == -1:
        return []
    sol = np.array(sol)
    n2s=np.sum(sol==1)
    sol = sol[n2s-1:]
    sol = sol[::-1]
    n0s = np.sum(sol==0)
    sol = sol[n0s-1:]
    return sol
def recursion(V,M,d):
    Val=np.diag(V)
    Trades = Val@M
    maxinds=np.argmax(Trades,axis=0)
    maxvals=np.max(Trades,axis=0)
    if (np.sum(maxvals>V)):
        if d > M.shape[0]:
            return [-1]
        else:
            step = recursion(maxvals,M,d+1)
            if step[0] == -1:
                return [-1]
            else:
                prevtrade=step[-1]
                step.append(maxinds[prevtrade])
                return step
    else:
        return [1]