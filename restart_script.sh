#!/bin/sh
job_name='a3_1'
search_dir_path='/scratch/kvanka/job/tmp/'$job_name
restart_script_path='/scratch/kvanka/siddharth/restart_script'
code_dir_path='/scratch/kvanka/siddharth/code'

cd $code_dir_path
nohup python -u _restart.py $job_name $search_dir_path $restart_script_path | tee output.log &


