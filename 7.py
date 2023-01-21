import time
import subprocess

while True:
  subprocess.call(['sh', 'ss3.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '8.py'])
  subprocess.call(['nohup', 'python3', '5.py'])
  break
