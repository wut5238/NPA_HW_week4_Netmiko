from jinja2 import Environment, FileSystemLoader
import yaml

def create():
    env = Environment(loader=FileSystemLoader('/home/devasc/Desktop/NPA_HW_week4_Netmiko/'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template('router.txt')

    devices = yaml.load(open('/home/devasc/Desktop/NPA_HW_week4_Netmiko/config_info.yaml'), Loader=yaml.FullLoader)

    path = "/home/devasc/Desktop/NPA_HW_week4_Netmiko/template/"
    for device in devices:
        config_file = path + device['name'] + '_config.txt'
        with open(config_file, 'w') as f:
            f.write(template.render(device))

create()
