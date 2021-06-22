import os
import shutil

from PATH import *

cnt = 0


def cmpFile():
    global cnt
    stdout = open(OUT, 'r')
    cmpout = open(CMP, 'r')
    err = open(ERR, 'w')

    outline = cmpout.readlines()
    stdline = stdout.readlines()

    flag = True
    if len(outline) != len(stdline):
        print('line counts error')
        err.write('line counts error\n')
        return -1

    length = len(outline)
    for i in range(0, length):
        if outline[i] != stdline[i]:
            flag = False
            print('wrong output at line {0}, we get \"{1}\" when we expected \"{2}\"'.format(i + 1, outline[i], stdline[i]))
            err.write('wrong output at line {0}, we get \"{1}\" when we expected \"{2}\"\n'.format(i + 1, outline[i], stdline[i]))

    if flag:
        print("****************************************************")
        print('All test is right')
        print("****************************************************")
    else:
        cnt += 1
        os.chdir(PATH)
        shutil.copyfile("stdin.txt", "hack/stdin{0}.txt".format(cnt))
        shutil.copyfile("stdout.txt", "hack/stdout{0}.txt".format(cnt))
        shutil.copyfile("cmp.txt", "hack/cmp{0}.txt".format(cnt))
        shutil.copyfile("err.txt", "hack/err{0}.txt".format(cnt))
    stdout.close()
    cmpout.close()
