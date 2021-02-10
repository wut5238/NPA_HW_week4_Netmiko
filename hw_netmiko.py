from netmiko import ConnectHandler
# S0 and R0 manual config 
# R1-R5 auto config
# config static route to management plane
# config default route to nat in ospf
device_ip = ['172.31.182.3', '172.31.182.4', '172.31.182.5', '172.31.182.6', '172.31.182.7', '172.31.182.8', '172.31.182.9']
username = 'admin'
password = 'cisco'
loopback_ip = ['172.20.182.3', '172.20.182.4', '172.20.182.5', '172.20.182.6', '172.20.182.7', '172.20.182.8', '172.20.182.9']
for ip in device_ip:
    device_params = {'device_type': 'cisco_ios',
                    'ip' : ip,
                    'username': username,
                    'password':password,
                    }
    config_l0 = ['conf t', 'int loopback 0', 'ip add {} 255.255.255.255'.format(loopback_ip[device_ip.index(ip)]), 'end']
    with ConnectHandler(**device_params) as ssh:
        ssh.enable()
        # ssh.send_config_set(config_l0)
        result = ssh.send_command('sh ip int br')
        print('============= '+ssh.send_command('sh run | sect hostname')+' =============')
        print(result)
        print('==========================================================================')
