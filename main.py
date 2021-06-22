import threading

from answer_generator import *
from data_generator import *
from subPro import *
from cmp import *


class ThreadTB(threading.Thread):
    def __init__(self, Type, cnt, test_name, delay):
        threading.Thread.__init__(self)
        self.Type = Type
        self.cnt = cnt
        self.test_name = test_name
        self.delay = delay

    def run(self):
        print('Test {0}'.format(self.cnt))
        [t1, t2] = runJavaPro(self.test_name, self.delay)
        print('CPU TIME:', round(t2 - t1, 4))
        if round(t2 - t1, 4) > 2.2:
            print("CPU TIME EXCEED")


class AnsGen(threading.Thread):
    def __init__(self, Type):
        threading.Thread.__init__(self)

    def run(self):
        genAnswer()


if __name__ == '__main__':
    L = ['hw', 'saber', 'lancer', 'rider', 'caster', 'assassin', 'berserker']
    i = 0
    while True:
        i += 1
        # generate_data()
        clearAll()

        threads = []
        ansThread = AnsGen("ansGen")
        tbThread = ThreadTB("tb", i, "", 0.3)
        threads.append(ansThread)
        threads.append(tbThread)

        for t in threads:
            t.start()
            t.join()

        cmpFile()
        break

'''
        [t1, t2] = runJavaPro("", 0.3)
        print('CPU TIME:', round(t2 - t1, 4))
        if round(t2 - t1, 4) > 2.2:
            print("CPU TIME EXCEED")
        else:
'''