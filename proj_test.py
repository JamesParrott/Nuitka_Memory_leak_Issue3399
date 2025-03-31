import gc
import threading

import proj_lib

def print_statistics():
    gc.collect()
    for obj in gc.garbage:
        print(f'LEAKED OBJECT!!!: {type(obj)} {obj}')
    all_objects = gc.get_objects()
    all_objects_len = len(all_objects)
    print(f'TOTAL OBJECTS: {all_objects_len}, INCREASE: {all_objects_len - print_statistics.all_objects_diff_cnt}')
    print_statistics.all_objects_diff_cnt = all_objects_len
    print(f'THREADS RUNNING: {threading.active_count()}')

print_statistics.all_objects_diff_cnt = 0

if __name__ == '__main__':
    print_statistics()

    for x in range(1, 100):
        for y in range(10):
            x = proj_lib.MyClass(x) # comment this line to get rid of the memory leaks in Nuitka built pyd file
            proj_lib.operation_with_match(x)
        print_statistics()
