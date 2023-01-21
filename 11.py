import time
import subprocess

while True:
  subprocess.call(['sh', 'ss5.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '12.py'])
  subprocess.call(['nohup', 'python3', '9.py'])
  break