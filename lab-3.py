import subprocess
import sys
import boto3
import datetime

s3 = boto3.client('s3')

def main(argv):
    cmd = argv
    log_file_name = datetime.datetime.now(tzinfo=UTC).strftime("%m_%d_%Y") + "_logfile"
    kickoff_subprocess(cmd, log_file_name)
    upload_output_to_S3(log_file_name)

def kickoff_subprocess(cmd, log_file_name):
    process = subprocess.call(cmd, shell=False)
    file = open(log_file_name, "a+")
    timestamp = datetime.datetime.now(tzinfo=UTC).strftime("%m/%d/%Y, %H:%M:%S")
    output = timestamp + " Command: "+ cmd[0] + " | Return Code: " + str(process) + "\n"
    with open(log_file_name, 'a+') as file:
        file.write(output)

def upload_output_to_S3(log_file_name):
    with open(log_file_name, 'a+') as file:
        file = open(log_file_name, "rb")
        s3.upload_fileobj(file, "<FMI1>", log_file_name)
        file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
