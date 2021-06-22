import subprocess
import sys
import time

from PATH import *


def runJavaPro(test_name, delay):
    file = open(PATH + 'stdin.txt', 'r')
    out = open(CMP, 'w')
    time.sleep(delay)
    if test_name == "":
        print("test begin at {0}".format('my hw'))
    else:
        print("test begin at {0}".format(test_name))

    t1 = time.perf_counter()
    if test_name == "":
        test_Path = PROC
    else:
        test_Path = test_PATH + test_name
    proc = subprocess.Popen(
        f"java -cp {test_Path} {MainClass}",
        shell=True,
        stdin=file,
        stdout=out,
        stderr=sys.stdout,
        encoding="utf-8")
    proc.wait(10)
    t2 = time.perf_counter()

    file.close()
    out.close()
    return [t1, t2]

