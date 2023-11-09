import sys
import subprocess


procs = []
for i in range(20):
    proc = subprocess.Popen([sys.executable, 'form_filler_code_blue.py', '{}in.csv'.format(i), '{}out.csv'.format(i)])
    procs.append(proc)

for proc in procs:
    proc.wait()