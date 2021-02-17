import os
from netmiko import ConnectHandler
def main():
    username = 'admin'
    password = 'cisco'
    routers = ['172.31.182.4','172.31.182.5','172.31.182.6','172.31.182.7','172.31.182.9','172.31.182.3','172.31.182.8']
    files = []
    for file in os.listdir("/home/devasc/Desktop/NPA_HW_week4_Netmiko/template"):
        if file.endswith(".txt"):
            files.append(file)
    files.sort()
    for i in range(len(routers)):
        device_params = {'device_type': 'cisco_ios',
                        'ip' : routers[i],
                        'username': username,
                        'password':password,
                        }
        with ConnectHandler(**device_params) as ssh:
            ssh.enable()
            ssh.send_config_from_file('/home/devasc/Desktop/NPA_HW_week4_Netmiko/template/{}'.format(files[i]))
            result = ssh.send_command('sh run')
        print(result)
        print("==========================")
main()
