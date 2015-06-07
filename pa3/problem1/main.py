import random
import platform
import subprocess

rnf = open("random_numbers.txt", 'w')
for i in range(10000):
    rnf.write(str(random.randrange(0, 10000)) + " ")
rnf.close()

if platform.system() == 'Windows':
    cmd = "markov++.exe < alice30.txt"
else:
    cmd = "./markov++ < alice30.txt"
out_cpp = subprocess.check_output(cmd, shell=True)

if platform.system() == 'Windows':
    cmd = "markov_c.exe < alice30.txt"
else:
    cmd = "./markov_c < alice30.txt"
out_c = subprocess.check_output(cmd, shell=True)

cmd = "java Markov_j < alice30.txt"
out_j = subprocess.check_output(cmd, shell=True)

if (out_cpp == out_c) and (out_c == out_j):
    print("Success!")
else:
    print("Fail!")