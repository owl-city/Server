import time
import subprocess

while True:
  subprocess.call(['sh', 'ss5.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '11.py'])
  subprocess.call(['nohup', 'python3', '10.py'])
  break