import time
import multiprocessing as mp
import concurrent.futures as cf
"""
    https://docs.python.org/3/library/concurrent.futures.html
"""

def main():
    start = time.perf_counter()
    confu()
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)}s')


def confu():
    with cf.ProcessPoolExecutor() as executor:
        pass

def mpr():
    start = time.perf_counter()
    
    processes: list = []
    for _ in range(8):
        p = mp.Process(target=calculate)
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    
    """
    for _ in range(10):
        calculate()
    """
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)}s')

def calculate():
    print(1231**124323)

if __name__ == "__main__":
    main()