import signal
import numpy as np
import time
import testee
import loader
import eval

problem="h3"

class TestTimeout(Exception):
    pass

class test_timeout:
  def __init__(self, seconds, error_message=None):
    if error_message is None:
      error_message = 'test timed out after {}s.'.format(seconds)
    self.seconds = seconds
    self.error_message = error_message

  def handle_timeout(self, signum, frame):
    raise TestTimeout(self.error_message)

  def __enter__(self):
    signal.signal(signal.SIGALRM, self.handle_timeout)
    signal.alarm(self.seconds)

  def __exit__(self, exc_type, exc_val, exc_tb):
    signal.alarm(0)

points=0
timelim=loader.loadTimeLim(problem)
timeoutlim=int(np.ceil(timelim*2))
for i in range(10):
    params=loader.loadParams(problem,i+1)
    sol=loader.loadSol(problem,i+1)
    try:
    #if True:
        with test_timeout(timeoutlim):
            st=time.time()
            tsol=testee.main(*params)
            et=time.time()
        runtime=et-st
        if runtime < timelim:
            evaluation=eval.evaluate(problem,params,sol,tsol)
            if evaluation:
                print(f"Teszt {i+1}: Helyes megoldás")
                points+=1
            else:
                print(f"Teszt {i+1}: Helyestelen megoldás")
        else:
           print(f"Teszt {i+1}: Időlimit túllépés, futási idő: {runtime} másodperc")
    except TestTimeout:
        print(f"Teszt {i+1}: Időlimit túllépés, megszakítva {timeoutlim} másodpercnél")
    except:
        print(f"Teszt {i+1}: Futási hiba")

print(f"Összpontszám: {points}/10")