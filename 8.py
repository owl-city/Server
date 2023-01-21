import time
import subprocess

while True:
  subprocess.call(['sh', 'ss3.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '7.py'])
  subprocess.call(['nohup', 'python3', '6.py'])
  break