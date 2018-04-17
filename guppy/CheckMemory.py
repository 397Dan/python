#!usr/bin/python
# coding = utf-8

def memory_usage_psutil():
    # return the memory usage in MB
    import psutil,os
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

def get_current_obj(a=[]):
    a.append([0]*1000)
    return a


def main():
    obj = []
    for i in range(1000):
        obj = get_current_obj(obj)
        if(i%100==0):
            print(memory_usage_psutil())
            from guppy import hpy
            hxx = hpy()
            heap = hxx.heap()
            print(heap)

if __name__=='__main__':
    main()