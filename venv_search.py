import subprocess
from pprint import pprint
import os
import sys

def list_virtual(path=".."):
    p = subprocess.Popen(f'find {path} | grep "bin/activate$"', shell=True, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()
    matching_paths = stdout.decode().split('\n')


    for t in matching_paths:
        q = subprocess.Popen(f'source {t} && pip list', shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        stdout, stderr = q.communicate()
        pip_output = stdout.decode().split('\n')

        print(os.path.abspath(t))
        pprint(pip_output)
        print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("greater than one")
        list_virtual(sys.argv[1])
    else:
         list_virtual()

