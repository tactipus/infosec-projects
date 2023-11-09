import sys
import subprocess


procs = []
for i in range(100):
    proc = subprocess.Popen([sys.executable, 'vocal_ny_rsvp.py', '{}in.csv'.format(i), '{}out.csv'.format(i)])
    procs.append(proc)
    print("Process has been done!")

for proc in procs:
    proc.wait()