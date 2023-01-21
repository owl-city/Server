import time
import subprocess

while True:
  subprocess.call(['sh', 'ss4.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '9.py'])
  subprocess.call(['nohup', 'python3', '11.py'])
  break