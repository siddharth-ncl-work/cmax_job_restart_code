import subprocess
from subprocess import PIPE
import os
import time
import sys


def qFlag(job_name):
  q_flag='not_defined'
  p=subprocess.Popen(['qstat'],stdout=PIPE,stderr=PIPE)
  output=p.communicate()
  if job_name in output[0].split():
    q_flag='running'
  else:
    q_flag='not_running'
  return q_flag

def searchDirFlag(search_dir_path):
  search_dir_flag=None
  if not os.path.isdir(search_dir_path):
    return search_dir_flag
  for file in os.listdir(search_dir_path):
    if 'GEO_OPT_'in file:
      search_dir_flag=file.split('_')[-1]
      break
  return search_dir_flag

def restartJob(restart_script_path):
  subprocess.Popen(['qsub',restart_script_path])

def checkJob(job_name,search_dir_path,restart_script_path):
  stop_flag=False
  q_flag=qFlag(job_name)
  search_dir_flag=searchDirFlag(search_dir_path)
  print 'Job:{0} is {1} GEO_OPT_{2}'.format(job_name,q_flag,search_dir_flag)
  if q_flag=='not_running':
    stop_flag=True
    if search_dir_flag==None:
      print 'search directory: {0} is not present'.format(search_dir_path)
    elif search_dir_flag.lower()=='running':
      restartJob(restart_script_path)
      stop_flag=False
    elif search_dir_flag.lower()=='converged':
      pass
    elif search_dir_flag.lower()=='failed':
      pass
    else:
      print 'unknown GEO_OPT flag {0}'.format(search_dir_flag)
  elif q_flag=='running':
    stop_flag=False
    if search_dir_flag==None:
      print 'search directory: {0} is not present'.format(search_dir_path)
    elif search_dir_flag.lower()=='running':
      pass
    elif search_dir_flag.lower()=='converged':
      stop_flag=True
    elif search_dir_flag.lower()=='failed':
      stop_flag=True
    else:
      print 'unknown GEO_OPT flag {}'.format(search_dir_flag)
  return stop_flag

start_time=time.time()
print(sys.argv)
job_name=sys.argv[1]
search_dir_path=sys.argv[2]
restart_script_path=sys.argv[3]
interval=1
stop_flag=False
while not stop_flag:
  time.sleep(interval)
  elapsed_time=round(time.time()-start_time,2)
  print 'Time elapsed {0} seconds'.format(elapsed_time)
  stop_flag=checkJob(job_name,search_dir_path,restart_script_path)
  if stop_flag:
    print('Terminating the programme')
~

