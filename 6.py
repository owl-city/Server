import time
import subprocess

while True:
  subprocess.call(['sh', 'ss2.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '5.py'])
  subprocess.call(['nohup', 'python3', '7.py'])
  break