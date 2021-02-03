from netmiko import ConnectHandler

device_ip = ['172.31.182.1', '172.31.182.2', '172.31.182.3', '172.31.182.4', '172.31.182.5']
username = 'admin'
password = 'cisco'
loopback_ip = ['172.20.182.1', '172.20.182.2', '172.20.182.3', '172.20.182.4', '172.20.182.5']
for ip in device_ip:
    config = ['conf t', 'int loopback 0', 'ip add {} 255.255.255.255'.format(loopback_ip[device_ip.index(ip)]), 'end']
    device_params = {'device_type': 'cisco_ios',
                    'ip' : ip,
                    'username': username,
                    'password':password,
                    }

    with ConnectHandler(**device_params) as ssh:
        ssh.enable()
        ssh.send_config_set(config)
        result = ssh.send_command('sh ip int br')
        print('============= '+ssh.send_command('sh run | sect hostname')+' =============')
        print(result)
        print('==========================================================================')
