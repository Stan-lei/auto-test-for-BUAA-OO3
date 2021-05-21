import networkx as nx
import data_generator as gen
import Exc
import sys
import subprocess
import time
import tester

PROC = "D:/IDEA/code/homework/homework10/out/production/homework10"


def java():
    PATH = ""
    MainClass = "MainClass"
    file = open('data.txt', 'r')
    out = open('java_ans.txt', 'w')

    t1 = time.perf_counter()

    proc = subprocess.Popen(
        f"java -cp {PROC} {MainClass}",
        shell=True,
        stdin=file,
        stdout=out,
        # stderr=sys.stdout,
        encoding="utf-8")
    proc.wait(10)

    t2 = time.perf_counter()

    file.close()
    out.close()
    return [t1, t2]


def python():
    out = open('python_ans.txt', 'w')
    p = subprocess.Popen('python tester.py', stdout=out, encoding='utf-8')
    p.wait(10)
    out.close()
    return p


def compare(File1, File2):
    file1 = open(File1, 'r')
    file2 = open(File2, 'r')
    ans1 = file1.readlines()
    ans2 = file2.readlines()
    file1.close()
    file2.close()
    if len(ans1) != len(ans2):
        print("length does not match")
        return False
    for i in range(min(len(ans1), len(ans2))):
        if ans1[i] != ans2[i]:
            print("In line {}".format(i + 1))
            print(ans1[i])
            print(ans2[i])
            print()
            return False


if __name__ == "__main__":
    for i in range(100):
        gen.generate_data()
        python()
        [t1, t2] = java()
        if t2 - t1 > 2.2:
            print("CPU TIME EXCEED with CPU TIME is {0}".format(t2 - t1))
            exit(0)
        if compare('python_ans.txt', 'java_ans.txt') == False:
            exit(0)
        print("No.{} has done.".format(i + 1))
