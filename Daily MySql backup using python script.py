import os
import subprocess
from datetime import datetime, timedelta
import boto3

# MySQL credentials
mysql_username = ""
mysql_password = ""
mysql_database = ""

# S3 bucket credentials
s3_bucket = ""
aws_access_key = ""
aws_secret_key = ""
aws_region = "us-east-1"

# Backup directory
backup_directory = "/backup/"

# Generate timestamp
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# MySQL backup command
mysql_dump_cmd = f"mysqldump -u {mysql_username} -p{mysql_password} {mysql_database} > {backup_directory}/backup_{timestamp}.sql"
mysql_dump_cmd = "mysqldump -u {} -p{} {} > {}/backup_{}.sql".format(mysql_username, mysql_password, mysql_database, backup_directory, timestamp)


# Execute MySQL backup
subprocess.run(mysql_dump_cmd, shell=True)

# S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)

# Upload backup to S3
backup_file = f"backup_{timestamp}.sql"
s3.upload_file(f"{backup_directory}/{backup_file}", s3_bucket, backup_file)

# Remove backup file from local directory
os.remove(f"{backup_directory}/{backup_file}")

print(f"Backup completed and uploaded to S3 bucket: {s3_bucket}/{backup_file}")
