import subprocess
import sys
import boto3
import datetime

s3 = boto3.client('s3')

def main(argv):
    cmd = argv
    log_file_name = datetime.datetime.now(tzinfo=datetime.timezone.utc).strftime("%m_%d_%Y") + "_logfile"
    kickoff_subprocess(cmd, log_file_name)
    upload_output_to_S3(log_file_name)

def kickoff_subprocess(cmd, log_file_name):
    process = subprocess.call(cmd, shell=False)
    # not needed as with open() used
    # file = open(log_file_name, "a+")
    with open(log_file_name, 'a+') as file:
        timestamp = datetime.datetime.now(tzinfo=atetime.timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
        output = timestamp + " Command: "+ cmd[0] + " | Return Code: " + str(process) + "\n"
        file.write(output)

def upload_output_to_S3(log_file_name):
    with open(log_file_name, 'rb') as file:
        # not needed as with open() used
        # file = open(log_file_name, "rb")
        s3.upload_fileobj(file, "<FMI1>", log_file_name)
        file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
