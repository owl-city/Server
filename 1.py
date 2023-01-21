import time
import subprocess

while True:
  subprocess.call(['sh', 'ss.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '2.py'])
  subprocess.call(['nohup', 'python3', '4.py'])
  break
