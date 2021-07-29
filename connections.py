import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def connection():
    try:
        stdin, stdout, stderr = ssh.exec_command('''
printf "echo ' '
whoami
cd /apps/some/path
ls -lrt
su - masapp
bash script.bash " | su - clrapp
''')

    except:
        print("Switching to user failed in server: 10.200.10.200")


try:
    ssh.connect("10.200.10.200", port, user, passw)
    connection()
except paramiko.SSHException:
    print("Server: 10.200.10.200 connection error")
ssh.close()

#################################Oracle DB connection###########

import cx_Oracle
import tabulate
from tabulate import tabulate

conn = "CLR_TRACKING/abcD@2021@10.200.20.200:1651/CYBENJP"
clrday = "select FIELD_VALUE from global_value_ctrl where FIELD_NAME = 'CLR_BUSINESS_DAY'"

con = cx_Oracle.connect(conn)
cursor = con.cursor()
cursor.execute(clrday)
epidata = cursor.fetchall()

fhead = ['File name', 'Import Date', 'Institution', 'Error', 'File Status', 'Checksum', 'File Id']
print(tabulate(epidata, headers=fhead, tablefmt='psql'))
cursor.close()
con.close()


########################Parallel SSH###############################

from pssh.clients import ParallelSSHClient

hosts = ['10.200.10.200', '10.200.20.201', '10.200.30.12', '10.200.21.34', '10.300.23.11']
client = ParallelSSHClient(hosts, port=22, user="user1", password="abcd123")
try:
    output = client.run_command('''
echo 'Disk space in EPI PROD Server:'
hostname
df -h''')

except:
    print("Connection timed out")


for host_output in output:
    for line in host_output.stdout:
        print(line)

exit_code = host_output.exit_code


#########################################Multi processing###################

from concurrent.futures import ThreadPoolExecutor

def some_function(ab, cd):
    pass

def some_function2(ab, cd):
    pass

def some_function3(ab, cd):
    pass

def some_function4(ab, cd):
    pass

def multi_process_tasks(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()



multi_process_tasks([
    lambda: some_function("abcd", "def"),
    lambda: some_function("defg", "123"),
    lambda: some_function2("abcd", "def"),
    lambda: some_function3("abcd", "def"),
    lambda: some_function4("abcd", "def")
])





