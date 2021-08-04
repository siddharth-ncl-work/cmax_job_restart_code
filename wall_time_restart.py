import time
import subprocess
import os
from datetime import datatime

proces_name=''
output_dir=''
output_file=''
  
def analyseQOutput():
  flag=None
  output=None
  with open('q.out','r') as file:
    output=file.readlines()
  if process_name in output:
    flag='running'
  else:
    flag='not_running'
return flag

def analyseDir():
  dir_flag=None
  output=os.listdir(output_dir)
  if output_file in output:
    dir_flag='present'
  else :
    output_flag='not_present'

def restart():
  
stop_flag=False
log_file=open('output.log','w')
while not stop_flag:
  log_file.write(str(datatime.today))
  subprocess.run(['/bin/bash', '-i', '-c', 'q'],stdout=open('q.out','w'),encoding='utf-8')
  q_flag=analyseQOutput()
  dir_flag=analyseDir()
  log_file.write(f'process is {q_flag},file is {dir_flag}')
  if q_flag=='not_running':
    if dir_flag=='present':
      log_file.write('restarting the  process')
      restart()
    else:
      log_file.write('process is not running, but might have converge or ran into the error\nTerminating the script!')
      stop_flag==True
  time.sleep(1)
