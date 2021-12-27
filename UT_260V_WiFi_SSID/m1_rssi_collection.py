# -*- coding: utf-8 -*-
import paramiko
from time import sleep
# Request the server for information
# created:2021.12.03
# usage:just run it
def rssi_collect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.31.155', 22, 'root', '3i1S@robotMIJA')
    for i in range(0,5):
        # i += 1
        stdin, stdout, stderr = ssh.exec_command('date')
        str1 = stdout.read().decode('utf-8')
        print(str1)
        stdin, stdout, stderr = ssh.exec_command('wpa_cli -iwlan0 scan')
        sleep(5)
        str2 = stdout.read().decode('utf-8')
        print(str2)
        stdin, stdout, stderr = ssh.exec_command('wpa_cli -iwlan0 scan_r')
        str3 = stdout.read().decode('utf-8')
        print(str3)
        sleep(25)
    ssh.close()

if __name__ == '__main__':
    rssi_collect()