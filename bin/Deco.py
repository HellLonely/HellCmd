import time

def preset():
    file = open('bin/versions.txt')
    for i in range(4):
        print(file.readline())