import time
import subprocess

while True:
  subprocess.call(['sh', 'ss2.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '6.py'])
  subprocess.call(['nohup', 'python3', '8.py'])
  break