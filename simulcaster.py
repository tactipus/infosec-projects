import sys
import subprocess


procs = []
for i in range(20):
    proc = subprocess.Popen([sys.executable, 'email_sender.py', '{}in.csv'.format(i), '{}out.csv'.format(i)])
    procs.append(proc)

for proc in procs:
    proc.wait()