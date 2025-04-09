import numpy as np

def evaluate(problem,params,solution,testeesolution):
    if problem == "k1":
        return solution == testeesolution
    if problem == "k2":
        if solution == testeesolution[0]:
            if solution == -1:
                return True
            drink = params[1][0,0]
            inds=[0,0]
            for i in range(len(testeesolution[1])):
                if testeesolution[1][i] == "J":
                    inds[1]+=1
                else:
                    inds[0]+=1
                drink+=params[1][inds[0],inds[1]]-params[0]
            if drink ==solution:
                return True
        return False
    if problem == "k3":
        return solution == testeesolution
    if problem == "kb":
        return np.allclose(solution, testeesolution)
    if problem == "h1":
        return solution == testeesolution
    if problem == "h2":
        return solution == testeesolution
    if problem == "h3":
        num=testeesolution[0]
        bucks=testeesolution[1]
        if num!=solution:
            return False
        k=params[0]
        dobz=params[2]
        sz=dobz[bucks[0],0]
        sums=0
        for i in range(len(bucks)):
            if sz!=dobz[bucks[i],0]:
                return False
            sums+=dobz[bucks[i],1]
        return sums == k
    if problem == "hb":
        params=params[0]
        params=[params[0].tolist(),params[1].tolist(),params[2].tolist()]
        for i in range(testeesolution.shape[0]):
            move = testeesolution[i]
            if len(params[move[0]]) == 0:
                return False
            if len(params[move[1]]) != 0:
                if params[move[0]][-1] > params[move[1]][-1]:
                    return False
            params[move[1]].append(params[move[0]][-1])
            params[move[0]].pop()
        if len(params[0]) == 0:
            if len(params[1]) == 0:
                sols = np.array(params[2])
                is_sorted = lambda a: np.all(a[1:]<=a[:-1])
                return is_sorted(sols)
            