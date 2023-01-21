import time
import subprocess

while True:
  subprocess.call(['sh', 'ss1.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '4.py'])
  subprocess.call(['nohup', 'python3', '1.py'])
  break