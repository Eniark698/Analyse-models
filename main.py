from multiprocessing import Process
from alive_progress import alive_bar
from merge import merge
from concat_csv import get
from add_destination import dest


#func for executing in parallels
def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()
    


#actual program
if __name__ == "__main__":
    with alive_bar(3) as bar:
        bar()
        get()
        bar()
        runInParallel(dest, merge)
        bar()
       