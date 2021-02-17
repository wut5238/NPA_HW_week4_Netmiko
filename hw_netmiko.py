from netmiko import ConnectHandler
# S0 and R0 manual config 
# R1-R5 auto config
# config static route to management plane
# config default route to nat in ospf

username = 'admin'
password = 'cisco'

routers = [
    {
        "device_ip":"172.31.182.4",
        "interfaces":
            [
                {
                    "int":"l0",
                    "ip":"172.20.182.4",
                    "netmask":"255.255.255.255",
                    "wildcard":"0.0.0.0"
                },
                {
                    "int":"g0/1",
                    "ip":"172.31.182.17",
                    "netmask":"255.255.255.240",
                    "wildcard":"0.0.0.15"
                },
                {
                    "int":"g0/2",
                    "ip":"172.31.182.33",
                    "netmask":"255.255.255.240",
                    "wildcard":"0.0.0.15"
                }
            ]
    },
    {
        "device_ip":"172.31.182.5",
        "interfaces":
            [
                {
                    "int":"l0",
                    "ip":"172.20.182.5",
                    "netmask":"255.255.255.255",
                    "wildcard":"0.0.0.0"
                },
                {
                    "int":"g0/1",
                    "ip":"172.31.182.18",
                    "netmask":"255.255.255.240",
                    "wildcard":"0.0.0.15"
                },
                {
                    "int":"g0/2",
                    "ip":"172.31.182.49",
                    "netmask":"255.255.255.240",
                    "wildcard":"0.0.0.15"
                }
            ]
    },
    {
        "device_ip":"172.31.182.6",
        "interfaces":
            [
                {
                    "int":"l0",
                    "ip":"172.20.182.6",
                    "netmask":"255.255.255.255",
                    "wildcard":"0.0.0.0"
                },
                {
                    "int":"g0/1",
                    "ip":"172.31.182.34",
                    "netmask":"255.255.255.240",
                    "wildcard":"0.0.0.15"
                },
                {
                    "int":"g0/2",
                    "ip":"172.31.182.50",
                    "netmask":"255.255.255.240",
                    "wildcard":"0.0.0.15"
                },
                {
                    "int":"g0/3",
                    "ip":"172.31.182.65",
                    "netmask":"255.255.255.240",
                    "wildcard":"0.0.0.15"
                }
            ]
    },
    {
        "device_ip":"172.31.182.7",
        "interfaces":
            [
                {
                    "int":"l0",
                    "ip":"172.20.182.7",
                    "netmask":"255.255.255.255",
                    "wildcard":"0.0.0.0"
                },
                {
                    "int":"g0/1",
                    "ip":"172.31.182.66",
                    "netmask":"255.255.255.240",
                    "wildcard":"0.0.0.15"
                },
            ]
    },
    {
        "device_ip":"172.31.182.9",
        "interfaces":
            [
                {
                    "int":"l0",
                    "ip":"172.20.182.9",
                    "netmask":"255.255.255.255",
                    "wildcard":"0.0.0.0"
                },
                {
                    "int":"g0/1",
                    "ip":"172.31.182.67",
                    "netmask":"255.255.255.240",
                    "wildcard":"0.0.0.15"
                },
            ]
    }
]

def conf_loopback():
    for ip in routers:
        device_params = {'device_type': 'cisco_ios',
                        'ip' : ip["device_ip"],
                        'username': username,
                        'password':password,
                        }
        config_l0 = ['conf t', 'int loopback 0', 'ip add {} 255.255.255.255'.format(ip["interfaces"][0]['ip']), 'end']
        with ConnectHandler(**device_params) as ssh:
            ssh.enable()
            ssh.send_config_set(config_l0)
            result = ssh.send_command('sh ip int br')
            print('============= '+ssh.send_command('sh run | sect hostname')+' =============')
            print(result)
            print('==========================================================================')

def conf_int():
    for int in routers:
        device_params = {'device_type': 'cisco_ios',
                        'ip' : int["device_ip"],
                        'username': username,
                        'password':password,
                        }
        for num in range(1,len(int["interfaces"])):
            config_int = ['conf t', 'int {}'.format(int["interfaces"][num]["int"]), 'ip add {} {}'.format(int['interfaces'][num]["ip"], int['interfaces'][num]["netmask"]), 'no shut']
            with ConnectHandler(**device_params) as ssh:
                ssh.enable()
                ssh.send_config_set(config_int)
                result = ssh.send_command('sh ip int br')
        print()
        print(result)

def conf_ospf():

    for ip in routers:
        device_params = {'device_type': 'cisco_ios',
                        'ip' : ip["device_ip"],
                        'username': username,
                        'password':password,
                        }
        for num in range(0, len(ip["interfaces"])):
            config_ospf = ['conf t', 'router ospf 1', 'network {} {} area 0'.format(ip["interfaces"][num]["ip"], ip["interfaces"][num]["wildcard"])]
            with ConnectHandler(**device_params) as ssh:
                ssh.enable()
                ssh.send_config_set(config_ospf)
                result = ssh.send_command('sh run | sect ospf')
        print()
        print(result)
