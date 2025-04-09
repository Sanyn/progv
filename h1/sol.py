import numpy as np
import queue 

def main(rob,lab):
    f=rob-1
    q=queue.Queue()
    start=np.reshape(np.where(lab==8),[2])
    timestamp=0
    notchecked=np.full_like(lab,True)
    notchecked[start[0],start[1]] =False
    q.put([1,start])
    q.put([0])
    while not q.empty():
        step=q.get()
        if step[0] == 0:
            timestamp+=1
            q.put([0])
        elif step[0] == 1:
            coords=step[1]
            #left
            if coords[0] > 0:
                if notchecked[coords[0]-1,coords[1]]:
                    notchecked[coords[0]-1,coords[1]] = False
                    if lab[coords[0]-1,coords[1]] == 9:
                        return timestamp+1
                    elif lab[coords[0]-1,coords[1]] == 0:
                        q.put([1,[coords[0]-1,coords[1]]])
                    else:
                        q.put([2,[coords[0]-1,coords[1]],f])
            #right
            if coords[0] < lab.shape[0]-1:
                if notchecked[coords[0]+1,coords[1]]:
                    notchecked[coords[0]+1,coords[1]] = False
                    if lab[coords[0]+1,coords[1]] == 9:
                        return timestamp+1
                    elif lab[coords[0]+1,coords[1]] == 0:
                        q.put([1,[coords[0]+1,coords[1]]])
                    else:
                        q.put([2,[coords[0]+1,coords[1]],f])
            #up
            if coords[1] > 0:
                if notchecked[coords[0],coords[1]-1]:
                    notchecked[coords[0],coords[1]-1] = False
                    if lab[coords[0],coords[1]-1] == 9:
                        return timestamp+1
                    elif lab[coords[0],coords[1]-1] == 0:
                        q.put([1,[coords[0],coords[1]-1]])
                    else:
                        q.put([2,[coords[0],coords[1]-1],f])
            #down
            if coords[1] < lab.shape[1]-1:
                if notchecked[coords[0],coords[1]+1]:
                    notchecked[coords[0],coords[1]+1] = False
                    if lab[coords[0],coords[1]+1] == 9:
                        return timestamp+1
                    elif lab[coords[0],coords[1]+1] == 0:
                        q.put([1,[coords[0],coords[1]+1]])
                    else:
                        q.put([2,[coords[0],coords[1]+1],f])
        elif step[0] == 2:
            t=step[2]
            if t > 1:
                q.put([2,step[1],t-1])
            else:
                q.put([1,step[1]])

